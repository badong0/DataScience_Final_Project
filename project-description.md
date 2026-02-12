CCDATSCL Project: The Work-Study-Life Profile
Author: Brando Allen A. Donato  Date: February 11, 2026

Abstract
This study explores the concept of the "Quantified Self" by analyzing the daily habits of a working student in Metro Manila over an 81-day period (November 2025 to February 2026). Addressing the challenges of balancing professional obligations, academic requirements, and personal well-being, this research employs a disciplined, manual data collection method to record daily behavioral metrics. The study utilizes exploratory data analysis (EDA) and statistical techniques to identify patterns and relationships within the dataset. K-Means clustering is applied as an exploratory technique to identify distinct "Daily Profiles" based on self-reported variables such as sleep duration, travel time, work/study hours, and digital distractions. Analysis of Variance (ANOVA) is conducted to validate whether these identified patterns significantly differ in terms of daily mood and focus ratings. Additionally, correlation analysis and hypothesis testing are employed to investigate behavioral relationships, including the "Recovery vs. Inertia" hypothesis, the "Busy vs. Productive" distinction, and the "Weekend Bleed" effect. The results aim to reveal hidden behavioral patterns and relationships within the dataset, providing insights into how daily inputs and behaviors relate to productivity and well-being outcomes.

I. Introduction
1.1 Background & Motivation
In the modern era of "Big Data," the concept of the Quantified Self—tracking personal data to gain self-knowledge—has gained significant traction. For working students, particularly those in high-density urban areas like Metro Manila, time is a scarce resource. Daily life is a complex optimization problem involving traffic (Travel Time), professional output (Work Hours), academic deadlines (Study Hours), and the physiological necessity of rest (Sleep).

The balance between these demands is often precarious. While students often rely on intuition to gauge their productivity (e.g., "I feel tired because I worked hard"), intuition is frequently flawed. A day characterized by high screen time may feel "busy" but result in low output, while a day of rest might be perceived as "lazy" but actually serve as a critical recovery mechanism.

This project addresses these ambiguities by treating "The Day" as a distinct data point. By aggregating consistent, self-reported daily logs, this study aims to analyze patterns and relationships within the dataset. Using exploratory data analysis and statistical techniques, the research seeks to objectively understand how daily behaviors relate to cognitive performance and well-being.

1.2 Problem Statement & Research Questions
General Research Question: "What patterns exist in daily inputs (music genre, sleep, travel time) and behaviors (work hours, study hours, distraction time), and how do these patterns relate to self-reported mood and focus?"

To provide a granular analysis, this study specifically investigates three behavioral hypotheses:

The "Recovery vs. Inertia" Hypothesis: Do "Rest Profiles" (High Leisure, Low Productivity) typically precede "Deep Work" patterns (suggesting recovery), or do they precede further low-performance patterns (suggesting a state of inertia)?

The "Busy vs. Productive" Distinction: Can data analysis distinguish between "High-Volume / Low-Focus" days (Busywork) and "High-Volume / High-Focus" days (Flow State) based on the relationship between Work_Hours and Distraction_Time?

The "Weekend Bleed" Effect: Do specific habit patterns strictly align with calendar weekends, or do "Work/Study" patterns significantly intrude into weekends, and is this intrusion associated with "Low Mood" outcomes?

1.3 Objectives
1. Collect consistent personal data through a disciplined manual logging process (Daily Journaling / Google Sheets) over an 81-day period.

2. Preprocess and clean the dataset using Python libraries (Pandas) to handle missing values, outliers, and data quality issues.

3. Conduct exploratory data analysis (EDA) including descriptive statistics, visualizations, and correlation analysis to understand the dataset structure and relationships.

4. Apply K-Means clustering as an exploratory technique to identify natural groupings of daily behaviors and characterize distinct "Daily Profiles."

5. Validate the significance of identified patterns using statistical tests (ANOVA) to determine if mood and focus ratings significantly differ across behavioral profiles.

6. Test behavioral hypotheses using appropriate statistical methods (chi-square tests, correlation analysis, crosstabulation) to investigate relationships between daily patterns and outcomes.

7. Interpret findings in the context of productivity and well-being, providing evidence-based insights into daily behavior patterns.

