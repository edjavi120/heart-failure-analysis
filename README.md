# Heart Failure: Ejection Fraction and Kidney Function

**Group members:** Edgar Ocasio-Arce, Cristobal Gonzalez, Robinson D. Willie

## What this project is
This project analyzes the Heart Failure Clinical Records dataset (299 patients) to answer one question:

> Does the link between reduced ejection fraction and death depend on kidney function (serum creatinine)?

The analysis is in a [marimo](https://marimo.io) notebook. It groups patients by ejection fraction category and kidney function and compares death rates using tables, a histogram, a boxplot, a scatter plot, and a grouped bar chart.

**Dataset:** Heart Failure Clinical Records [Dataset]. (2020). UCI Machine Learning Repository. https://doi.org/10.24432/C5Z89R

## Files
- `heart_failure_analysis.py`: the marimo notebook
- `heart_failure_clinical_records_dataset.csv`: the dataset

## How to run it
1. Install Python 3.10 or newer.
2. Install the required packages:
   ```bash
   pip install marimo pandas matplotlib seaborn
   ```
3. From this folder, open the notebook:
   ```bash
   marimo edit heart_failure_analysis.py
   ```
   To view it as a read-only app, run `marimo run heart_failure_analysis.py` instead.
