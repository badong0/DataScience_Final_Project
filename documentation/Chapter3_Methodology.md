# Chapter 3: Methodology

## A. Participants

This study employed a single-subject case study design (n=1). The participant was a working student residing in Metro Manila, Philippines, enrolled in a data science program at the time of data collection. The participant was responsible for managing both professional work obligations and academic coursework simultaneously, making this demographic representative of the target population of interest—working students who must balance multiple competing demands on their time and energy.

**Participant Characteristics:**
- **Location**: Metro Manila, Philippines
- **Status**: Working student (simultaneously employed and enrolled in academic program)
- **Academic Program**: Data Science
- **Data Collection Period**: November 19, 2025 to February 7, 2026 (81 days)

The single-subject design was chosen to enable deep, longitudinal analysis of individual behavioral patterns, consistent with the Quantified Self movement's emphasis on personal data exploration and self-knowledge through rigorous self-tracking.

---

## B. Data Collection Methods

### B.1 Data Collection Protocol

Data was collected using a structured, manual logging system implemented in Google Sheets. The participant recorded daily activities and metrics at the end of each day, ensuring contemporaneous recording to minimize recall bias. The data collection period spanned 81 consecutive days from November 19, 2025 to February 7, 2026.

**Collection Frequency**: Daily logging at the end of each day  
**Collection Tool**: Google Sheets (manual data entry)  
**Total Observations**: 81 days  
**Date Range**: November 19, 2025 to February 7, 2026

### B.2 Variables Collected

The following variables were systematically recorded for each day:

#### **Temporal Variables**
- **Date**: Calendar date of the observation (MM-DD-YY format)
- **Day of the Week**: Day name (Monday through Sunday)

#### **Sleep and Rest Variables**
- **Sleep_Hours**: Duration of sleep obtained the previous night, measured in hours (continuous, range: 0-12 hours)

#### **Productivity Variables**
- **Work_Hours**: Estimated duration of professional work activities, measured in hours (continuous, range: 0-10 hours)
- **Study_Hours**: Estimated duration of academic study activities, measured in hours (continuous, range: 0-11.73 hours)
- **Tasks_Completed**: Count of discrete tasks accomplished during the day (discrete, range: 0-10)

#### **Time Allocation Variables**
- **Chore_Time_Mins**: Time spent on household tasks and chores, measured in minutes (continuous, range: 0-500 minutes)
- **Distraction_Time_Mins**: Estimated time spent on non-productive digital activities including social media, games, and entertainment, measured in minutes (continuous, range: 0-500 minutes)
- **Travel Time (Hours)**: Duration of commute between locations, measured in hours (continuous, range: 0-3 hours)
- **Music_Time_Hours**: Time spent listening to music, measured in hours (continuous)

#### **Transportation Variables**
- **Mode of Transport**: Primary transportation method(s) used during the day (categorical: Public Transport, Motorcycle, or combinations thereof)

#### **Music Preference Variables**
- **Main_Music_Genre**: Primary music genre(s) listened to during the day (categorical: Rock, OPM, Podcast, Jazz, Lofi, Classical, News, Pop, Oldies, R&B, or combinations)

#### **Subjective Well-being Variables**
- **Mood_Rating**: Self-reported mood rating on a scale of 1 to 5, where 1 = very poor, 2 = poor, 3 = neutral, 4 = good, 5 = excellent (ordinal, range: 1-5)
- **Focus_Rating**: Self-reported focus/concentration rating on a scale of 1 to 5, where 1 = very poor, 2 = poor, 3 = neutral, 4 = good, 5 = excellent (ordinal, range: 1-5)

#### **Additional Variables**
- **Notes**: Optional free-text field for qualitative observations or contextual information

**Scope of primary analysis (aligned with paper).** The primary statistical analysis (descriptive statistics, correlation matrix, weekday vs. weekend t-tests, and the three behavioral hypotheses) uses the variables listed in the paper's Table 1: Sleep_Hours, Work_Hours, Study_Hours, Distraction_Time_Mins, Travel Time (Hours), Tasks_Completed, Mood_Rating, Focus_Rating, and Is_Weekend. Variables **Music_Time_Hours**, **Main_Music_Genre**, **Chore_Time_Mins**, and **Mode of Transport** were collected and preprocessed (including one-hot encoding for categoricals) but are not included in the primary hypothesis testing or correlation results reported in the paper; they remain available for exploratory or future analysis.

