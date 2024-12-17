# Battery Dataset Analysis

This repository contains Python code to analyze and visualize how battery impedance parameters, such as electrolyte resistance (`Re`) and charge transfer resistance (`Rct`), change as Li-ion batteries age through charge/discharge cycles. The analysis is based on the [NASA Battery Dataset](https://www.kaggle.com/datasets/patrickfleith/nasa-battery-dataset/data).

---

## Dataset Description

The dataset comprises measurements from Li-ion batteries subjected to different operational profiles (charge, discharge, and impedance). Impedance measurements were carried out using Electrochemical Impedance Spectroscopy (EIS) with frequency sweeps from 0.1Hz to 5kHz. 

The study tracks aging effects due to repeated charge/discharge cycles, with experiments concluding when batteries reached the end-of-life (EOL) criteria.

---

## Visualization Overview

Using the **Plotly** library, the code generates an interactive plot showing the variation of:

- `Re`: Estimated electrolyte resistance (Ohms)
- `Rct`: Estimated charge transfer resistance (Ohms)

as a function of charge/discharge cycle numbers.

---

## Results

![Result Image]()

This image depicts the variation of electrolyte resistance (Re) and charge transfer resistance (Rct) with increasing charge/discharge cycles. We observe a gradual increase in both resistances, indicating battery degradation as the cycles progress.

---

## Steps to Reproduce the Analysis

###  **Install Dependencies**
Make sure to install the required libraries before running the code:

```bash
pip install pandas plotly

---
