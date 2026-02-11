# The Work-Study-Life Profile: A Quantified Self Analysis

A data science project analyzing daily habits of a working student using unsupervised learning (K-Means clustering) and statistical validation to identify distinct behavioral profiles.

## Project Overview

This study explores the concept of the "Quantified Self" by analyzing daily habits over a 74-day period. The project employs K-Means Clustering to identify distinct "Daily Profiles" and uses ANOVA to validate these clusters against mood and focus ratings.

## Project Structure

The project is organized into separate notebooks for different phases:

### Phase 1 & 2: Data Cleaning and Preprocessing
**File:** `data_cleaning.ipynb`
- Load and inspect raw data
- Handle missing values
- Parse and validate dates
- Feature selection for clustering
- StandardScaler normalization
- Save processed data

### Phase 3 & 4: Clustering Analysis and Statistical Validation
**File:** `clustering_analysis.ipynb`
- K-Means clustering (k=3)
- Comparative analysis (Hierarchical, DBSCAN, GMM)
- Cluster profiling and visualization
- ANOVA validation (Mood and Focus vs Clusters)
- Post-hoc tests

### Phase 5: Hypothesis Testing
**File:** `hypothesis_testing.ipynb`
- **Recovery vs. Inertia**: Do rest profiles precede deep work or low performance?
- **Busy vs. Productive**: Can clustering distinguish busywork from flow state?
- **Weekend Bleed**: Do work/study profiles intrude into weekends and affect mood?

### Phase 6.2: Predictive Modeling (Future Work)
**File:** `predictive_model.ipynb`
- Random Forest model to predict Focus_Rating
- Feature importance analysis
- Productivity forecast based on daily inputs

## Setup

1. Create conda environment:
```bash
conda create --name quantified_env python=3.9
conda activate quantified_env
```

2. Install dependencies:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy jupyter
```

3. Run notebooks in order:
   - `data_cleaning.ipynb` → `clustering_analysis.ipynb` → `hypothesis_testing.ipynb` → `predictive_model.ipynb`

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

**Targets:**
- Mood_Rating (1-5)
- Focus_Rating (1-5)

## Expected Clusters

Based on methodology:
1. **Cluster 0: "The Commuter Grind"** - High travel time, moderate work, low study
2. **Cluster 1: "The Deep Work / WFH Day"** - Zero/low travel, high work and study
3. **Cluster 2: "The Distracted Recovery"** - High distraction, high sleep, low tasks

## Author

Brando Allen A. Donato  
Date: February 6, 2026