### B.3 Data Collection Quality Assurance

To ensure data quality and consistency:
- **Contemporaneous Recording**: All entries were made at the end of each day to minimize recall bias
- **Structured Format**: Google Sheets template ensured consistent variable names and formats
- **Completeness Check**: Daily logging was maintained throughout the entire 81-day period
- **Validation**: Date column was validated against computed day of the week to ensure accuracy

---

## C. Operational Definitions

This section provides precise definitions of all variables and derived constructs used in the analysis.

### C.1 Primary Variables

#### **Sleep_Hours**
- **Definition**: The total duration of sleep obtained during the previous night, measured in hours
- **Measurement**: Self-reported estimate rounded to the nearest 0.5 hours
- **Range**: 0-12 hours
- **Interpretation**: 0 indicates no sleep recorded; values represent continuous hours of sleep

#### **Work_Hours**
- **Definition**: The total duration of time spent engaged in professional work activities, measured in hours
- **Measurement**: Self-reported estimate of time dedicated to work-related tasks
- **Range**: 0-10 hours
- **Interpretation**: Includes time spent on work tasks, meetings, and work-related communications; excludes breaks and non-work activities

#### **Study_Hours**
- **Definition**: The total duration of time spent engaged in academic study activities, measured in hours
- **Measurement**: Self-reported estimate of time dedicated to studying, coursework, and academic tasks
- **Range**: 0-11.73 hours
- **Interpretation**: Includes time spent reading, writing assignments, completing coursework, and attending classes; excludes breaks

#### **Chore_Time_Mins**
- **Definition**: The total duration of time spent on household tasks and chores, measured in minutes
- **Measurement**: Self-reported estimate of time dedicated to domestic activities
- **Range**: 0-500 minutes
- **Interpretation**: Includes cleaning, cooking, shopping, and other household maintenance activities

#### **Distraction_Time_Mins**
- **Definition**: The total duration of time spent on non-productive digital activities, measured in minutes
- **Measurement**: Self-reported estimate of time spent on social media, games, entertainment, and other non-productive digital consumption
- **Range**: 0-500 minutes
- **Interpretation**: Represents time spent on activities that do not contribute to work, study, or rest goals; serves as a proxy for digital distraction

#### **Travel Time (Hours)**
- **Definition**: The total duration of time spent commuting between locations, measured in hours
- **Measurement**: Self-reported estimate of total commute time
- **Range**: 0-3 hours
- **Interpretation**: Includes all time spent traveling between home, work, school, and other locations; reflects Metro Manila traffic conditions

#### **Tasks_Completed**
- **Definition**: The count of discrete tasks accomplished during the day
- **Measurement**: Self-reported count of completed tasks
- **Range**: 0-10
- **Interpretation**: Discrete count of tasks finished; serves as a productivity metric independent of time spent

#### **Mood_Rating**
- **Definition**: Self-reported subjective assessment of overall mood on a 5-point ordinal scale
- **Measurement**: Single rating at end of day
- **Scale**: 
  - 1 = Very Poor
  - 2 = Poor
  - 3 = Neutral
  - 4 = Good
  - 5 = Excellent
- **Range**: 1-5
- **Interpretation**: Higher values indicate more positive mood; represents overall emotional state

#### **Focus_Rating**
- **Definition**: Self-reported subjective assessment of focus/concentration ability on a 5-point ordinal scale
- **Measurement**: Single rating at end of day
- **Scale**:
  - 1 = Very Poor (highly distracted, unable to concentrate)
  - 2 = Poor (frequently distracted, low concentration)
  - 3 = Neutral (moderate focus, some distractions)
  - 4 = Good (good focus, minimal distractions)
  - 5 = Excellent (high focus, minimal to no distractions)
- **Range**: 1-5
- **Interpretation**: Higher values indicate better ability to maintain focus and concentration

#### **Music_Time_Hours**
- **Definition**: The total duration of time spent listening to music, measured in hours
- **Measurement**: Self-reported estimate
- **Range**: 0-12 hours
- **Interpretation**: Includes all music listening time regardless of context (during work, study, commute, etc.)

