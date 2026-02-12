CCDATSCL Project: The Work-Study-Life Profile
Author: Brando Allen A. Donato  Date: February 6, 2026

Abstract
This study explores the concept of the "Quantified Self" by analyzing the daily habits of a working student in Metro Manila over a 74-day period. Addressing the challenges of balancing professional obligations, academic requirements, and personal well-being, this research employs a disciplined, manual data collection method to record daily behavioral metrics. The study utilizes K-Means Clustering (Unsupervised Learning) to identify distinct "Daily Profiles" based on self-reported variables such as sleep duration, travel time, work/study hours, and digital distractions. Furthermore, Analysis of Variance (ANOVA) is conducted to validate these clusters against daily mood and focus ratings. Additionally, Multiple Linear Regression (MLR) is employed to predict Mood_Rating and Focus_Rating, identifying which daily inputs and behaviors most significantly influence productivity and well-being. The results aim to reveal hidden behavioral patterns—such as the "Weekend Bleed" effect or the "Busy vs. Productive" distinction—providing a mathematical taxonomy of daily life to optimize productivity and mitigate burnout.

I. Introduction
1.1 Background & Motivation
In the modern era of "Big Data," the concept of the Quantified Self—tracking personal data to gain self-knowledge—has gained significant traction. For working students, particularly those in high-density urban areas like Metro Manila, time is a scarce resource. Daily life is a complex optimization problem involving traffic (Travel Time), professional output (Work Hours), academic deadlines (Study Hours), and the physiological necessity of rest (Sleep).

The balance between these demands is often precarious. While students often rely on intuition to gauge their productivity (e.g., "I feel tired because I worked hard"), intuition is frequently flawed. A day characterized by high screen time may feel "busy" but result in low output, while a day of rest might be perceived as "lazy" but actually serve as a critical recovery mechanism.

This project addresses these ambiguities by treating "The Day" as a distinct data point. By aggregating consistent, self-reported daily logs, this study aims to construct a "taxonomy of days." Using unsupervised machine learning techniques, specifically K-Means clustering, the research seeks to objectively categorize days into specific profiles to better understand the drivers of cognitive performance.

1.2 Problem Statement & Hypotheses
General Research Question: "How do daily inputs (music genre, sleep, travel time) and behaviors (work hours, study hours, distraction time) cluster into distinct 'Daily Profiles,' and how do these profiles correlate with self-reported mood and focus?"

To provide a granular analysis, this study specifically investigates three behavioral hypotheses:

The "Recovery vs. Inertia" Hypothesis: Do "Rest Profiles" (High Leisure, Low Productivity) typically precede "Deep Work" clusters (suggesting recovery), or do they precede further low-performance clusters (suggesting a state of inertia)?

The "Busy vs. Productive" Distinction: Can unsupervised clustering distinguish between "High-Volume / Low-Focus" days (Busywork) and "High-Volume / High-Focus" days (Flow State) based solely on the ratio of Work_Hours to Distraction_Time?

The "Weekend Bleed" Effect: Do specific habit profiles strictly align with calendar weekends, or do "Work/Study" profiles significantly intrude into weekends, and is this intrusion the strongest predictor of "Low Mood" clusters?

1.3 Objectives
Collect consistent personal data through a disciplined manual logging process (Daily Journaling / Google Sheets) over a 74-day period.

Preprocess and normalize the dataset using Python libraries (Pandas, Scikit-learn) to handle disparate scales (e.g., minutes of distraction vs. hours of sleep).

Model the data using K-Means Clustering to identify natural, mathematical groupings of daily behaviors.

Validate the significance of these clusters using statistical tests (ANOVA) against subjective metrics of Mood and Focus.

Build Multiple Linear Regression (MLR) models to predict Mood_Rating and Focus_Rating, identifying significant predictors and their coefficients to understand which factors most influence productivity and well-being.

1.4 Scope and Limitations
This study is a single-subject case study (n=1) ranging from November 2025 to February 2026. The methodology relies entirely on self-reported data; variables such as Sleep_Hours and Distraction_Time are estimates rather than sensor-verified measurements.

II. Related Work
2.1 The Quantified Self
Swan (2013) describes the "Quantified Self" as the use of technology for data acquisition on aspects of a person's daily life. This project applies this concept by moving from intuition to evidence-based tracking to improve academic and professional performance.

2.2 The Cost of Distraction
Research by Mark et al. (2008) highlights that interruptions and context switching significantly increase stress and the effort required to complete tasks. This supports the study's inclusion of Distraction_Time and Travel Time as critical negative features impacting focus.

