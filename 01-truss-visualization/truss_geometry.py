
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Create figures folder automatically
FIGURE_DIR = Path(__file__).parent / "figures"
FIGURE_DIR.mkdir(parents=True, exist_ok=True)
# --------------------------------------------------
# 1. Material properties
# --------------------------------------------------
E = 200 * 10**9  # Young's modulus (N/m^2)
A = 0.005       # Cross-sectional area (m^2)

# --------------------------------------------------
# 2. Define nodal coordinates [x, y]
# --------------------------------------------------
nodes = np.array([
    [0, 6],
    [4, 6],
    [8, 6],
    [12, 6],
    [16, 6],
    [12, 2],
    [8, 0],
    [4, 2]
])

# --------------------------------------------------
# 3. Define members [node_i, node_j]
# --------------------------------------------------
members = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 8],
    [1, 8],
    [2, 8],
    [3, 7],
    [4, 6],
    [3, 8],
    [3, 6]
])

# --------------------------------------------------
# 4. Create the plotting area
# --------------------------------------------------
fig, axes = plt.subplots(figsize=(10, 5))
axes.set_aspect("equal", adjustable="box")

# --------------------------------------------------
# 5. Plot all structural members
# --------------------------------------------------
for mbr in members:
    node_i = mbr[0]
    node_j = mbr[1]

    ix, iy = nodes[node_i - 1]
    jx, jy = nodes[node_j - 1]

    axes.plot([ix, jx], [iy, jy], "b-")

# --------------------------------------------------
# 6. Plot all nodes
# --------------------------------------------------
axes.plot(nodes[:, 0], nodes[:, 1], "bo")

# Add node numbers
for i, (x, y) in enumerate(nodes, start=1):
    axes.annotate(
        str(i),
        (x, y),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center"
    )

# --------------------------------------------------
# 7. Format and display the figure
# --------------------------------------------------
axes.set_xlabel("X-coordinate (m)")
axes.set_ylabel("Y-coordinate (m)")
axes.set_title("2D Truss Geometry")
axes.grid(True)

plt.tight_layout()

plt.savefig(
    FIGURE_DIR / "truss_geometry.png",
    dpi=600,
    bbox_inches="tight"
)

plt.show()