#### **Mode of Transport**
- **Definition**: Primary transportation method(s) used during the day
- **Measurement**: Categorical selection from available options
- **Categories**: 
  - Public Transport (jeepney, bus, train, etc.)
  - Motorcycle
  - Combinations (e.g., "Public Transport, Motorcycle")
- **Interpretation**: May include multiple modes if different transportation was used for different trips

#### **Main_Music_Genre**
- **Definition**: Primary music genre(s) listened to during the day
- **Measurement**: Categorical selection from available genres
- **Categories**: Rock, OPM (Original Pilipino Music), Podcast, Jazz, Lofi, Classical, News, Pop, Oldies, R&B
- **Interpretation**: May include multiple genres if different music was listened to at different times

### C.2 Derived Variables

#### **Is_Weekend**
- **Definition**: Binary indicator variable identifying whether the observation date falls on a weekend
- **Computation**: Derived from Date variable using Python datetime: `Is_Weekend = True if dayofweek in [5, 6] else False`
- **Values**: 
  - `True` = Saturday or Sunday
  - `False` = Monday through Friday
- **Purpose**: Enables weekend vs. weekday comparisons for behavioral patterns

#### **Work_Study_Profile**
- **Definition**: Binary indicator identifying days with high combined work and study hours
- **Computation**: `Work_Study_Profile = True if (Work_Hours + Study_Hours) >= median(Work_Hours + Study_Hours) else False`
- **Purpose**: Used in hypothesis testing to identify work/study-intensive days

#### **Productivity_Type**
- **Definition**: Categorical variable classifying high-volume days as either "Busywork" or "Flow State"
- **Computation**: 
  - High-volume days: `(Work_Hours + Study_Hours) >= median(Work_Hours + Study_Hours)`
  - Busywork: High-volume AND `Focus_Rating < median(Focus_Rating)`
  - Flow State: High-volume AND `Focus_Rating >= median(Focus_Rating)`
- **Categories**: 
  - "Busywork (High Volume, Low Focus)"
  - "Flow State (High Volume, High Focus)"
  - Other (low-volume days)
- **Purpose**: Enables distinction between high-volume days with low vs. high focus

#### **Rest Day**
- **Definition**: Binary indicator identifying days with low work/study and high distraction
- **Computation**: 
  - `Rest Day = True if Work_Hours < median(Work_Hours) AND Study_Hours < median(Study_Hours) AND Distraction_Time_Mins > median(Distraction_Time_Mins) else False`
- **Rationale**: Uses separate medians for Work_Hours and Study_Hours so that a day must have both below their respective medians (minimal productive activity) and distraction above the median (high leisure engagement). This matches the operational definition used in the paper and in the hypothesis-testing code.
- **Purpose**: Used in Recovery vs. Inertia hypothesis testing

#### **Deep Work Day**
- **Definition**: Binary indicator identifying days with high work/study and low distraction
- **Computation**: 
  - `Deep Work Day = True if (Work_Hours + Study_Hours) >= median(Work_Hours + Study_Hours) AND Distraction_Time_Mins < median(Distraction_Time_Mins) else False`
- **Purpose**: Used in Recovery vs. Inertia hypothesis testing

### C.3 Construct Definitions

#### **Productivity**
- **Definition**: A multidimensional construct representing output and accomplishment
- **Operationalization**: Measured through three indicators:
  1. **Work_Hours**: Time invested in professional work
  2. **Study_Hours**: Time invested in academic activities
  3. **Tasks_Completed**: Discrete count of completed tasks
- **Interpretation**: Higher values across these indicators suggest higher productivity

#### **Mood**
- **Definition**: Subjective emotional state and overall psychological well-being
- **Operationalization**: Measured through **Mood_Rating** (1-5 scale)
- **Interpretation**: Higher ratings indicate more positive mood and better psychological well-being

#### **Focus**
- **Definition**: Ability to maintain attention and concentration on tasks
- **Operationalization**: Measured through **Focus_Rating** (1-5 scale)
- **Interpretation**: Higher ratings indicate better ability to concentrate and resist distractions

#### **Distraction**
- **Definition**: Time spent on non-productive digital activities that compete with work and study goals
- **Operationalization**: Measured through **Distraction_Time_Mins**
- **Interpretation**: Higher values indicate more time spent on non-productive activities; inversely related to focus and productivity

