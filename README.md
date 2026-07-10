# Synametrix: Industrial Biorefinery Thermodynamics & Economics Engine

![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)
![License: Proprietary/Academic](https://img.shields.io/badge/License-Proprietary_&_Academic-red.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

This repository contains a physics-informed techno-economic framework designed to audit and validate the thermodynamic constraints, mass transfer kinetics, and chemical operating expenditures (OPEX) of integrated Anaerobic Digestion (AD) and Microalgae biorefineries.

The computational models actively prevent the design of biological systems that violate thermodynamic principles or operate at a structural financial loss.

---

## Table of Contents
1. [Theoretical Background & Industry Gaps](#theoretical-background--industry-gaps)
2. [Core Computational Modules](#core-computational-modules)
3. [Hydrodynamic & Biological Output](#hydrodynamic--biological-output)
4. [Installation & Requirements](#installation--requirements)
5. [Command Line Interface (CLI)](#command-line-interface-cli)
6. [Citation & Academic Use](#citation--academic-use)
7. [Commercial Licensing & Hiring](#commercial-licensing--hiring)

---

## Theoretical Background & Industry Gaps

The integration of microalgae cultivation with Anaerobic Digestion is frequently proposed for wastewater remediation and resource recovery (e.g., lipid extraction, biomethane upgrading). 

However, proposed conceptual frameworks often fail at pilot scale due to physical and economic constraints:
* **The Latent Heat of Vaporization:** Drying algal slurry requires 2.26 MJ/kg of energy. If the extracted lipids yield 37 MJ/kg of energy, thermal drying inherently creates a negative Energy Return on Investment (EROI).
* **Buffer Capacity (Alkalinity):** Digestate frequently contains >80 meq/L of alkalinity. Using Sodium Hydroxide (NaOH) to raise the pH for struvite precipitation results in chemical costs that exceed the retail value of the recovered fertilizer.
* **Mass Transfer Kinetics:** Sparging raw biogas into microalgae cultures for CO2 mitigation requires blower compression energy. If the volumetric mass transfer coefficient (k_La) is inadequate, the blower consumes more electricity than the upgraded biomethane generates.

This framework calculates these physical limits and explicitly raises a `ThermodynamicViolationError` if a proposed system is physically or economically non-viable.

---

## Core Computational Modules

### 1. Gas-Liquid Mass Transfer (Biogas Upgrading)
Calculates the adiabatic compression energy required to achieve target volumetric mass transfer coefficients (k_La) for biogas sparging. It models the two-film theory of mass transfer to ensure the blower energy penalty remains strictly below the Lower Heating Value (LHV) of the purified biomethane.

### 2. Chemical Economics (Struvite Precipitation)
Simulates chemical titration of Sodium Hydroxide (NaOH) against the raw alkalinity (buffer capacity) of the digestate. It quantifies the daily chemical OPEX against the retail value of the precipitated struvite.

### 3. Thermodynamic Constraints (Lipid Extraction)
Calculates the latent heat required to thermally dry an algal slurry. It dynamically compares the drying energy penalty against the energy density of the extracted lipids. If the extraction energy exceeds the resulting fuel yield, it demonstrates the necessity for Hydrothermal Liquefaction (HTL) or wet-extraction architectures.

---

## Hydrodynamic & Biological Output

The Synametrix rendering engine synthesizes complex differential equations into standard figures.

### Free Ammonia (FA) Toxicity Thermal Map
Models the Anthonisen et al. (1976) pH-dependent ammonium-free ammonia equilibrium to map exact toxicity thresholds against operational temperatures in the anaerobic digester.
<p align="center">
  <img src="figures/png/4-01.png" alt="Free Ammonia Map" width="70%">
</p>

### Beer-Lambert Light Attenuation
Demonstrates the local light intensity decay across the reactor depth as a function of biomass concentration, identifying the physical location of the dark core onset.
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

## Installation & Requirements

Requires Python 3.10+. 

1. Clone the repository:
   ```bash
   git clone https://github.com/SourishSenapati/Synametrix.git
   cd Synametrix
   ```

2. Install the package in editable mode:
   ```bash
   pip install -e .
   ```

3. Install visualization dependencies (for generating graphs):
   ```bash
   pip install matplotlib numpy
   ```

---

## Command Line Interface (CLI)

Once installed, Synametrix acts as a globally available command-line tool.

### Run the Techno-Economic Audit
Execute the core thermodynamic and economic exception engine:
```bash
synametrix
```
Output: The engine will simulate mass transfer, precipitation, and extraction. If thermodynamic laws are violated, it will terminate with a `ThermodynamicViolationError`.

### Generate Publication Figures
To synthesize the mathematical models into TIFF/PNG format:
```bash
python -m synametrix.visualization.plotter
```

---

## Citation & Academic Use

This computational framework was developed alongside the book chapter: 
"Integration of Microalgae with Anaerobic Digestion" by Sourish Senapati (National Institute of Technology, Rourkela, Odisha, India). 

Synametrix is protected under a Custom Proprietary & Academic License. 

**For Academic Use:**
Use of this software by researchers, scientific institutions, or educational entities is subject to strict attribution covenants:
* **Supplemental Reliance:** If utilized for data verification or minor referencing, you are legally bound to provide explicit bibliographic citation of the author's original prior art.
* **Substantial Reliance:** If this computational architecture constitutes a core methodological component of your research, you are strictly prohibited from publishing without extending a formal offer of Joint Authorship to Sourish Senapati.

---

## Commercial Licensing & Hiring

Commercial entities (consultancies, EPC contractors, startups, industrial plants) are strictly prohibited from using these models without formal authorization.

To acquire commercial rights to deploy this architecture on proprietary backend servers, or to integrate this logic into industrial biorefinery SCADA systems, you must purchase a commercial license or hire the author.

To discuss commercial deployment, consulting, or employment opportunities, please contact Sourish Senapati directly via GitHub.
