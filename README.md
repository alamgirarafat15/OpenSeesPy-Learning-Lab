OpenSeesPy Learning Lab

A hands-on learning project focused on structural analysis using Python and OpenSeesPy.

Project 01: 2D Truss Analysis

This project implements a linear static analysis of a 2D truss structure using OpenSeesPy.

Features

Truss geometry and node visualization

Elastic material and truss element definition

Support and nodal load definition

Linear static analysis

Nodal displacement extraction

Member axial force calculation

Deformed shape visualization

Tension and compression member visualization

Tools and Technologies

Python

OpenSeesPy

NumPy

Matplotlib

Project Structure

OpenSeesPy-Learning-Lab/
├── 01-truss-visualization/
│   ├── truss_geometry.py
│   ├── truss_model.py
│   └── figures/
├── requirements.txt
├── .gitignore
└── README.md

Installation

Install the required packages:

python -m pip install -r requirements.txt

Running the Analysis

Run the following commands from the project root:

python 01-truss-visualization/truss_geometry.py
python 01-truss-visualization/truss_model.py

Learning Objectives

Understand the workflow of defining a structural model, applying loads, performing static analysis, extracting results, and visualizing structural response using OpenSeesPy.

Learning Source

The implementation follows the concepts presented in the EngineeringSkills introduction to OpenSeesPy tutorial.

Disclaimer

This repository is an educational learning project, not a validated structural design tool.