#### **Travel Time**
- **Definition**: Time spent commuting between locations
- **Operationalization**: Measured through **Travel Time (Hours)**
- **Interpretation**: Reflects Metro Manila traffic conditions and transportation efficiency; represents time cost of mobility

---

## D. Data Cleaning and Preprocessing

### D.1 Data Loading and Initial Inspection

The raw dataset was loaded from Google Sheets export (CSV format) into Python using the Pandas library. Initial inspection revealed:
- **Total Observations**: 81 days
- **Total Variables**: 15 original variables
- **Date Range**: November 19, 2025 to February 7, 2026
- **Data Format**: Mixed (numeric, categorical, date, text)

### D.2 Missing Value Handling

#### **Missing Dates**
- **Procedure**: Rows with missing or invalid date values were completely removed from the dataset
- **Rationale**: Date is essential for temporal analysis and cannot be imputed
- **Result**: No rows were removed (all 81 observations had valid dates)

#### **Missing Numeric Values**
- **Procedure**: Missing numeric values were imputed with 0
- **Rationale**: 
  - Missing values likely indicate zero activity (e.g., 0 work hours on a rest day)
  - Zero imputation allows mathematical operations while preserving the meaning of absence
  - This approach is conservative and avoids introducing artificial values
- **Variables Affected**: Sleep_Hours, Work_Hours, Study_Hours, Chore_Time_Mins, Distraction_Time_Mins, Travel Time, Music_Time_Hours, Tasks_Completed, Mood_Rating, Focus_Rating
- **Result**: All numeric variables have complete data after imputation

#### **Missing Categorical Values**
- **Procedure**: Missing values in categorical variables (Mode of Transport, Main_Music_Genre) were filled with empty strings ("")
- **Rationale**: Preserves the structure for one-hot encoding while indicating absence of the category
- **Result**: Categorical variables processed without data loss

### D.3 Data Type Conversion

#### **Date Parsing**
- **Procedure**: Date column was parsed from string format (MM-DD-YY) to Python datetime format
- **Method**: `pd.to_datetime()` with format specification
- **Validation**: Computed day of the week from parsed date and compared against recorded "Day of the Week" column to ensure accuracy
- **Result**: All dates successfully parsed; day-of-week validation confirmed accuracy

#### **Categorical Encoding**
- **Procedure**: Categorical variables were converted to numerical format using one-hot encoding
- **Variables Encoded**:
  - **Mode of Transport**: Split comma-separated values and created binary columns (Transport_Public_Transport, Transport_Motorcycle)
  - **Main_Music_Genre**: Split comma-separated values and created binary columns for each genre (Genre_Rock, Genre_OPM, Genre_Podcast, Genre_Jazz, Genre_Lofi, Genre_Classical, Genre_News, Genre_Pop, Genre_Oldies, Genre_RandB)
- **Method**: Custom Python function to split comma-separated values and create binary (0/1) indicator columns
- **Result**: All categorical variables converted to numerical format suitable for statistical analysis

### D.4 Outlier Detection and Handling

#### **Outlier Identification**
- **Method**: Visual inspection using box plots and histograms for all numerical variables
- **Tools**: Matplotlib and Seaborn visualization libraries
- **Variables Inspected**: All numerical variables (Sleep_Hours, Work_Hours, Study_Hours, Travel Time, Distraction_Time_Mins, Tasks_Completed, Mood_Rating, Focus_Rating)

#### **Outlier Treatment**
- **Decision**: All identified outliers were retained in the dataset
- **Rationale**: 
  - Outliers represent genuine behavioral variations (e.g., exceptionally long work days, zero-sleep nights)
  - Removing outliers would eliminate important information about extreme but real patterns
  - The single-subject design benefits from capturing the full range of behavioral variation
- **Result**: Complete dataset preserved with all 81 observations

### D.5 Feature Engineering

#### **Derived Temporal Variables**
- **Is_Weekend**: Binary indicator derived from Date using `df['Date'].dt.dayofweek.isin([5, 6])`
  - Saturday = 5, Sunday = 6
  - Enables weekend vs. weekday comparisons

