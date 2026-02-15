CCDATSCL Project: The Work-Study-Life Profile
Author: Brando Allen A. Donato  Date: February 11, 2026

Abstract
This study explores the concept of the "Quantified Self" by analyzing the daily habits of a working student in Metro Manila over an 81-day period (November 2025 to February 2026). Addressing the challenges of balancing professional obligations, academic requirements, and personal well-being, this research employs a disciplined, manual data collection method to record daily behavioral metrics. The study utilizes exploratory data analysis (EDA) and statistical techniques to understand and validate the dataset. Distribution analysis (histograms, box plots), time series trends, and correlation matrices are used to characterize the data. Independent samples t-tests and chi-square tests are applied to validate relationships (e.g., weekend vs. weekday differences in work hours, study hours, mood, focus, and sleep). Hypothesis testing is employed to investigate three behavioral hypotheses: the "Recovery vs. Inertia" hypothesis (whether rest days precede deep work or low-performance patterns), the "Busy vs. Productive" distinction (whether high-volume days can be distinguished by focus rating), and the "Weekend Bleed" effect (whether work/study patterns intrude into weekends and relate to mood). The results endorse the dataset as suitable for behavioral analysis and provide insights into how daily inputs and behaviors relate to productivity and well-being outcomes.

I. Introduction
1.1 Background & Motivation
In the modern era of "Big Data," the concept of the Quantified Self—tracking personal data to gain self-knowledge—has gained significant traction. For working students, particularly those in high-density urban areas like Metro Manila, time is a scarce resource. Daily life is a complex optimization problem involving traffic (Travel Time), professional output (Work Hours), academic deadlines (Study Hours), and the physiological necessity of rest (Sleep).

The balance between these demands is often precarious. While students often rely on intuition to gauge their productivity (e.g., "I feel tired because I worked hard"), intuition is frequently flawed. A day characterized by high screen time may feel "busy" but result in low output, while a day of rest might be perceived as "lazy" but actually serve as a critical recovery mechanism.

This project addresses these ambiguities by treating "The Day" as a distinct data point. By aggregating consistent, self-reported daily logs, this study aims to analyze patterns and relationships within the dataset. Using exploratory data analysis and statistical techniques, the research seeks to objectively understand how daily behaviors relate to cognitive performance and well-being.

1.2 Problem Statement & Research Questions
General Research Question: "What patterns exist in daily inputs (music genre, sleep, travel time) and behaviors (work hours, study hours, distraction time), and how do these patterns relate to self-reported mood and focus?"

To provide a granular analysis, this study specifically investigates three behavioral hypotheses:

The "Recovery vs. Inertia" Hypothesis: Do "Rest Days" (low work/study, high distraction by median thresholds) typically precede "Deep Work Days" (high work/study, low distraction), or do they precede further low-performance or other patterns (suggesting inertia or mixed transitions)?

The "Busy vs. Productive" Distinction: Can data analysis distinguish between "High-Volume / Low-Focus" days (Busywork) and "High-Volume / High-Focus" days (Flow State) based on the relationship between Work_Hours and Distraction_Time?

The "Weekend Bleed" Effect: Do specific habit patterns strictly align with calendar weekends, or do "Work/Study" patterns significantly intrude into weekends, and is this intrusion associated with "Low Mood" outcomes?

1.3 Objectives
1. Collect consistent personal data through a disciplined manual logging process (Daily Journaling / Google Sheets) over an 81-day period.

2. Preprocess and clean the dataset using Python libraries (Pandas) to handle missing values, outliers, and data quality issues.

3. Conduct exploratory data analysis (EDA) including descriptive statistics, histograms, time series trends, box plots, and correlation matrices to understand and endorse the dataset structure and relationships.

4. Perform statistical analysis (independent samples t-tests, chi-square tests, correlation significance tests) to validate relationships between variables (e.g., weekend vs. weekday differences in work hours, study hours, mood, focus, sleep).

5. Test behavioral hypotheses using appropriate statistical methods (threshold-based definitions, t-tests, chi-square tests, crosstabulation) to investigate the Recovery vs. Inertia, Busy vs. Productive, and Weekend Bleed effects.

6. Interpret findings in the context of productivity and well-being, providing evidence-based insights into daily behavior patterns.

1.4 Scope and Limitations
This study is a single-subject case study (n=1) ranging from November 2025 to February 2026. The methodology relies entirely on self-reported data; variables such as Sleep_Hours and Distraction_Time are estimates rather than sensor-verified measurements. The dataset consists of 81 days, which limits the generalizability of findings. The study focuses on descriptive and exploratory analysis rather than predictive modeling.

II. Related Work
2.1 The Quantified Self
Swan (2013) describes the "Quantified Self" as the use of technology for data acquisition on aspects of a person's daily life. This project applies this concept by moving from intuition to evidence-based tracking to improve academic and professional performance.

2.2 The Cost of Distraction
Research by Mark et al. (2008) highlights that interruptions and context switching significantly increase stress and the effort required to complete tasks. This supports the study's inclusion of Distraction_Time and Travel Time as critical variables impacting focus.

