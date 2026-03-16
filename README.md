⸻

IDS_Project

Comparative Study of GAN-based Synthetic Data Augmentation for Intrusion Detection Systems

⸻

Introduction

This repository contains the data preprocessing pipeline for intrusion detection datasets used in the research project:

“Comparative Study of GAN-based Synthetic Data Augmentation for Intrusion Detection Systems.”

The purpose of this repository is to prepare raw intrusion detection datasets for machine learning experiments by performing:
	•	Data cleaning
	•	Feature encoding
	•	Feature normalization
	•	Class imbalance analysis
	•	Data visualization

The preprocessing workflow is implemented using Jupyter Notebooks to ensure transparency, reproducibility, and easy experimentation.

⸻

Table of Contents
	•	Project Structure￼
	•	Datasets Used￼
	•	Preprocessing Pipeline￼
	•	Installation￼
	•	Dependencies￼
	•	Usage￼
	•	Output￼
	•	Examples￼
	•	Troubleshooting￼
	•	Contributors￼
	•	License￼

⸻

Project Structure

IDS_Project
│
├── notebooks
│   ├── preprocess_unsw_nb15.ipynb
│   └── preprocess_cicids2017.ipynb
│
├── data_raw
│   (downloaded datasets placed here)
│
├── data_processed
│   (cleaned datasets generated after preprocessing)
│
├── plots
│   (class distribution charts and correlation heatmaps)
│
└── README.md


⸻

Datasets Used

1. UNSW-NB15 Dataset

Dataset Source
https://research.unsw.edu.au/projects/unsw-nb15-dataset

Expected directory structure:

data_raw/unsw_nb15/

    UNSW_NB15_training-set.csv
    UNSW_NB15_testing-set.csv


⸻

2. CICIDS2017 Dataset

Dataset Source
https://www.unb.ca/cic/datasets/ids-2017.html

Instructions:
	1.	Download the MachineLearningCSV.zip archive.
	2.	Extract the CSV files.
	3.	Place them in:

data_raw/cic-ids-2017/MachineLearningCVE/


⸻

Preprocessing Pipeline

The preprocessing workflow implemented in the notebooks performs the following steps:

1. Data Cleaning
	•	Removed duplicate rows
	•	Handled missing values
	•	Replaced infinite values with NaN
	•	Removed rows containing invalid values

2. Feature Encoding
	•	Converted categorical features to numerical values
	•	Used Label Encoding for categorical columns

3. Feature Normalization
	•	Numerical features were scaled between 0 and 1
	•	Implemented using MinMaxScaler

4. Train-Test Split

Each dataset was split into:
	•	70% Training Data
	•	30% Testing Data

5. Imbalance Analysis
	•	Analyzed class distribution
	•	Identified majority and minority attack classes

6. Data Visualization

Generated visual insights including:
	•	Class distribution bar charts
	•	Correlation heatmaps

⸻

Installation

Clone the repository:

git clone https://github.com/arjunshetty2003/IDS_Project.git
cd IDS_Project


⸻

Dependencies

Install the required Python packages:

pip install pandas numpy scikit-learn matplotlib seaborn jupyter

Main libraries used:
	•	pandas
	•	numpy
	•	scikit-learn
	•	matplotlib
	•	seaborn
	•	jupyter

⸻

Usage

Step 1 — Download datasets

Download datasets from the official sources listed above.

Step 2 — Place datasets in data_raw/

Follow the required directory structure.

Step 3 — Launch Jupyter Notebook

jupyter notebook

Step 4 — Run preprocessing notebooks

Open and execute:

notebooks/preprocess_unsw_nb15.ipynb
notebooks/preprocess_cicids2017.ipynb

Running these notebooks will reproduce the full preprocessing pipeline.

⸻

Output

After preprocessing, the cleaned datasets will be generated in:

data_processed/

    unsw_nb15_cleaned.csv
    cicids2017_cleaned.csv

Visualization outputs are stored in:

plots/

These include:
	•	Class distribution charts
	•	Correlation heatmaps

⸻

Examples

Example visualizations produced during preprocessing:
	•	Attack class distribution plots
	•	Feature correlation heatmaps

These visualizations help analyze dataset imbalance and feature relationships before model training.

⸻

Troubleshooting

Dataset not found error

Ensure datasets are placed exactly in the required folder structure:

data_raw/

Missing libraries

Install dependencies again:

pip install -r requirements.txt

Or install manually.

Notebook not executing

Ensure Jupyter Notebook is properly installed:

pip install jupyter


⸻

Contributors

Project developed by:

Aniket Kumar Sah
Arjun Shetty
Barsha Shah
Divyanshi Jha

⸻


