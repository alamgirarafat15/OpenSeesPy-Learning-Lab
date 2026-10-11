# OpenSeesPy Learning Lab

A hands-on learning repository for structural analysis and visualization using Python, OpenSeesPy, and OpsVis.

This repository documents my step-by-step learning journey in computational structural engineering, starting with basic truss analysis and progressing toward frame analysis, modal analysis, nonlinear structural analysis, and earthquake response simulation.

The projects are intended for educational and research-learning purposes. External tutorials are acknowledged in the relevant sections.

---

## Project 01: Linear Static Analysis of a 2D Truss

### Overview

This project implements a linear static analysis of a two-dimensional (2D) truss structure using OpenSeesPy.

The model consists of 8 nodes and 13 truss members subjected to three concentrated vertical loads. The analysis evaluates nodal displacements and member axial forces and visualizes the undeformed geometry, deformed configuration, and tension/compression behavior.

### Model Properties

| Parameter | Value |
|---|---:|
| Spatial dimensions | 2D |
| Number of nodes | 8 |
| Number of truss members | 13 |
| Young's modulus, \(E\) | 200 GPa |
| Cross-sectional area, \(A\) | 0.005 m² |
| Analysis type | Linear static |
| Load at Node 2 | 10 kN downward |
| Load at Node 3 | 30 kN downward |
| Load at Node 4 | 5 kN downward |

### Tools and Technologies

- Python
- OpenSeesPy
- NumPy
- Matplotlib

### Project Structure

```text
OpenSeesPy-Learning-Lab/
├── 01-truss-visualization/
│   ├── truss_geometry.py
│   ├── truss_model.py
│   ├── figures/
│   │   ├── truss_geometry.png
│   │   ├── deflection plot.png
│   │   └── truss_tension_compression.png
│   └── results/
│       ├── nodal_displacements.csv
│       └── member_axial_forces.csv
├── [portal-frame-project-folder]/
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: Replace the portal-frame placeholder with the actual folder name if that project is included in this repository.*

---

## Results and Visualizations

### 1. Original Truss Geometry

The initial geometry illustrates the node coordinates and connectivity of the 13 truss members.

![Original Truss Geometry](01-truss-visualization/figures/truss_geometry.png)

### 2. Deformed Shape

The deformed configuration is plotted alongside the original structure. The displacements are amplified by a factor of 500 for visualization; therefore, the displayed deformation is not to scale.

![Truss Deflected Shape](01-truss-visualization/figures/deflection%20plot.png)

### 3. Tension and Compression Members

Blue lines represent members in tension, while red lines represent members in compression, according to the sign convention used in this model.

![Tension and Compression Diagram](01-truss-visualization/figures/truss_tension_compression.png)

---

## Numerical Results

### Nodal Displacements

The following table summarizes the calculated horizontal and vertical nodal displacements.

| Node | Horizontal, \(U_x\) (m) | Vertical, \(U_y\) (m) |
|---:|---:|---:|
| 1 | 0.00000 | 0.00000 |
| 2 | −0.00010 | −0.00063 |
| 3 | −0.00019 | −0.00073 |
| 4 | −0.00028 | −0.00057 |
| 5 | −0.00036 | 0.00000 |
| 6 | −0.00005 | −0.00055 |
| 7 | −0.00018 | −0.00058 |
| 8 | −0.00032 | −0.00059 |

The maximum downward displacement is approximately **0.73 mm at Node 3**.

Full results: [Nodal displacements CSV](01-truss-visualization/results/nodal_displacements.csv)

### Member Axial Forces

Positive axial forces indicate tension, and negative axial forces indicate compression under the sign convention used in this model.

| Member | Connectivity | Axial Force (kN) | Behavior |
|---:|:---:|---:|---|
| 1 | 1–2 | −23.75 | Compression |
| 2 | 2–3 | −23.75 | Compression |
| 3 | 3–4 | −21.25 | Compression |
| 4 | 4–5 | −21.25 | Compression |
| 5 | 5–6 | +30.05 | Tension |
| 6 | 6–7 | +27.95 | Tension |
| 7 | 7–8 | +27.95 | Tension |
| 8 | 1–8 | +33.59 | Tension |
| 9 | 2–8 | −10.00 | Compression |
| 10 | 3–7 | −25.00 | Compression |
| 11 | 4–6 | −5.00 | Compression |
| 12 | 3–8 | −1.77 | Compression |
| 13 | 3–6 | −5.30 | Compression |

Full results: [Member axial forces CSV](01-truss-visualization/results/member_axial_forces.csv)

### Key Findings

- 4 members are reported in tension and 9 in compression.
- The maximum tensile force is approximately 33.59 kN in Member 8.
- The maximum compression force magnitude is 25.00 kN in Member 10.
- The maximum downward nodal displacement is approximately 0.73 mm at Node 3.

These results are reported from the current implementation and have not been independently re-calculated here.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/alamgirarafat15/OpenSeesPy-Learning-Lab.git
cd OpenSeesPy-Learning-Lab
```

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