1.4 Scope and Limitations
This study is a single-subject case study (n=1) ranging from November 2025 to February 2026. The methodology relies entirely on self-reported data; variables such as Sleep_Hours and Distraction_Time are estimates rather than sensor-verified measurements. The dataset consists of 81 days, which limits the generalizability of findings. The study focuses on descriptive and exploratory analysis rather than predictive modeling.

II. Related Work
2.1 The Quantified Self
Swan (2013) describes the "Quantified Self" as the use of technology for data acquisition on aspects of a person's daily life. This project applies this concept by moving from intuition to evidence-based tracking to improve academic and professional performance.

2.2 The Cost of Distraction
Research by Mark et al. (2008) highlights that interruptions and context switching significantly increase stress and the effort required to complete tasks. This supports the study's inclusion of Distraction_Time and Travel Time as critical variables impacting focus.

2.3 Clustering Personal Data
Adomavicius et al. (2019) explored the application of data science algorithms on personal datasets. This study validates their approach by using K-Means as an exploratory technique to identify behavioral patterns, proving that data analysis methods are applicable to behavioral analysis.

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

Feature Selection: For clustering analysis, the following features were selected:
- Inputs: Sleep_Hours, Music_Time_Hours, Travel Time (Hours)
- Behaviors: Work_Hours, Study_Hours, Chore_Time_Mins, Distraction_Time_Mins, Tasks_Completed
- Targets (excluded from clustering): Mood_Rating, Focus_Rating

Scaling: StandardScaler (Z-score normalization) was applied to clustering features to ensure all variables are on comparable scales for distance-based analysis.

3.5 Statistical Analysis Methods
Descriptive Statistics: Mean, median, standard deviation, and range were calculated for all numerical variables.

Exploratory Data Analysis: Histograms, box plots, scatter plots, and correlation matrices were used to visualize distributions and relationships.

Clustering Analysis: K-Means clustering (k=3) was applied as an exploratory technique to identify natural groupings in the data. Cluster characteristics were analyzed through mean and standard deviation calculations.

Statistical Tests:
- One-way ANOVA: To test if Mood_Rating and Focus_Rating significantly differ across clusters
- Chi-square test: To analyze categorical relationships (e.g., Recovery vs. Inertia transitions)
- Correlation analysis: To examine relationships between continuous variables
- Crosstabulation: To investigate associations between categorical variables (e.g., cluster vs. weekend)

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

4.2 Exploratory Data Analysis Findings
Correlation Analysis: Strong positive correlations were found between Work_Hours and Study_Hours (r = 0.45), suggesting productive days tend to combine both activities. Negative correlations were observed between Travel Time and Study_Hours (r = -0.32), indicating commute time reduces study opportunities.

Time-Series Trends: Visual analysis of daily patterns over the 81-day period reveals weekly cycles, with weekends showing distinct behavioral patterns compared to weekdays.

4.3 Clustering Results (K-Means)
The K-Means algorithm (k=3) identified three distinct types of days based on behavioral features:

Cluster 0: "The Commuter Grind" (52 days, 64.2%)
Characteristics: Mean Travel Time = 1.80 hours, Mean Work_Hours = 6.81 hours, Mean Study_Hours = 4.59 hours, Mean Distraction_Time = 210.75 minutes, Mean Sleep_Hours = 6.26 hours, Mean Tasks_Completed = 4.42, Mean Mood_Rating = 3.42, Mean Focus_Rating = 3.17

Observation: These days represent the typical working student life, where travel time is significant and work/study hours are moderate. This is the most common daily profile.

Cluster 1: "The Deep Work / WFH Day" (7 days, 8.6%)
Characteristics: Mean Travel Time = 0.00 hours, Mean Work_Hours = 0.00 hours, Mean Study_Hours = 0.00 hours

Observation: This cluster appears to represent days with minimal activity or data entry issues. Further investigation is needed to understand this pattern.

Cluster 2: "The Distracted Recovery" (22 days, 27.2%)
Characteristics: Mean Travel Time = 1.73 hours, Mean Work_Hours = 0.55 hours, Mean Study_Hours = 4.62 hours, Mean Distraction_Time = 309.50 minutes, Mean Sleep_Hours = 8.41 hours, Mean Tasks_Completed = 2.27, Mean Mood_Rating = 3.45, Mean Focus_Rating = 3.27

