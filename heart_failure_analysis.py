# GitHub repository: https://github.com/edjavi120/heart-failure-analysis

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    # Load the libraries we use in this notebook.
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    return mo, pd, plt, sns


@app.cell
def _(mo):
    mo.md(r"""
    # Heart Failure: Ejection Fraction and Kidney Function

    **Group members:** Edgar Ocasio-Arce, Cristobal Gonzalez and Robinson D. Willie

    **GitHub:** https://github.com/edjavi120/heart-failure-analysis

    ## Research question
    **Does the link between reduced ejection fraction and death depend on kidney function (serum creatinine)?**

    ## Dataset
    This dataset contains medical records of 299 patients who already had heart failure, collected in 2015
    at the Faisalabad Institute of Cardiology and the Allied Hospital in Faisalabad, Pakistan.

    Source: Heart Failure Clinical Records [Dataset]. (2020). UCI Machine Learning Repository. https://doi.org/10.24432/C5Z89R

    The columns we use:

    - `ejection_fraction`: the percentage of blood the heart pumps out with each beat (lower means a weaker heart)
    - `serum_creatinine`: the level of creatinine in the blood (higher means the kidneys are not clearing waste well)
    - `DEATH_EVENT`: 1 if the patient died during the follow-up period, 0 if they survived
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## What does the dataset contain?
    Before making any charts, we load the file and look at what is in it.
    """)
    return


@app.cell
def _(pd):
    # Load the CSV file into a DataFrame called df and display it.
    df= pd.read_csv("heart_failure_clinical_records_dataset.csv")
    df
    return (df,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Adding computed columns
    The raw numbers are hard to compare, so we add three columns that put each patient into a group:

    - `ef_category`: Reduced (EF of 30 or below), Mid (31 to 45), or Preserved (above 45)
    - `kidney_function`: High creatinine (above 1.5) or Normal creatinine (1.5 or below)
    - `outcome`: "Died" or "Survived", so the charts are easier to read than 0 and 1
    """)
    return


@app.cell
def _(df):
    # Start everyone as "Mid", then relabel the low and high EF patients.
    df["ef_category"] = "Mid"
    df.loc[df["ejection_fraction"] <= 30, "ef_category"] = "Reduced"
    df.loc[df["ejection_fraction"] > 45, "ef_category"] = "Preserved"

    # Label kidney function based on a creatinine cutoff of 1.5.
    df["kidney_function"] = "Normal creatinine"
    df.loc[df["serum_creatinine"] > 1.5, "kidney_function"] = "High creatinine"

    # Turn the 0/1 death column into words.
    df["outcome"] = "Survived"
    df.loc[df["DEATH_EVENT"] == 1, "outcome"] = "Died"

    # Show only the columns that matter for our question.
    df[["ejection_fraction", "ef_category", "serum_creatinine", "kidney_function", "outcome"]]
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    # Part 1: Ejection fraction
    *NAME*

    ## How is ejection fraction spread out across patients?
    We make a histogram of ejection fraction, with lines marking our cutoffs at 30 and 45.
    """)
    return


@app.cell
def _(df, plt, sns):
    # Histogram of ejection fraction, with red lines at the category cutoffs.
    sns.histplot(data=df, x="ejection_fraction")
    plt.axvline(30, color="red", linestyle="--", label="Reduced cutoff (30%)")
    plt.axvline(45, color="green", linestyle="--", label="Preserved cutoff (45%)")
    plt.title("Distribution of Ejection Fraction")
    plt.xlabel("Ejection Fraction (%)")
    plt.ylabel("Number of Patients")
    plt.legend()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Do patients with reduced ejection fraction die more often?
    We group the patients by EF category and take the mean of `DEATH_EVENT`.
    Since `DEATH_EVENT` is 1 for died and 0 for survived, the mean is the proportion of patients who died.
    """)
    return


@app.cell
def _(df):
    # Group by EF category and find the proportion who died in each group.
    df.groupby("ef_category")["DEATH_EVENT"].mean()
    return


@app.cell
def _(mo):
    mo.md(r"""
    About 55% of patients with reduced EF died, compared with about 21 to 23% in the other two groups.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    # Part 2: Kidney function
    *NAME*

    ## How many patients have high creatinine, and how often did they die?
    We filter the dataset to keep only patients with creatinine above 1.5.
    """)
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Who had the highest creatinine?
    We sort the high-creatinine patients from highest to lowest to see whether the most extreme values belong to patients who died.
    """)
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Is creatinine higher in patients who died?
    We make box plots comparing creatinine between patients who survived and patients who died.
    """)
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(r"""
    Patients who died had higher creatinine overall, and about 64% of high-creatinine patients died, compared with 32% of all patients.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    # Part 3: Putting it together
    *NAME*

    ## Do deaths cluster where EF is low and creatinine is high?
    We make a scatter plot of creatinine against ejection fraction, colored by outcome.
    """)
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Does high creatinine change the death rate at every EF level?
    This is our main question. We group by both EF category and kidney function and find the proportion who died in each combination.
    """)
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    # Conclusion
    **Yes, the link between reduced ejection fraction and death depends on kidney function.**

    - Reduced EF on its own is risky: about 55% of patients with EF of 30 or below died.
    - High creatinine raises the proportion who died in every EF group. With reduced EF, it goes from about 46% to 72%.
    - The biggest jump is in the Mid EF group, from about 12% to 59%.

    **Limitations:** only 6 patients have both preserved EF and high creatinine, so that bar is not reliable.
    Our cutoffs (30, 45, and 1.5) are simple choices, and this shows a pattern in the data, not proof that one thing causes the other.
    """)
    return


if __name__ == "__main__":
    app.run()