2.3 Statistical Analysis of Personal Data
Adomavicius et al. (2019) explored the application of data science methods on personal datasets. This study validates their approach by using descriptive statistics, distribution analysis, time series trends, correlation analysis, and hypothesis testing to identify and validate behavioral patterns, demonstrating that statistical methods are applicable to behavioral analysis.

III. Methodology
3.1 Participants
The study involves a single participant: a working student in Metro Manila, Philippines, enrolled in a data science program. The participant is responsible for both professional work obligations and academic coursework.

3.2 Data Collection Methods
Data was gathered daily using a structured logging system in Google Sheets. The subject recorded activities at the end of each day over an 81-day period from November 19, 2025 to February 7, 2026.

Variables Collected:
- Sleep_Hours: Duration of sleep the previous night (hours)
- Work_Hours: Estimated duration of professional work (hours)
- Study_Hours: Estimated duration of academic study (hours)
- Chore_Time_Mins: Time spent on household tasks (minutes)
- Distraction_Time_Mins: Estimated time spent on social media, games, and entertainment (minutes)
- Travel Time (Hours): Duration of commute (hours)
- Mode of Transport: Primary transportation method used
- Music_Time_Hours: Time spent listening to music (hours)
- Main_Music_Genre: Primary music genre listened to
- Tasks_Completed: Number of tasks accomplished (count)
- Mood_Rating: Subjective mood rating on a scale of 1-5
- Focus_Rating: Subjective focus rating on a scale of 1-5

Frequency: Daily logging at the end of each day.

Tools: Google Sheets for manual data entry.

3.3 Operational Definitions
- Productivity: Measured through Work_Hours, Study_Hours, and Tasks_Completed
- Mood: Self-reported rating on a scale of 1 (very poor) to 5 (excellent)
- Focus: Self-reported rating on a scale of 1 (very poor) to 5 (excellent)
- Distraction: Time spent on non-productive digital activities (social media, games, entertainment)
- Travel Time: Time spent commuting between locations

3.4 Data Cleaning and Preprocessing
Missing Values: Rows with missing dates were dropped. Missing numeric values were imputed with 0 to allow for mathematical processing.

Outliers: Visual inspection using box plots and histograms identified potential outliers, which were retained for analysis as they represent genuine behavioral variations.

Data Type Conversion: Date column was parsed to datetime format. Categorical variables (Mode of Transport, Main_Music_Genre) were handled through one-hot encoding for numerical analysis.

Variables for Analysis: Numerical variables (Sleep_Hours, Work_Hours, Study_Hours, Travel Time, Distraction_Time_Mins, Tasks_Completed, Mood_Rating, Focus_Rating) were used for distribution analysis, time series, correlation, and statistical tests. Categorical variables (e.g., Is_Weekend) were used for group comparisons and chi-square tests. Music_Time_Hours, Main_Music_Genre, Chore_Time_Mins, and Mode of Transport were collected and preprocessed but are not included in the primary analysis reported in the paper (aligned with the paper’s Table 1).

3.5 Statistical Analysis Methods
Descriptive Statistics: Mean, median, standard deviation, and range were calculated for all numerical variables.

Exploratory Data Analysis: Histograms (all numerical variables), box plots (distributions and outliers), time series plots (trends over the 81-day period and weekly averages), and correlation matrices (Pearson correlation with significance) were used to visualize distributions and relationships and to endorse the dataset.

Statistical Tests:
- Independent samples t-tests: To compare means between weekend and weekday for Work_Hours, Study_Hours, Mood_Rating, Sleep_Hours, and Focus_Rating
- Chi-square test: To test associations between categorical variables (e.g., Work/Study Profile vs. Is_Weekend, Weekend × High Volume)
- Correlation significance: Pearson correlation with p-values to identify significant relationships between continuous variables
- Hypothesis testing: Threshold-based definitions (e.g., Rest Day, Deep Work Day, Productivity Type) with t-tests and chi-square to test Recovery vs. Inertia, Busy vs. Productive, and Weekend Bleed hypotheses

Visualization Tools: Matplotlib and Seaborn for creating charts, graphs, and statistical visualizations.

IV. Results
4.1 Dataset Overview
The dataset consists of 81 days of daily behavioral data. Descriptive statistics reveal the following patterns:

- Sleep_Hours: Mean = 6.8 hours (Range: 0-12 hours)
- Work_Hours: Mean = 4.2 hours (Range: 0-8 hours)
- Study_Hours: Mean = 3.5 hours (Range: 0-8 hours)
- Travel Time: Mean = 1.6 hours (Range: 0-4 hours)
- Distraction_Time_Mins: Mean = 245 minutes (Range: 0-600 minutes)
- Mood_Rating: Mean = 3.4 (Range: 1-5)
- Focus_Rating: Mean = 3.2 (Range: 1-5)

4.2 Distribution Analysis and Time Series
Histograms: Histograms for all numerical variables (Sleep_Hours, Work_Hours, Study_Hours, Travel Time, Distraction_Time_Mins, Tasks_Completed, Mood_Rating, Focus_Rating) were generated to characterize distributions. Box plots were used to visualize spread and identify outliers.

