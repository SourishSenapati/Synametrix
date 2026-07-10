# SyntroDynaMatrix

![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

**Recommended GitHub Repository Name:** `SyntroDynaMatrix`
**Recommended GitHub Description:** `Physics-informed computational models validating the thermodynamic constraints and chemical OPEX of Anaerobic Digestion and Microalgae Biorefineries.`
**Recommended GitHub Tags:** `techno-economic-analysis`, `thermodynamics`, `anaerobic-digestion`, `microalgae`, `biogas-upgrading`, `python`, `process-engineering`

---

## Technical Overview

Integration of microalgae with Anaerobic Digestion (AD) is frequently proposed for wastewater remediation and resource recovery (SAF lipids, biomethane). However, many proposed frameworks fail to account for physical constraints such as the latent heat of vaporization or digestate buffer capacity. 

This repository provides an executable computational engine to calculate mass transfer kinetics, Energy Return on Investment (EROI), and chemical operating expenditures (OPEX). It actively raises exceptions when a proposed biorefinery process violates the laws of thermodynamics or operates at a structural financial loss.

## Core Modules & Physics Validated

### 1. Gas-Liquid Mass Transfer (Biogas Upgrading)
Calculates the adiabatic compression energy required to achieve target volumetric mass transfer coefficients ($k_La$) for biogas sparging. It compares the blower energy penalty against the Lower Heating Value (LHV) of the purified biomethane to ensure EROI remains strictly `> 1.0`.

### 2. Chemical Economics (Struvite Precipitation)
Titrates the required Sodium Hydroxide (NaOH) against the raw alkalinity (buffer capacity) of the digestate. It proves that for high-alkalinity feedstocks (>80 meq/L), the daily chemical OPEX to raise pH mathematically exceeds the €120/tonne retail value of the precipitated struvite.

### 3. Thermodynamic Constraints (Lipid Extraction)
Calculates the latent heat of vaporization ($2.26$ MJ/kg) required to thermally dry an algal slurry. It dynamically compares the drying energy penalty against the 37 MJ/kg LHV of the extracted lipids, raising a `ThermodynamicViolationError` when drying requires more energy than the resulting fuel contains, physically proving the requirement for Hydrothermal Liquefaction (HTL) or wet-extraction.

---

## Hydrodynamic & Biological Modelling Output

The `generate_figures.py` rendering engine synthesizes mathematical models into publication-ready figures.

### Free Ammonia (FA) Toxicity Thermal Map
Models the Anthonisen et al. (1976) pH-dependent ammonium-free ammonia equilibrium to map exact toxicity thresholds against operational temperatures.
<p align="center">
  <img src="figures/png/4-01.png" alt="Free Ammonia Map" width="70%">
</p>

### Beer-Lambert Light Attenuation
Demonstrates the local light intensity decay across the reactor depth as a function of biomass concentration, identifying the exact physical location of the "dark core" onset.
<p align="center">
  <img src="figures/png/2-02.png" alt="Beer-Lambert Attenuation" width="70%">
</p>

### PINN Spatial Biomass Distribution Heatmap
Calculates mixing efficiency and flow stagnation zones within a tubular photobioreactor based on Physics-Informed Neural Network (PINN) inference.
<p align="center">
  <img src="figures/png/2-06.png" alt="PINN Heatmap" width="70%">
</p>

### Barlow Burst Pressure Analysis
Calculates failure zones for tubular reactors constructed from Borosilicate Glass versus PMMA at standard working pressures (0.6 MPa).
<p align="center">
  <img src="figures/png/2-05.png" alt="Barlow Burst Pressure" width="70%">
</p>

---

## Installation & Execution

1. Clone the repository and install dependencies:
   ```bash
   git clone https://github.com/YourUsername/SyntroDynaMatrix.git
   cd SyntroDynaMatrix
   pip install -r requirements.txt
   ```

2. Run the techno-economic audit suite:
   ```bash
   python biorefinery_tea_model.py
   ```

3. Generate the graphics:
   ```bash
   python generate_figures.py
   ```

## Citation

This computational framework was developed alongside the book chapter: 
**"Integration of Microalgae with Anaerobic Digestion"** by Sourish Senapati (National Institute of Technology, Rourkela, Odisha, India). 

If you utilize this model for process engineering or academic research, please cite the author.
