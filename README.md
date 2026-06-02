# CV-QEC: Continuous-Variable Quantum Error Correction

This repository contains the numerical simulations for the paper:

**"Discrete-variable assisted error correction of continuous-variable quantum information"**  
Negin Razian, En-Jui Chang, and Hoi-Kwan Lau  
Department of Physics, Simon Fraser University

## Abstract

We propose a novel CV quantum error correction (QEC) scheme that utilizes 
discrete-variable (DV) ancilla to extract information about CV displacement errors 
and counteract them — without requiring GKP states.

A single-qubit ancilla can suppress CV infidelity by more than 20%. 
By concatenating with DV QEC codes, the scheme is robust against physical 
errors in hybrid CV-DV systems.

## Contents

- `cv_qec.ipynb` — Main notebook reproducing the paper figures
  - Displacement error channel
  - Filter function after qubit measurement
  - Variance suppression vs qudit dimension d
  - Optimal conditional displacement strength α

## Key Results

- Single-qubit ancilla suppresses displacement variance by **36.8%**
- With squeezing, total variance reduced by **20.5%**
- Variance scales as **1/d** with qudit dimension d

## Requirements

```bash
pip install numpy scipy matplotlib
```

## Related

- arXiv: [https://arxiv.org/abs/2604.06565]
- Contact: neginsadat.razian@gmail.com