#### **Feature Scaling**
- **Procedure**: Numerical features selected for clustering analysis were standardized using StandardScaler (Z-score normalization)
- **Method**: `sklearn.preprocessing.StandardScaler`
- **Formula**: `z = (x - μ) / σ` where μ is mean and σ is standard deviation
- **Variables Scaled**: Sleep_Hours, Music_Time_Hours, Travel Time (Hours), Work_Hours, Study_Hours, Chore_Time_Mins, Distraction_Time_Mins, Tasks_Completed
- **Purpose**: Ensures all features contribute equally to distance-based analyses (e.g., clustering)
- **Result**: Scaled features saved to `data/scaled_features.csv` for clustering analysis

### D.6 Data Quality Validation

#### **Completeness Check**
- **Result**: All 81 days have complete data after imputation
- **Missing Data Rate**: 0% (after imputation)

#### **Date Validation**
- **Procedure**: Computed day of week from parsed date and compared with recorded "Day of the Week"
- **Result**: All dates validated successfully; no mismatches detected

#### **Range Validation**
- **Procedure**: Checked all numerical variables against expected ranges
- **Results**:
  - Sleep_Hours: 0-12 hours ✓
  - Work_Hours: 0-10 hours ✓
  - Study_Hours: 0-11.73 hours ✓
  - Mood_Rating: 1-5 ✓
  - Focus_Rating: 1-5 ✓
  - All variables within expected ranges

### D.7 Final Dataset Structure

After cleaning and preprocessing:
- **Total Observations**: 81 days
- **Total Variables**: 30 variables (15 original + 15 derived/encoded)
- **Numerical Variables**: 8 primary + 8 scaled versions
- **Categorical Variables**: 2 original (encoded into 12 binary columns)
- **Temporal Variables**: Date, Day of the Week, Is_Weekend
- **Output Files**: 
  - `data/cleaned_data.csv` (main cleaned dataset)
  - `data/scaled_features.csv` (scaled features for clustering)
  - `data/descriptive_statistics.csv` (summary statistics)

---

## E. Statistical Analysis Methods

### E.1 Descriptive Statistics

Descriptive statistics were calculated for all numerical variables to characterize the dataset's central tendencies, variability, and distributions.

#### **Measures Computed**
- **Mean**: Arithmetic average of values
- **Median**: 50th percentile (middle value)
- **Standard Deviation**: Measure of variability around the mean
- **Minimum**: Smallest observed value
- **Maximum**: Largest observed value
- **Range**: Difference between maximum and minimum
- **Quartiles**: 25th percentile (Q1), 50th percentile (median), 75th percentile (Q3)

#### **Variables Analyzed**
All numerical variables: Sleep_Hours, Work_Hours, Study_Hours, Travel Time (Hours), Distraction_Time_Mins, Tasks_Completed, Mood_Rating, Focus_Rating

#### **Output**
Descriptive statistics table saved to `data/descriptive_statistics.csv` for inclusion in the paper.

### E.2 Exploratory Data Analysis (EDA)

#### **E.2.1 Distribution Analysis**

**Histograms**
- **Purpose**: Visualize the distribution shape of each numerical variable
- **Method**: Created histograms for all 8 numerical variables
- **Parameters**: 
  - Figure size: 2000×1000 pixels
  - DPI: 300 (publication quality)
  - Overlaid with mean and median lines
- **Output**: `figures/Figure_1_Histograms_All_Variables.png`
- **Interpretation**: Identifies distribution shapes (normal, skewed, bimodal), central tendencies, and potential outliers

**Box Plots**
- **Purpose**: Visualize distributions, identify outliers, and compare spread across variables
- **Method**: Created box plots for all numerical variables
- **Parameters**: Standard box plot showing quartiles, median, and outliers
- **Output**: `figures/Figure_4_Box_Plots_Distributions.png`
- **Interpretation**: Shows median, quartiles, range, and identifies potential outliers beyond 1.5×IQR

#### **E.2.2 Time Series Analysis**

**Daily Trends**
- **Purpose**: Identify temporal patterns and trends over the 81-day period
- **Method**: Line plots of key variables over time
- **Variables Visualized**: Work_Hours, Study_Hours, Mood_Rating, Focus_Rating
- **Output**: `figures/Figure_2_Time_Series_Trends.png`
- **Interpretation**: Reveals daily fluctuations, trends, cycles, and temporal relationships

**Weekly Averages**
- **Purpose**: Identify weekly patterns and differences between weekend and weekday behavior
- **Method**: Calculated weekly averages and plotted trends
- **Variables Analyzed**: Work_Hours, Study_Hours, Mood_Rating, Focus_Rating
- **Output**: `figures/Figure_5_Weekly_Trends.png`
- **Interpretation**: Reveals weekly cycles and weekend vs. weekday differences