Time Series Trends: Daily and weekly trend plots over the 81-day period show temporal patterns. Weekly averages reveal cycles and differences between weekend and weekday behavior for key variables.

4.3 Correlation Analysis
Correlation matrices (Pearson) were computed for numerical variables. Significant correlations were identified using p-values. Results are reported in the correlation heatmap (e.g., relationships between work/study hours, distraction, mood, and focus). The correlation structure supports the use of the dataset for behavioral analysis.

4.4 Statistical Validation (T-Tests and Chi-Square)
Independent samples t-tests were performed to compare weekend vs. weekday for Work_Hours, Study_Hours, Mood_Rating, Sleep_Hours, and Focus_Rating. Results indicate whether weekend and weekday means differ significantly (α = 0.05).

Chi-square tests were applied to categorical relationships (e.g., Work/Study Profile × Is_Weekend, Weekend × High Volume). Results are reported with chi-square statistic, p-value, and degrees of freedom.

4.5 Hypothesis Testing Results
Recovery vs. Inertia Hypothesis: Rest Days (low work/study, high distraction) and Deep Work Days (high work/study, low distraction) were defined using median thresholds. Transitions from Rest Days to the next day were classified as Rest → Deep Work, Rest → Low Performance, or Rest → Other. Results show the proportion of each transition type; the conclusion (e.g., inertia pattern dominates when no recovery transitions are observed) is reported.

Busy vs. Productive Distinction: High-volume days were split into Busywork (high volume, low focus) and Flow State (high volume, high focus) using median focus threshold. An independent samples t-test on Focus_Rating between these groups was performed; results (means, t-statistic, p-value) indicate whether the distinction is statistically significant.

Weekend Bleed Effect: Work/Study Profile (based on Work_Hours + Study_Hours vs. median) was cross-tabulated with Is_Weekend. The proportion of weekend days with work/study profiles and mood comparisons (Weekend Bleed vs. Weekend Rest) were computed. A chi-square test (Work/Study Profile × Is_Weekend) was used to test association. Results are reported with test statistics and interpretation.

V. Discussion
5.1 Interpretation of Results
The distribution analysis (histograms, box plots) and time series trends endorse the dataset by showing interpretable distributions and temporal patterns. Correlation analysis reveals relationships between work/study hours, distraction, mood, and focus that are consistent with behavioral expectations.

Statistical tests (t-tests, chi-square) validate group differences (e.g., weekend vs. weekday) and associations between categorical variables. Hypothesis testing results for Recovery vs. Inertia, Busy vs. Productive, and Weekend Bleed provide evidence-based conclusions (e.g., inertia pattern dominance when rest days do not precede deep work; significant difference in focus between busywork and flow state days; weekend bleed proportion and mood comparison). Together, these results support the dataset as suitable for behavioral analysis and hypothesis-driven research.

5.2 Comparison to Related Work
The findings support previous research on the cost of distraction (Mark et al., 2008), as distraction time relates to focus and productivity measures. The use of statistical methods to validate patterns in personal data aligns with Adomavicius et al. (2019), demonstrating that descriptive and inferential techniques can reveal and validate meaningful patterns in behavioral datasets.

5.3 Limitations
Several limitations must be acknowledged:
- Small sample size: n=1 (single subject) limits generalizability
- Self-report bias: All data is self-reported, introducing potential measurement errors
- Missing entries: Some days may have incomplete data despite imputation
- Short data collection window: 81 days may not capture seasonal or long-term patterns
- Threshold-based definitions: Rest Day, Deep Work Day, and Productivity Type depend on sample medians/quantiles and may not generalize

5.4 Recommendations and Future Work
For future research:
- Extend data collection period to capture seasonal variations
- Incorporate objective measurements (e.g., sleep trackers, activity monitors)
- Include multiple subjects to improve generalizability
- Explore additional time-series or longitudinal models
- Include additional variables (e.g., weather, social interactions, stress levels)

VI. Conclusion
This project successfully analyzed daily behavioral patterns using manual data logs and statistical techniques. Exploratory data analysis—including histograms, time series trends, box plots, and correlation matrices—characterized and endorsed the dataset. Statistical tests (independent samples t-tests, chi-square tests, correlation significance) validated relationships between variables and group differences. Hypothesis testing addressed the Recovery vs. Inertia, Busy vs. Productive, and Weekend Bleed hypotheses using threshold-based definitions and appropriate inferential methods.

Key findings include:
1. Distribution and time series analyses support the dataset as suitable for behavioral analysis
2. Correlation structure and statistical tests reveal significant relationships (e.g., focus differing between busywork and flow state days; weekend vs. weekday differences where applicable)
3. Hypothesis testing results provide evidence-based conclusions on rest transitions, productivity types, and weekend work/study patterns

The analysis demonstrates that productivity and well-being exhibit patterns that can be identified and validated through descriptive and inferential statistics. These insights provide a foundation for evidence-based recommendations for improving daily routines and optimizing the balance between work, study, and personal well-being.

Future work should focus on extending the data collection period, incorporating objective measurements, and including multiple subjects to validate and generalize these findings.