2.3 Clustering Personal Data
Adomavicius et al. (2019) explored the application of data science algorithms on personal datasets. This study validates their approach by using K-Means not to classify static objects, but to classify temporal units (days), proving that unsupervised learning is applicable to behavioral analysis.

III. Methodology
3.1 Data Collection
Data was gathered daily using a structured logging system in Google Sheets. The subject recorded activities at the end of each day.

Variable            Description
====================================================================================
Work / Study Hours  Estimated duration of professional and academic work.
Distraction Time    Estimated time spent on social media, games, and entertainment.
Sleep Hours         Duration of sleep the previous night.
Travel Time         Duration of commute (Hours).
Mood / Focus        Subjective rating on a scale of 1-5.

3.2 Data Description
The dataset consists of N=74 days (rows) with the following key features:

Inputs: Sleep_Hours, Music_Time_Hours, Travel Time (Hours), Mode of Transport

Behaviors: Work_Hours, Study_Hours, Chore_Time_Mins, Distraction_Time_Mins, Tasks_Completed

Outputs (Targets): Mood_Rating, Focus_Rating

3.3 Preprocessing
Cleaning: Rows with missing dates were dropped. Missing numeric values were imputed with 0 to allow for mathematical processing.

Scaling: A StandardScaler (Z-score normalization) was applied. This is critical because Distraction_Time (measured in hundreds of minutes) has a much larger variance than Travel Time (measured in single-digit hours). Scaling ensures that the clustering algorithm treats all variables with equal weight.

IV. Results & Discussion
4.1 Clustering Results (K-Means)
The K-Means algorithm (set to k=3) identified three distinct types of days based on the input features:

Cluster 0: "The Commuter Grind"
Characteristics: Defined by significant Travel Time and moderate Work_Hours, but lower Study_Hours.

Observation: These days represent the logistical burden of the working student life, where travel eats into academic time.

Cluster 1: "The Deep Work / WFH Day"
Characteristics: Characterized by Zero Travel Time, High Work_Hours, and High Study_Hours.

Observation: These are the most productive days, likely correlating with Work-From-Home setups where commute time is converted into productive output.

Cluster 2: "The Distracted Recovery"
Characteristics: High Distraction_Time_Mins, High Sleep_Hours, and Low Tasks_Completed.

Observation: These days likely align with weekends or burnout recovery periods.

4.2 Statistical Validation (ANOVA)
An ANOVA test was performed to check if the Mood_Rating and Focus_Rating significantly differed across the three clusters.

Result: The P-values indicate whether the differences in mood and focus are statistically significant. A low p-value (< 0.05) would confirm that the type of day (e.g., Commuting vs. Deep Work) directly influences emotional well-being and cognitive performance.

4.3 Predictive Modeling (Multiple Linear Regression)
Multiple Linear Regression (MLR) models were constructed to predict Mood_Rating and Focus_Rating based on daily inputs and behaviors. The MLR models provide:

Coefficient Analysis: Identifies which factors (Sleep_Hours, Travel Time, Work_Hours, Study_Hours, Distraction_Time_Mins, etc.) most significantly influence mood and focus, with positive coefficients indicating increases and negative coefficients indicating decreases.

Statistical Significance: P-values for each predictor determine which factors are statistically significant (p < 0.05) in predicting outcomes.

Model Performance: R², Adjusted R², RMSE, and MAE metrics evaluate the predictive power of the models.

Interpretation: The MLR results complement the clustering analysis by quantifying the relationship between specific behaviors and outcomes, enabling evidence-based recommendations for optimizing daily routines.

V. Conclusion
This project successfully classified daily life into quantifiable profiles using manual data logs and predictive models. The inclusion of Travel Time proved to be a defining feature, clearly distinguishing low-energy days from high-productivity days. The K-Means clustering revealed distinct behavioral patterns, while the MLR models quantified the relationships between daily inputs and outcomes. The analysis suggests that productivity is not random; it is a result of specific behavioral combinations that can be predicted and optimized.

The combination of unsupervised learning (clustering) and supervised learning (MLR) provides both pattern discovery and predictive insights, enabling evidence-based recommendations for improving productivity and well-being.

Future Work: Future iterations could explore time-series analysis, incorporate additional features (e.g., weather, social interactions), or apply advanced machine learning techniques (e.g., Random Forest, Neural Networks) for improved prediction accuracy. Longitudinal studies with multiple subjects could validate and generalize these findings.