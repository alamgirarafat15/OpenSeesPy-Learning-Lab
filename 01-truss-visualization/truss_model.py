import openseespy.opensees as ops

# Reset OpenSees model
ops.wipe()

# 2D model: 2 dimensions, 2 DOFs per node
ops.model("basic", "-ndm", 2, "-ndf", 2)

# Material and cross-sectional area
E = 200e9
A = 0.005

# Node coordinates
nodes = [
    [0, 6], [4, 6], [8, 6], [12, 6],
    [16, 6], [12, 2], [8, 0], [4, 2]
]

# Create nodes
for i, coord in enumerate(nodes, start=1):
    ops.node(i, coord[0], coord[1])

# Truss connectivity
members = [
    [1, 2], [2, 3], [3, 4], [4, 5],
    [5, 6], [6, 7], [7, 8], [1, 8],
    [2, 8], [3, 7], [4, 6], [3, 8], [3, 6]
]

# Define elastic material
ops.uniaxialMaterial("Elastic", 1, E)

# Create truss elements
for i, member in enumerate(members, start=1):
    ops.element("Truss", i, member[0], member[1], A, 1)

# Define supports
ops.fix(1, 1, 1)  # Node 1: pin support
ops.fix(5, 0, 1)  # Node 5: horizontal roller

# Define time series
ops.timeSeries("Constant", 1)

# Define load pattern
ops.pattern("Plain", 1, 1)

# Apply nodal loads (Fx, Fy) in Newtons
ops.load(2, 0.0, -10000.0)
ops.load(3, 0.0, -30000.0)
ops.load(4, 0.0, -5000.0)
# -----------------------------
# Analysis configuration
# -----------------------------

ops.system("BandSPD")
ops.numberer("RCM")
ops.constraints("Plain")

ops.integrator("LoadControl", 1.0)
ops.algorithm("Linear")
ops.analysis("Static")

# Run analysis
result = ops.analyze(1)

if result == 0:
    print("Static analysis completed successfully!")
else:
    print("Analysis failed. Error code:", result)
# -----------------------------
# Nodal Displacements
# -----------------------------

if result == 0:
    print("\n--- Nodal Displacements ---")

    for i, n in enumerate(nodes):
        ux = round(ops.nodeDisp(i + 1, 1), 5)
        uy = round(ops.nodeDisp(i + 1, 2), 5)

        print(f"Node {i + 1}: Ux = {ux} m, Uy = {uy} m")
    import matplotlib.pyplot as plt

# -----------------------------
# Plot the deformed shape
# -----------------------------

if result == 0:

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_aspect("equal", adjustable="box")

    xFac = 500  # Amplification factor

    for mbr in members:
        node_i = int(mbr[0])
        node_j = int(mbr[1])

        # Original coordinates
        ix, iy = nodes[node_i - 1]
        jx, jy = nodes[node_j - 1]

        # Original structure: grey
        ax.plot([ix, jx], [iy, jy], color="grey", linewidth=1)

        # Nodal displacements
        ux_i, uy_i = ops.nodeDisp(node_i)
        ux_j, uy_j = ops.nodeDisp(node_j)

        # Deformed structure: red
        ax.plot(
            [ix + ux_i * xFac, jx + ux_j * xFac],
            [iy + uy_i * xFac, jy + uy_j * xFac],
            color="red",
            linewidth=1.5
        )

    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Distance (m)")
    ax.set_title("Truss Deflected Shape (500x Amplification)")
    ax.grid(True)
    plt.tight_layout()
    plt.show()
# -----------------------------
# Member Axial Forces
# -----------------------------

if result == 0:
    import numpy as np

    mbrForces = np.array([])

    print("\n--- Member Axial Forces ---")

    for i, mbr in enumerate(members):
        axialForce = round(ops.basicForce(i + 1)[0] / 1000, 2)

        mbrForces = np.append(mbrForces, axialForce)

        print(
            f"Force in member {i + 1} "
            f"(nodes {mbr[0]} to {mbr[1]}) "
            f"is {axialForce} kN"
        )
    # -----------------------------
# Tension / Compression Plot
# -----------------------------

from pathlib import Path

if result == 0:

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_aspect("equal", adjustable="box")

    for i, mbr in enumerate(members):
        node_i = int(mbr[0])
        node_j = int(mbr[1])

        ix, iy = nodes[node_i - 1]
        jx, jy = nodes[node_j - 1]

        force = mbrForces[i]

        if abs(force) < 0.001:
            color = "grey"
            linestyle = "--"
        elif force > 0:
            color = "blue"       # Tension
            linestyle = "-"
        else:
            color = "red"        # Compression
            linestyle = "-"

        ax.plot(
            [ix, jx],
            [iy, jy],
            color=color,
            linestyle=linestyle,
            linewidth=2
        )

        # Member number
        ax.text(
            (ix + jx) / 2,
            (iy + jy) / 2,
            str(i + 1),
            fontsize=9
        )

    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Distance (m)")
    ax.set_title("Truss Members: Tension and Compression")
    ax.grid(True)

    # Legend
    from matplotlib.lines import Line2D

    legend_items = [
        Line2D([0], [0], color="blue", lw=2, label="Tension"),
        Line2D([0], [0], color="red", lw=2, label="Compression"),
        Line2D(
            [0], [0],
            color="grey", lw=2, linestyle="--",
            label="Near-zero force"
        )
    ]

    ax.legend(handles=legend_items)
    plt.tight_layout()

    # Save figure
    FIGURE_DIR = Path(__file__).parent / "figures"
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    save_path = FIGURE_DIR / "truss_tension_compression.png"

    fig.savefig(save_path, dpi=600, bbox_inches="tight")
    print(f"\nTension-compression plot saved to: {save_path}")
from pathlib import Path

FIGURE_DIR = Path(__file__).parent / "figures"
FIGURE_DIR.mkdir(parents=True, exist_ok=True)

fig.savefig(
    FIGURE_DIR / "truss_geometry.png",
    dpi=600,
    bbox_inches="tight"
)
plt.show()
plt.close(fig)

print("Loads defined successfully!")
print("OpenSeesPy model created successfully!")
print("Number of nodes:", len(nodes))
print("Number of truss members:", len(members))