#### **E.2.3 Correlation Analysis**

**Correlation Matrix**
- **Purpose**: Identify relationships between numerical variables
- **Method**: Pearson correlation coefficient (r) calculated for all pairs of numerical variables
- **Visualization**: Correlation heatmap with color coding
- **Parameters**: 
  - Upper triangle masked for clarity
  - Color scale: Red (negative) to Blue (positive)
  - Values annotated on heatmap
- **Output**: `figures/Figure_3_Correlation_Matrix.png` and `figures/Figure_6_Correlation_Matrix_Statistical.png`
- **Interpretation**: Identifies strong (|r| > 0.7), moderate (0.4 < |r| < 0.7), and weak (|r| < 0.4) correlations

**Correlation Significance Testing**
- **Purpose**: Determine statistical significance of observed correlations
- **Method**: Pearson correlation with p-value calculation using `scipy.stats.pearsonr()`
- **Significance Level**: α = 0.05
- **Interpretation**: p < 0.05 indicates statistically significant correlation
- **Output**: Significant correlations (p < 0.05) identified and reported

### E.3 Statistical Tests

#### **E.3.1 Independent Samples t-Tests**

**Purpose**: Compare means between two independent groups (weekend vs. weekday)

**Variables Tested**:
1. **Work_Hours**: Weekend vs. Weekday
2. **Study_Hours**: Weekend vs. Weekday
3. **Mood_Rating**: Weekend vs. Weekday
4. **Sleep_Hours**: Weekend vs. Weekday
5. **Focus_Rating**: Weekend vs. Weekday

