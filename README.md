# IDS_Project

Comparative Study of GAN-based Synthetic Data Augmentation for Intrusion Detection Systems

## Overview

This repository contains the preprocessing workflows used to prepare intrusion detection datasets for machine learning and synthetic data augmentation experiments.

Current scope:
- Data cleaning and schema normalization
- Feature encoding and normalization
- Train/test split preparation
- Class imbalance analysis
- Exploratory visualization (class distribution and correlation heatmaps)

## Reproducibility Policy

Rule of thumb:
- Code and notebooks belong in GitHub.
- Large datasets do not belong in GitHub history.
- README must explain exact setup and run steps.

Important:
- Do not commit files larger than GitHub limits (especially multi-GB CSV files).
- Keep only small sample files in data folders when needed for demonstration.

## Project Structure

```text
IDS_Project/
├── notebooks/
│   ├── preprocess_cicids2017.ipynb
│   ├── preprocess_unsw_nb15.ipynb
│   └── NSL-KDD preprocessing.ipynb
├── data_raw/                  # raw datasets placed manually
├── data_processed/            # generated cleaned datasets (sample files only in git)
├── plots/                     # generated figures
├── logs/                      # additional generated outputs
├── reports/
├── requirements.txt
└── README.md
```

## Datasets

### 1) UNSW-NB15

Source: https://research.unsw.edu.au/projects/unsw-nb15-dataset

Place files in:

```text
data_raw/unsw_nb15/
  UNSW_NB15_training-set.csv
  UNSW_NB15_testing-set.csv
```

Raw dataset folder (Google Drive):
https://drive.google.com/drive/folders/1hBD_q6HCL5TvmY0i6LAM7Myq-m9ay1Pv

### 2) CICIDS2017

Source: https://www.unb.ca/cic/datasets/ids-2017.html

Place MachineLearningCVE CSV files in:

```text
data_raw/cic-ids-2017/MachineLearningCVE/
```

Raw dataset folder (Google Drive):
https://drive.google.com/drive/folders/1eUKK6YCX0VGr0h2ak7Nnd646f9qxCqek

### 3) NSL-KDD

Place raw NSL-KDD file(s) in:

```text
data_raw/nsl_kdd/
```

Raw dataset folder (Google Drive):
https://drive.google.com/drive/folders/1nnDe6Rb3dgTXRmZH2hXA8n12kFvmG6Zs

## Reproducibility Guide

### 1) Clone repository

```bash
git clone https://github.com/arjunshetty2003/IDS_Project.git
cd IDS_Project
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Download datasets

Download the raw datasets from the Google Drive links in the Datasets section.

### 4) Place datasets

Ensure the folder layout exactly matches the paths shown in this README.

Quick placement checklist:
- CICIDS2017 raw CSV files -> data_raw/cic-ids-2017/MachineLearningCVE/
- UNSW-NB15 raw CSV files -> data_raw/unsw_nb15/
- NSL-KDD raw file(s) -> data_raw/nsl_kdd/

### 5) Run preprocessing notebooks

```bash
jupyter notebook
```

Run notebooks in this order:
- notebooks/preprocess_cicids2017.ipynb
- notebooks/preprocess_unsw_nb15.ipynb
- notebooks/NSL-KDD preprocessing.ipynb

## Preprocessing Pipeline (Implemented)

1. Merge/load raw files
2. Clean headers and remove duplicates
3. Handle invalid values (inf and NaN where applicable)
4. Encode categorical columns (LabelEncoder)
5. Normalize numeric columns (MinMaxScaler)
6. Split into train/test (70/30, random_state=42)
7. Analyze class imbalance
8. Generate plots
9. Save cleaned outputs

## Outputs

Generated artifacts include:
- data_processed/unsw_nb15_cleaned.csv
- data_processed/cicids2017_cleaned.csv (may be too large for GitHub, keep external)
- plots/cicids2017_plots/Class_Distribution_CICIDS2017.png
- plots/cicids2017_plots/CorrelationHeatmap_CICIDS2017.png
- logs/NSL_KDD_CLEANED.csv

## Expected Result

After running notebooks successfully:
- Cleaned datasets are created in data_processed/ and logs/
- Class distribution and correlation plots are generated in plots/

## Troubleshooting

### Label column KeyError in CICIDS notebook

Cause: raw header can contain leading spaces.

Fix:

```python
df.columns = df.columns.str.strip()
```

### Dataset not found

Verify folder names and file names exactly match the expected layout.

### Missing package

Reinstall dependencies:

```bash
pip install -r requirements.txt
```

## Contributors

- Aniket Kumar Sah
- Arjun Shetty
- Barsha Shah
- Divyanshi Jha


