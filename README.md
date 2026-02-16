# The Work-Study-Life Profile: A Quantified Self Analysis

A data science project analyzing daily habits of a working student using **exploratory data analysis**, **statistical techniques**, and **pattern identification** to understand behavioral profiles.

## Project Overview

This study explores the concept of the "Quantified Self" by analyzing daily habits over an **81-day period** (November 2025 to February 2026). The project employs **K-Means clustering as an exploratory technique** to identify distinct "Daily Profiles" and uses **ANOVA** to validate whether these patterns significantly differ in terms of mood and focus ratings.

**Focus**: Data Science Concepts - Understanding the dataset through statistical analysis, not predictive modeling.

## Project Structure

The project is organized into separate notebooks for different phases:

### Phase 1 & 2: Data Cleaning and Exploratory Data Analysis (EDA)
**File:** `1data_cleaning.ipynb`
- Load and inspect raw data
- Handle missing values and data quality issues
- Parse and validate dates
- **Exploratory Data Analysis**: Descriptive statistics, visualizations, correlation analysis
- Feature selection for analysis
- StandardScaler normalization (for clustering)
- Save processed data

### Phase 3 & 4: Pattern Identification and Statistical Validation
**File:** `2clustering_analysis.ipynb`
- **K-Means clustering (k=3)** as an exploratory technique to identify behavioral patterns
- Comparative analysis (Hierarchical, DBSCAN, GMM) for understanding
- Cluster profiling and characterization
- **ANOVA validation** (Mood and Focus vs Clusters)
- Post-hoc tests (if ANOVA is significant)
- Statistical interpretation of patterns

### Phase 5: Hypothesis Testing
**File:** `3hypothesis_testing.ipynb`
- **Recovery vs. Inertia**: Do rest profiles precede deep work or low performance? (Chi-square test)
- **Busy vs. Productive**: Can data analysis distinguish busywork from flow state? (Correlation analysis)
- **Weekend Bleed**: Do work/study profiles intrude into weekends and affect mood? (Crosstabulation, chi-square)

## Setup

1. Create conda environment:
```bash
conda create --name quantified_env python=3.9
conda activate quantified_env
```

2. Install dependencies:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy jupyter statsmodels
```

3. Run notebooks in order:
   - `1data_cleaning.ipynb` → `2clustering_analysis.ipynb` → `3hypothesis_testing.ipynb`

## Data

- **Raw Data:** `data/Data Science Dataset - DATABASE.csv`
- **Processed Data:** Generated in `data/cleaned_data.csv` and `data/scaled_features.csv`
- **Results:** Saved in `data/` directory after each phase

## Key Features Analyzed

**Inputs:**
- Sleep_Hours
- Music_Time_Hours
- Travel Time (Hours)

**Behaviors:**
- Work_Hours
- Study_Hours
- Chore_Time_Mins
- Distraction_Time_Mins
- Tasks_Completed

**Targets (Outcomes):**
- Mood_Rating (1-5)
- Focus_Rating (1-5)

## Statistical Methods Used

- **Descriptive Statistics**: Mean, median, standard deviation, range
- **Exploratory Data Analysis**: Histograms, box plots, scatter plots, correlation matrices
- **Clustering**: K-Means (as pattern discovery tool)
- **ANOVA**: One-way ANOVA to test differences across clusters
- **Chi-square Tests**: For categorical relationships
- **Correlation Analysis**: To examine variable relationships

## Author

Brando Allen A. Donato  
Date: February 11, 2026