**Method**: 
- Two-sample t-test assuming unequal variances (Welch's t-test)
- Implemented using `scipy.stats.ttest_ind()`
- Null hypothesis (H₀): μ_weekend = μ_weekday
- Alternative hypothesis (H₁): μ_weekend ≠ μ_weekday

**Output Reported**:
- Mean and standard deviation for each group
- Sample sizes (n) for each group
- t-statistic
- p-value
- Significance decision (α = 0.05)

**Interpretation**: p < 0.05 indicates significant difference between weekend and weekday means

#### **E.3.2 Chi-Square Tests of Independence**

**Purpose**: Test associations between categorical variables

**Tests Performed**:
1. **Work/Study Profile × Is_Weekend**: Tests whether work/study patterns differ between weekends and weekdays
2. **Weekend × High Volume**: Tests association between weekend status and high-volume days

**Method**:
- Chi-square test of independence using `scipy.stats.chi2_contingency()`
- Null hypothesis (H₀): Variables are independent
- Alternative hypothesis (H₁): Variables are associated

**Output Reported**:
- Contingency table (observed frequencies)
- Chi-square statistic (χ²)
- Degrees of freedom (df)
- p-value
- Significance decision (α = 0.05)

**Interpretation**: p < 0.05 indicates significant association between categorical variables

#### **E.3.3 Correlation Significance Tests**

**Purpose**: Determine statistical significance of Pearson correlations

**Method**:
- Pearson correlation coefficient (r) with p-value
- Implemented using `scipy.stats.pearsonr()`
- Null hypothesis (H₀): ρ = 0 (no correlation)
- Alternative hypothesis (H₁): ρ ≠ 0 (correlation exists)

**Significance Level**: α = 0.05

**Output**: 
- Correlation coefficient (r)
- p-value
- Significant correlations (p < 0.05) identified and reported

### E.4 Hypothesis Testing

#### **E.4.1 Hypothesis 5.1: Recovery vs. Inertia**

**Research Question**: Do "Rest Days" (low work/study, high distraction) typically precede "Deep Work Days" (high work/study, low distraction), or do they precede further low-performance patterns (suggesting inertia)?

**Operational Definitions**:
- **Rest Day**: `Work_Hours < median(Work_Hours) AND Study_Hours < median(Study_Hours) AND Distraction_Time_Mins > median(Distraction_Time_Mins)`
- **Deep Work Day**: `(Work_Hours + Study_Hours) >= median(Work_Hours + Study_Hours) AND Distraction_Time_Mins < median(Distraction_Time_Mins)`
- **Low Performance Day**: Days that are neither Rest Days nor Deep Work Days

**Method**:
1. Identify all Rest Days in the dataset
2. For each Rest Day, examine the next day's classification
3. Classify transitions as:
   - Rest → Deep Work (recovery pattern)
   - Rest → Low Performance (inertia pattern)
   - Rest → Other (mixed transitions)
4. Calculate proportions of each transition type
5. Compare proportions to determine dominant pattern

**Statistical Analysis**: 
- Transition frequency counts
- Proportion calculations
- Visual analysis of transition patterns

**Output**: Transition analysis results saved to `data/recovery_inertia_transitions.csv`

#### **E.4.2 Hypothesis 5.2: Busy vs. Productive Distinction**

**Research Question**: Can data analysis distinguish between "High-Volume / Low-Focus" days (Busywork) and "High-Volume / High-Focus" days (Flow State) based on the relationship between Work_Hours and Distraction_Time?

**Operational Definitions**:
- **High-Volume Day**: `(Work_Hours + Study_Hours) >= median(Work_Hours + Study_Hours)`
- **Busywork**: High-volume AND `Focus_Rating < median(Focus_Rating)`
- **Flow State**: High-volume AND `Focus_Rating >= median(Focus_Rating)`

**Method**:
1. Identify all high-volume days
2. Classify each as Busywork or Flow State based on Focus_Rating threshold
3. Compare Focus_Rating means between Busywork and Flow State groups
4. Perform independent samples t-test

**Statistical Test**: Independent samples t-test comparing Focus_Rating between Busywork and Flow State groups
- Null hypothesis (H₀): μ_busywork = μ_flow_state
- Alternative hypothesis (H₁): μ_busywork ≠ μ_flow_state
- Significance level: α = 0.05

**Output**: 
- Mean Focus_Rating for each group
- t-statistic and p-value
- Significance decision

#### **E.4.3 Hypothesis 5.3: Weekend Bleed Effect**

**Research Question**: Do specific habit patterns strictly align with calendar weekends, or do "Work/Study" patterns significantly intrude into weekends, and is this intrusion associated with "Low Mood" outcomes?

**Operational Definitions**:
- **Work/Study Profile**: `(Work_Hours + Study_Hours) >= median(Work_Hours + Study_Hours)`
- **Weekend Bleed**: Work/Study Profile occurring on weekend days (Saturday or Sunday)
- **Low Mood**: `Mood_Rating < median(Mood_Rating)`

**Method**:
1. Create Work/Study Profile binary indicator
2. Cross-tabulate Work/Study Profile × Is_Weekend
3. Calculate proportion of weekend days with Work/Study profiles
4. Compare mood ratings between:
   - Weekend Bleed (Weekend + Work/Study Profile)
   - Weekend Rest (Weekend + No Work/Study Profile)
5. Perform chi-square test of independence

**Statistical Test**: Chi-square test of independence (Work/Study Profile × Is_Weekend)
- Null hypothesis (H₀): Work/Study Profile and Weekend status are independent
- Alternative hypothesis (H₁): Work/Study Profile and Weekend status are associated
- Significance level: α = 0.05

**Output**:
- Crosstabulation table
- Chi-square statistic, degrees of freedom, p-value
- Mood comparisons between groups
- Significance decision

### E.5 Visualization Tools and Software

**Software**: Python 3.9 with the following libraries:
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib**: Basic plotting and visualization
- **Seaborn**: Statistical visualization and heatmaps
- **SciPy**: Statistical tests (ttest_ind, chi2_contingency, pearsonr)
- **scikit-learn**: Feature scaling (StandardScaler)

**Figure Specifications**:
- **Resolution**: 300 DPI (publication quality)
- **Format**: PNG
- **Size**: Optimized for IEEE paper format (typically 12×6 or 14×8 inches)
- **Style**: Whitegrid style for clarity
- **Output Directory**: `figures/` folder

**Statistical Software**: All analyses performed using Python with scipy.stats and pandas libraries, ensuring reproducibility and transparency.

---

## Summary

This methodology section provides a comprehensive framework for understanding how data was collected, cleaned, and analyzed. The single-subject design enables deep longitudinal analysis of behavioral patterns, while the rigorous statistical methods ensure valid and reliable conclusions. All procedures are documented to enable replication and transparency, consistent with best practices in data science research.
