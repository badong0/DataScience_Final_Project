---
name: Work-Study-Life Profile Plan
overview: A step-by-step plan to execute the Quantified Self / Work-Study-Life Profile project from project-description.md, covering data cleaning, preprocessing, K-Means clustering with comparative analysis (Hierarchical, DBSCAN, GMM), ANOVA validation, hypothesis testing, and optional predictive modeling.
todos: []
isProject: false
---

# Work-Study-Life Profile: Step-by-Step Execution Plan

## Phase 1: Environment and Data Setup

### Step 1.1: Environment Setup

- Create conda environment via [conda.txt](conda.txt): `conda create --name quantified_env python=3.9`
- Install dependencies: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `scipy`, `jupyter`

### Step 1.2: Load and Inspect Data

- Load [data/Data Science Dataset - DATABASE.csv](data/Data Science Dataset - DATABASE.csv) in Jupyter
- Inspect: `df.info()`, `df.describe()`, `df.isnull().sum()` to understand structure, ranges, and missingness
- Note: Dataset has 74 rows with columns: Date, Day of the Week, Sleep_Hours, Work_Hours, Study_Hours, Chore_Time_Mins, Distraction_Time_Mins, Travel Time (Hours), Mode of Transport, Music_Time_Hours, Main_Music_Genre, Tasks_Completed, Mood_Rating, Focus_Rating, Notes

---

## Phase 2: Data Cleaning and Preprocessing

### Step 2.1: Handle Missing Values

- Drop rows with missing dates (per methodology)
- Impute missing numeric values with 0 (per methodology)
- Optionally: flag and log imputed values for transparency

### Step 2.2: Parse and Validate Dates

- Parse `Date` column to datetime
- Validate `Day of the Week` against computed weekday from `Date` (some entries may be misaligned)
- Add a derived `Is_Weekend` column (Saturday/Sunday) for the "Weekend Bleed" hypothesis

### Step 2.3: Handle Categorical Variables

- **Mode of Transport** and **Main_Music_Genre** are multi-valued strings; decide:
  - Option A: One-hot encode for clustering (if these are input features)
  - Option B: Exclude from clustering, use only for exploratory analysis
- Per methodology, clustering uses: Sleep_Hours, Travel Time, Work_Hours, Study_Hours, behaviors (Chore_Time_Mins, Distraction_Time_Mins, Tasks_Completed)

### Step 2.4: Feature Selection for Clustering

- **Inputs:** Sleep_Hours, Music_Time_Hours, Travel Time (Hours)
- **Behaviors:** Work_Hours, Study_Hours, Chore_Time_Mins, Distraction_Time_Mins, Tasks_Completed
- **Targets (excluded from clustering):** Mood_Rating, Focus_Rating
- Exclude Date, Day of the Week, Mode of Transport, Main_Music_Genre, Notes from clustering (unless one-hot encoded)

### Step 2.5: Scaling

- Apply `StandardScaler` (Z-score normalization) to clustering features
- Store scaler for later use (e.g., inverse transform for interpretability)

---

## Phase 3: K-Means Clustering

### Step 3.1: Elbow Method / Silhouette Analysis

- Use Elbow Method and/or Silhouette Score to choose k (methodology suggests k=3)
- Compare k=2,3,4,5 to validate k=3 or refine

### Step 3.2: Fit K-Means (k=3)

- Fit K-Means on scaled features
- Assign cluster labels to each day

### Step 3.3: Cluster Profiling

- Compute mean and std of each feature per cluster
- Name clusters based on characteristics (per methodology):
  - **Cluster 0:** "The Commuter Grind" (high Travel Time, moderate Work, low Study)
  - **Cluster 1:** "The Deep Work / WFH Day" (zero/low Travel, high Work, high Study)
  - **Cluster 2:** "The Distracted Recovery" (high Distraction, high Sleep, low Tasks_Completed)

### Step 3.4: Visualizations

- PCA (2D) or t-SNE scatter plot colored by cluster
- Box plots of key features by cluster
- Heatmap of cluster centroids (scaled back if possible for interpretability)

### Step 3.5: Comparative Clustering Analysis

Run alternative algorithms on the same scaled features and compare:

- **K-Means:** Fast, interpretable centroids; assumes spherical clusters, needs k (primary method)
- **Hierarchical (Agglomerative):** No k needed upfront, dendrogram for structure; slower, cut height choice (use Ward linkage)
- **DBSCAN:** Handles outliers, arbitrary shapes; needs eps/min_samples tuning (may label many as noise)
- **Gaussian Mixture (GMM):** Soft assignments, elliptical clusters; more complex, less interpretable (good for overlap)

**Comparison framework:**