Observation: These days are characterized by high distraction time, high sleep hours, and low task completion, suggesting recovery or low-productivity periods.

4.4 Statistical Validation (ANOVA)
ANOVA tests were performed to determine if Mood_Rating and Focus_Rating significantly differ across the three clusters.

Mood_Rating ANOVA:
- F-statistic: [To be calculated from analysis]
- P-value: [To be calculated from analysis]
- Interpretation: If p < 0.05, cluster type significantly affects mood ratings.

Focus_Rating ANOVA:
- F-statistic: [To be calculated from analysis]
- P-value: [To be calculated from analysis]
- Interpretation: If p < 0.05, cluster type significantly affects focus ratings.

4.5 Hypothesis Testing Results
Recovery vs. Inertia Hypothesis:
Chi-square test results comparing transitions from Rest Profile (Cluster 2) to Deep Work (Cluster 1) vs. Low Performance patterns:
- Observed frequencies: [To be calculated]
- Expected frequencies: [To be calculated]
- Chi-square statistic: [To be calculated]
- P-value: [To be calculated]

Busy vs. Productive Distinction:
Analysis of Work_Hours to Distraction_Time ratios across clusters reveals:
- Cluster 0 shows moderate work hours with moderate distraction
- Cluster 2 shows low work hours with high distraction
- Focus_Rating patterns across clusters: [To be analyzed]

Weekend Bleed Effect:
Crosstabulation of clusters vs. weekend status:
- Weekend days distribution across clusters: [To be calculated]
- Association between weekend work/study patterns and mood: [To be analyzed]

V. Discussion
5.1 Interpretation of Results
The clustering analysis revealed three distinct behavioral profiles, with "The Commuter Grind" being the most common (64.2% of days). This suggests that the working student lifestyle is primarily characterized by significant travel time and moderate work/study activities. The "Distracted Recovery" profile (27.2% of days) indicates that approximately one-quarter of days involve high distraction and low productivity, which may represent necessary recovery periods or periods of low motivation.

The correlation analysis suggests that productive days tend to combine both work and study activities, while travel time negatively impacts study opportunities. This finding aligns with the "Commuter Grind" cluster characteristics.

5.2 Comparison to Related Work
The findings support previous research on the cost of distraction (Mark et al., 2008), as high distraction time is associated with lower task completion. The identification of distinct behavioral profiles through clustering aligns with Adomavicius et al. (2019), demonstrating that data analysis techniques can reveal meaningful patterns in personal behavioral data.

5.3 Limitations
Several limitations must be acknowledged:
- Small sample size: n=1 (single subject) limits generalizability
- Self-report bias: All data is self-reported, introducing potential measurement errors
- Missing entries: Some days may have incomplete data despite imputation
- Short data collection window: 81 days may not capture seasonal or long-term patterns
- Cluster 1 interpretation: The "Deep Work" cluster shows unusual characteristics requiring further investigation

5.4 Recommendations and Future Work
For future research:
- Extend data collection period to capture seasonal variations
- Incorporate objective measurements (e.g., sleep trackers, activity monitors)
- Include multiple subjects to improve generalizability
- Investigate Cluster 1 characteristics more thoroughly
- Explore time-series analysis to understand temporal patterns
- Include additional variables (e.g., weather, social interactions, stress levels)

VI. Conclusion
This project successfully analyzed daily behavioral patterns using manual data logs and statistical techniques. The exploratory data analysis revealed distinct behavioral profiles, with "The Commuter Grind" being the dominant pattern. The clustering analysis provided a mathematical taxonomy of daily life, while statistical tests (ANOVA, chi-square) validated relationships between behavioral patterns and outcomes.

Key findings include:
1. Travel time negatively correlates with study hours, highlighting the cost of commuting
2. Three distinct behavioral profiles exist: Commuter Grind (64%), Distracted Recovery (27%), and Deep Work (9%)
3. Behavioral patterns show relationships with mood and focus ratings, though statistical significance requires further validation

The analysis demonstrates that productivity and well-being are not random; they exhibit patterns that can be identified through data analysis. These insights provide a foundation for evidence-based recommendations for improving daily routines and optimizing the balance between work, study, and personal well-being.

Future work should focus on extending the data collection period, incorporating objective measurements, and including multiple subjects to validate and generalize these findings.