OpenSeesPy may require a compatible Python version and platform-specific dependencies. A virtual environment is recommended.

---

## Running Project 01

Run the geometry visualization:

```bash
python 01-truss-visualization/truss_geometry.py
```

Run the structural model and analysis:

```bash
python 01-truss-visualization/truss_model.py
```

The model script is intended to perform the analysis and extract numerical results. CSV export and figure generation depend on the code implemented in the relevant scripts.

---

## Learning Objectives

Through these projects, I aim to develop practical skills in:

- Defining nodes and structural elements in OpenSeesPy.
- Assigning material properties and cross-sectional properties.
- Applying boundary conditions and external loads.
- Configuring and performing linear static analysis.
- Extracting nodal displacements and member forces.
- Visualizing undeformed and deformed structural configurations.
- Interpreting numerical structural-analysis results.
- Performing eigenvalue and modal analysis.
- Developing nonlinear and earthquake time-history analysis workflows.
- Preparing structural response datasets for machine-learning research.

---

## Validation and Verification

For Project 01, the reported nodal displacements and member axial forces are compared with numerical results associated with the referenced EngineeringSkills introductory tutorial.

This comparison is intended as a basic implementation check. It does not constitute independent validation of the software, a comprehensive verification study, or certification for structural design.

---

## Learning References and Attribution

### 1. Introduction to OpenSeesPy

**Source:** EngineeringSkills

[Introduction to OpenSees and OpenSeesPy](https://www.engineeringskills.com/posts/introduction-to-opensees-and-openseespy)

This tutorial is a learning reference for introductory OpenSeesPy concepts and related structural-analysis exercises.

### 2. Parametric Frame Analysis with OpenSeesPy and OpsVis

**Original author:** Dr Seán Carroll  
**Source:** EngineeringSkills

[Building a Parametric Frame Analysis Pipeline with OpenSeesPy and OpsVis](https://www.engineeringskills.com/posts/building-a-parametric-frame-analysis-pipeline-with-openseespy-and-opsvis)

This tutorial covers parametric 2D frame modelling, elastic structural analysis, and visualization using OpenSeesPy and OpsVis.

If the portal-frame example in this repository uses code from this tutorial, the example should be clearly identified as tutorial-based. Any original code, figures, or other materials retained from the source remain subject to the source's applicable licence and permissions. Attribution does not replace permission to redistribute material.

Any independent modifications, extensions, or original implementations should be documented separately.

---

## Future Development

Planned learning and research stages include:

- 2D portal-frame analysis.
- Beam-column elements and section properties.
- Structural response visualization using OpsVis.
- Eigenvalue and modal analysis.
- Static lateral-load analysis and story-drift calculation.
- Nonlinear material modelling and nonlinear static analysis.
- Earthquake ground-motion input and transient time-history analysis.
- Nonlinear time-history analysis.
- Extraction of roof displacement, story drift, and other seismic response quantities.
- Seismic response dataset generation and machine-learning applications.

The status of each stage will be updated as the corresponding implementation is completed and checked.

---

## Disclaimer

This repository is intended for educational and research-learning purposes. The models and results should not be used directly for real-world structural design without appropriate independent verification, validation, and professional engineering review.

---

## Author

**Mohammad Arafat Alamgir**

Civil Engineering | Structural Analysis | OpenSeesPy | Computational Mechanics

GitHub: [@alamgirarafat15](https://github.com/alamgirarafat15)