- Fix k=3 for K-Means, Hierarchical, GMM to ensure fair comparison
- For DBSCAN: tune eps and min_samples to get ~3 clusters, or report noise proportion
- Compute internal metrics: Silhouette Score, Calinski-Harabasz Index
- Run ANOVA (Mood, Focus) for each method's labels; compare F-statistics and p-values
- Build a comparison table: Algorithm | Silhouette | CH Index | ANOVA Mood p-value | ANOVA Focus p-value
- Visualize: side-by-side PCA/t-SNE plots colored by each algorithm's labels
- Discuss which method best separates behavioral profiles and why

---

## Phase 4: Statistical Validation (ANOVA)

### Step 4.1: Mood vs. Cluster

- One-way ANOVA: `Mood_Rating` by cluster label
- Report F-statistic and p-value
- Interpret: p < 0.05 indicates cluster type significantly affects mood

### Step 4.2: Focus vs. Cluster

- One-way ANOVA: `Focus_Rating` by cluster label
- Report F-statistic and p-value
- Interpret: p < 0.05 indicates cluster type significantly affects focus

### Step 4.3: Post-hoc Tests (if ANOVA significant)

- Tukey HSD or pairwise t-tests to identify which cluster pairs differ

---

## Phase 5: Hypothesis Testing

### Step 5.1: "Recovery vs. Inertia" Hypothesis

- Define "Rest Profiles" (e.g., Cluster 2) and "Deep Work" (e.g., Cluster 1)
- For each day in Rest Profile, check next day's cluster:
  - Count transitions: Rest → Deep Work vs. Rest → Low-Performance
- Use chi-square or proportion tests to assess if recovery precedes deep work more than inertia

### Step 5.2: "Busy vs. Productive" Distinction

- Compute ratio: `Work_Hours / (Distraction_Time_Mins/60)` or similar
- Check if clusters naturally separate High-Volume/Low-Focus (Busywork) from High-Volume/High-Focus (Flow State)
- Visualize: Work_Hours vs. Distraction_Time_Mins, colored by cluster and Focus_Rating

### Step 5.3: "Weekend Bleed" Effect

- Crosstab: cluster vs. `Is_Weekend`
- Check if Work/Study profiles appear on weekends
- Correlate Weekend + Work/Study intrusion with Low Mood (e.g., regression or stratified ANOVA)

---

## Phase 6: Results and Documentation

### Step 6.1: Compile Results

- Summary table of cluster characteristics
- ANOVA results table
- Hypothesis test outcomes
- Figures suitable for [documentation/CCIT-CPT-001 ACM Paper Format.docx](documentation/CCIT-CPT-001 ACM Paper Format.docx)

### Step 6.2: Optional Future Work – Predictive Modeling

- Train Random Forest to predict `Focus_Rating` from Sleep_Hours, Travel Time, Work_Hours, Study_Hours, Distraction_Time_Mins (previous/current day)
- Evaluate RMSE/MAE and feature importance
- This creates a "Productivity Forecast" as described in Future Work

---

## Suggested File Structure

```
Final Proj Work Life/
├── data/
│   └── Data Science Dataset - DATABASE.csv
├── data_cleaning.ipynb         # Phase 1–2: Load, clean, preprocess
├── clustering_analysis.ipynb   # Phase 3–4: K-Means, comparative (Hierarchical, DBSCAN, GMM), ANOVA
├── hypothesis_testing.ipynb    # Phase 5: Recovery vs. Inertia, Busy vs. Productive, Weekend Bleed
├── (optional) predictive_model.ipynb   # Phase 6.2: Random Forest
└── project-description.md
```

---

## Mermaid: High-Level Workflow

```mermaid
flowchart TD
    subgraph phase1 [Phase 1: Setup]
        A1[Environment Setup]
        A2[Load and Inspect Data]
    end

    subgraph phase2 [Phase 2: Preprocessing]
        B1[Handle Missing Values]
        B2[Parse Dates and Add Is_Weekend]
        B3[Feature Selection]
        B4[StandardScaler]
    end

    subgraph phase3 [Phase 3: Clustering]
        C1[Elbow/Silhouette for k]
        C2[Fit K-Means k=3]
        C3[Profile and Name Clusters]
        C4[Visualizations]
        C5[Comparative: Hierarchical, DBSCAN, GMM]
    end

    subgraph phase4 [Phase 4: Validation]
        D1[ANOVA Mood vs Cluster]
        D2[ANOVA Focus vs Cluster]
    end

    subgraph phase5 [Phase 5: Hypotheses]
        E1[Recovery vs Inertia]
        E2[Busy vs Productive]
        E3[Weekend Bleed]
    end

    A1 --> A2 --> B1 --> B2 --> B3 --> B4 --> C1 --> C2 --> C3 --> C4 --> C5 --> D1 --> D2 --> E1 --> E2 --> E3
```



