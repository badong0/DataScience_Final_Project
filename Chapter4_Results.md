# Chapter 4: Results

This chapter presents the findings from the analysis of 81 days of daily behavioral data collected from November 19, 2025 to February 7, 2026. Results are organized into five main sections: (1) Dataset Overview and Descriptive Statistics, (2) Distribution Analysis, (3) Time Series Trends, (4) Correlation Analysis, and (5) Statistical Test Results and Hypothesis Testing.

---

## 4.1 Dataset Overview and Descriptive Statistics

### 4.1.1 Dataset Characteristics

The final cleaned dataset consists of **81 observations** (days) with **15 original variables** expanded to **30 variables** after preprocessing and feature engineering. All observations span a continuous 81-day period with no missing dates. The dataset includes **23 weekend days** (28.4%) and **58 weekday days** (71.6%).

### 4.1.2 Descriptive Statistics Summary

Table I presents descriptive statistics for all numerical variables, including mean, median, standard deviation, minimum, maximum, and range values.

**TABLE I**  
**DESCRIPTIVE STATISTICS FOR NUMERICAL VARIABLES (N=81)**

| Variable | Mean | Median | Std Dev | Min | Max | Range |
|----------|------|--------|---------|-----|-----|-------|
| Sleep_Hours | 6.30 | 6.00 | 2.69 | 0.00 | 12.00 | 12.00 |
| Work_Hours | 4.52 | 6.00 | 3.44 | 0.00 | 10.00 | 10.00 |
| Study_Hours | 4.20 | 4.00 | 2.72 | 0.00 | 11.73 | 11.73 |
| Travel Time (Hours) | 1.62 | 1.40 | 0.88 | 0.00 | 3.00 | 3.00 |
| Distraction_Time_Mins | 219.36 | 210.00 | 104.91 | 0.00 | 500.00 | 500.00 |
| Tasks_Completed | 3.46 | 3.00 | 2.09 | 0.00 | 10.00 | 10.00 |
| Mood_Rating | 3.14 | 3.00 | 1.44 | 0.00 | 5.00 | 5.00 |
| Focus_Rating | 2.93 | 3.00 | 1.52 | 0.00 | 5.00 | 5.00 |

### 4.1.3 Key Patterns in Descriptive Statistics

**Sleep Patterns**: Mean sleep duration was 6.30 hours (SD = 2.69), with a median of 6.00 hours. The range spans from 0 to 12 hours, indicating substantial day-to-day variation. The distribution shows some days with no recorded sleep (0 hours) and others with extended sleep periods (up to 12 hours).

**Productivity Variables**: 
- **Work_Hours**: Mean of 4.52 hours (SD = 3.44) with a median of 6.00 hours, indicating a right-skewed distribution where many days have low work hours but some days have high work loads (up to 10 hours).
- **Study_Hours**: Mean of 4.20 hours (SD = 2.72) with a median of 4.00 hours, showing a more symmetric distribution. Maximum study hours reached 11.73 hours on intensive study days.
- **Tasks_Completed**: Mean of 3.46 tasks (SD = 2.09) with a median of 3.00 tasks, indicating moderate daily task completion.

**Time Allocation**:
- **Travel Time**: Mean of 1.62 hours (SD = 0.88), reflecting Metro Manila commute patterns. Median of 1.40 hours suggests most days involve moderate commute times.
- **Distraction_Time_Mins**: Mean of 219.36 minutes (3.66 hours, SD = 104.91), with a median of 210 minutes. The wide range (0-500 minutes) indicates substantial variation in digital distraction levels.

**Subjective Well-being**:
- **Mood_Rating**: Mean of 3.14 (SD = 1.44) on a 1-5 scale, with median of 3.00, indicating neutral to slightly positive average mood.
- **Focus_Rating**: Mean of 2.93 (SD = 1.52) with median of 3.00, suggesting moderate focus levels with room for improvement.

---

## 4.2 Distribution Analysis

### 4.2.1 Histogram Analysis

Histograms were generated for all eight numerical variables to visualize their distributions. Figure 1 presents histograms for all variables, revealing the following distribution characteristics:

**Figure 1. Histograms of All Numerical Variables**  
*This figure shows the distribution shapes for Sleep_Hours, Work_Hours, Study_Hours, Travel Time, Distraction_Time_Mins, Tasks_Completed, Mood_Rating, and Focus_Rating over 81 days. Mean and median lines are overlaid to show central tendencies.*

**Key Distribution Findings**:

1. **Sleep_Hours**: Shows a bimodal distribution with peaks around 6-7 hours and 0 hours, suggesting distinct patterns of regular sleep vs. sleep-deprived days.

2. **Work_Hours**: Right-skewed distribution with a concentration of values at lower hours (0-2 hours) and a tail extending to 10 hours, indicating most days have low work hours with occasional intensive work days.

3. **Study_Hours**: Relatively symmetric distribution centered around 4 hours, with a slight right skew. Most values cluster between 2-6 hours.

4. **Travel Time**: Right-skewed distribution with most values concentrated below 2 hours, reflecting typical commute patterns with occasional longer travel days.

5. **Distraction_Time_Mins**: Approximately normal distribution centered around 200-250 minutes, with symmetric spread indicating consistent distraction patterns.

6. **Tasks_Completed**: Right-skewed distribution with most days completing 2-4 tasks, with fewer days achieving high task counts (8-10 tasks).

7. **Mood_Rating**: Bimodal distribution with peaks at 2 and 4, suggesting distinct good and poor mood days, with fewer neutral (3) ratings.

8. **Focus_Rating**: Approximately normal distribution centered at 3, with symmetric spread indicating consistent focus patterns.

### 4.2.2 Box Plot Analysis

Box plots were generated to visualize distributions, identify outliers, and compare variability across variables. Figure 4 presents box plots for all numerical variables.

**Figure 4. Box Plots Showing Distributions and Outliers**  
*This figure displays box plots for all numerical variables, showing quartiles, medians, and potential outliers. Outliers beyond 1.5×IQR are shown as individual points.*

**Outlier Analysis**:
- **Sleep_Hours**: Several outliers identified at 0 hours (no sleep days) and at 10-12 hours (extended sleep days)
- **Work_Hours**: Outliers at 0 hours (no work days) and at 9-10 hours (intensive work days)
- **Study_Hours**: Outlier at 11.73 hours (intensive study day)
- **Distraction_Time_Mins**: Outliers at 0 minutes (no distraction days) and at 400-500 minutes (high distraction days)
- **Mood_Rating and Focus_Rating**: Outliers at 0 (likely data entry issues or extreme days) and at 5 (excellent days)

All identified outliers were retained in the analysis as they represent genuine behavioral variations rather than measurement errors.

---

## 4.3 Time Series Trends

### 4.3.1 Daily Trends

Time series plots were generated to examine temporal patterns over the 81-day period. Figure 2 presents daily trends for four key variables: Work_Hours, Study_Hours, Mood_Rating, and Focus_Rating.

**Figure 2. Time Series Trends Over 81-Day Period**  
*This figure shows daily values for Work_Hours, Study_Hours, Mood_Rating, and Focus_Rating from November 19, 2025 to February 7, 2026. Trends reveal daily fluctuations and temporal patterns.*

**Temporal Patterns Observed**:

1. **Work_Hours**: Shows high variability with periods of intensive work (peaks at 8-10 hours) alternating with low-work periods (0-2 hours). No clear long-term trend, but weekly cycles are apparent.

2. **Study_Hours**: Displays moderate variability with sustained periods of 4-6 hours of study, punctuated by intensive study days (8-11 hours). Study hours appear more consistent than work hours.

3. **Mood_Rating**: Shows cyclical patterns with periods of sustained positive mood (4-5) alternating with lower mood periods (1-2). Mood appears to correlate with work/study intensity.

4. **Focus_Rating**: Displays similar cyclical patterns to mood, with focus ratings generally ranging from 2-4. Focus appears to be inversely related to distraction time.

### 4.3.2 Weekly Trends

Weekly averages were calculated to identify weekly cycles and weekend vs. weekday differences. Figure 5 presents weekly trend analysis.

**Figure 5. Weekly Trend Analysis**  
*This figure shows weekly averages for Work_Hours, Study_Hours, Mood_Rating, and Focus_Rating. Weekly patterns reveal differences between weekend and weekday behavior.*

**Weekly Pattern Findings**:

- **Work_Hours**: Consistently lower on weekends compared to weekdays, confirming expected work schedule patterns.
- **Study_Hours**: Higher on weekends compared to weekdays, suggesting weekend study sessions compensate for weekday work obligations.
- **Mood_Rating**: Slight variations between weeks but no clear weekend vs. weekday pattern.
- **Focus_Rating**: Moderate consistency across weeks with some weekly variation.

---

## 4.4 Correlation Analysis

### 4.4.1 Correlation Matrix

A Pearson correlation matrix was computed for all numerical variables to identify relationships between variables. Figure 3 and Figure 6 present correlation heatmaps.

**Figure 3. Correlation Matrix Heatmap**  
*This figure displays Pearson correlation coefficients between all pairs of numerical variables. Color intensity indicates correlation strength, with red representing negative correlations and blue representing positive correlations.*

**Figure 6. Statistical Correlation Matrix**  
*This figure shows the correlation matrix with statistical significance indicators, highlighting significant correlations (p < 0.05).*

### 4.4.2 Significant Correlations

Table II presents all statistically significant correlations (p < 0.05) identified in the analysis. A total of **20 significant correlations** were found among the 8 numerical variables.

**TABLE II**  
**SIGNIFICANT CORRELATIONS (p < 0.05)**

| Variable 1 | Variable 2 | Correlation (r) | p-value | Interpretation |
|------------|-----------|-----------------|---------|----------------|
| Sleep_Hours | Travel Time (Hours) | 0.283 | 0.0106 | Weak positive |
| Sleep_Hours | Distraction_Time_Mins | 0.590 | <0.0001 | Moderate positive |
| Sleep_Hours | Mood_Rating | 0.483 | <0.0001 | Moderate positive |
| Sleep_Hours | Focus_Rating | 0.422 | 0.0001 | Moderate positive |
| Work_Hours | Travel Time (Hours) | 0.315 | 0.0041 | Weak positive |
| Work_Hours | Tasks_Completed | 0.582 | <0.0001 | Moderate positive |
| Work_Hours | Mood_Rating | 0.274 | 0.0134 | Weak positive |
| Work_Hours | Focus_Rating | 0.248 | 0.0253 | Weak positive |
| Study_Hours | Distraction_Time_Mins | 0.243 | 0.0289 | Weak positive |
| Study_Hours | Tasks_Completed | 0.354 | 0.0012 | Weak positive |
| Study_Hours | Mood_Rating | 0.273 | 0.0136 | Weak positive |
| Study_Hours | Focus_Rating | 0.257 | 0.0204 | Weak positive |
| Travel Time (Hours) | Tasks_Completed | 0.308 | 0.0051 | Weak positive |
| Travel Time (Hours) | Mood_Rating | 0.435 | <0.0001 | Moderate positive |
| Travel Time (Hours) | Focus_Rating | 0.323 | 0.0033 | Weak positive |
| Distraction_Time_Mins | Mood_Rating | 0.429 | 0.0001 | Moderate positive |
| Distraction_Time_Mins | Focus_Rating | 0.373 | 0.0006 | Weak positive |
| Tasks_Completed | Mood_Rating | 0.361 | 0.0009 | Weak positive |
| Tasks_Completed | Focus_Rating | 0.380 | 0.0005 | Weak positive |
| Mood_Rating | Focus_Rating | 0.621 | <0.0001 | Strong positive |

**Correlation Strength Interpretation**:
- **Strong** (|r| > 0.7): Mood_Rating ↔ Focus_Rating (r = 0.621)
- **Moderate** (0.4 < |r| < 0.7): Sleep_Hours ↔ Distraction_Time_Mins (r = 0.590), Work_Hours ↔ Tasks_Completed (r = 0.582), Sleep_Hours ↔ Mood_Rating (r = 0.483), Travel Time ↔ Mood_Rating (r = 0.435), Distraction_Time_Mins ↔ Mood_Rating (r = 0.429), Sleep_Hours ↔ Focus_Rating (r = 0.422)
- **Weak** (|r| < 0.4): All other significant correlations

### 4.4.3 Key Correlation Findings

1. **Strongest Relationship**: Mood_Rating and Focus_Rating show the strongest positive correlation (r = 0.621, p < 0.0001), indicating that mood and focus are closely related psychological states.

2. **Sleep Relationships**: Sleep_Hours shows moderate positive correlations with Distraction_Time_Mins (r = 0.590), Mood_Rating (r = 0.483), and Focus_Rating (r = 0.422), suggesting that sleep duration relates to both distraction levels and well-being.

3. **Productivity Relationships**: Work_Hours and Tasks_Completed show moderate positive correlation (r = 0.582), indicating that more work hours are associated with more completed tasks.

4. **Travel Time Relationships**: Travel Time shows moderate positive correlation with Mood_Rating (r = 0.435) and weak positive correlations with Focus_Rating (r = 0.323) and Tasks_Completed (r = 0.308), suggesting that commute time may relate to productivity and well-being.

5. **Distraction Relationships**: Distraction_Time_Mins shows moderate positive correlations with Sleep_Hours (r = 0.590) and Mood_Rating (r = 0.429), and weak positive correlation with Focus_Rating (r = 0.373), indicating complex relationships between distraction, sleep, and well-being.

---

## 4.5 Statistical Test Results

### 4.5.1 Independent Samples t-Tests: Weekend vs. Weekday Comparisons

Independent samples t-tests were performed to compare means between weekend and weekday groups for five key variables. Table III presents the complete results.

**TABLE III**  
**INDEPENDENT SAMPLES t-TEST RESULTS: WEEKEND VS. WEEKDAY**

| Variable | Weekend Mean (SD) | Weekday Mean (SD) | n (Weekend) | n (Weekday) | t-statistic | p-value | Significant (α=0.05) |
|---------|-------------------|-------------------|-------------|-------------|-------------|---------|----------------------|
| Work_Hours | 1.96 (2.55) | 5.53 (3.22) | 23 | 58 | -4.759 | <0.0001 | **Yes** |
| Study_Hours | 5.49 (3.23) | 3.69 (2.33) | 23 | 58 | 2.813 | 0.0062 | **Yes** |
| Mood_Rating | 3.04 (1.43) | 3.17 (1.45) | 23 | 58 | -0.362 | 0.7185 | No |
| Sleep_Hours | 6.70 (2.45) | 6.15 (2.77) | 23 | 58 | 1.291 | 0.2006 | No |
| Focus_Rating | 2.65 (1.50) | 3.05 (1.53) | 23 | 58 | -1.349 | 0.1811 | No |

**Key Findings**:

1. **Work_Hours**: Highly significant difference (t = -4.759, p < 0.0001). Weekday work hours (M = 5.53, SD = 3.22) are significantly higher than weekend work hours (M = 1.96, SD = 2.55), confirming expected work schedule patterns.

2. **Study_Hours**: Significant difference (t = 2.813, p = 0.0062). Weekend study hours (M = 5.49, SD = 3.23) are significantly higher than weekday study hours (M = 3.69, SD = 2.33), suggesting weekend study sessions compensate for weekday work obligations.

3. **Mood_Rating**: No significant difference (t = -0.362, p = 0.7185). Weekend mood (M = 3.04, SD = 1.43) and weekday mood (M = 3.17, SD = 1.45) do not differ significantly.

4. **Sleep_Hours**: No significant difference (t = 1.291, p = 0.2006). Weekend sleep (M = 6.70, SD = 2.45) and weekday sleep (M = 6.15, SD = 2.77) do not differ significantly, though weekend sleep is slightly higher.

5. **Focus_Rating**: No significant difference (t = -1.349, p = 0.1811). Weekend focus (M = 2.65, SD = 1.50) and weekday focus (M = 3.05, SD = 1.53) do not differ significantly, though weekday focus is slightly higher.

### 4.5.2 Chi-Square Tests of Independence

Chi-square tests were performed to examine associations between categorical variables. Table IV presents the results.

**TABLE IV**  
**CHI-SQUARE TEST RESULTS**

| Test | Variable 1 | Variable 2 | χ² statistic | df | p-value | Significant (α=0.05) |
|------|-------------|------------|--------------|----|---------|----------------------|
| Test 1 | Work/Study Profile | Is_Weekend | 1.984 | 1 | 0.1589 | No |
| Test 2 | Weekend | High Volume | 19.794 | 1 | <0.0001 | **Yes** |

**Key Findings**:

1. **Work/Study Profile × Is_Weekend**: No significant association (χ² = 1.984, df = 1, p = 0.1589). Work/Study profiles do not significantly differ between weekends and weekdays, though 34.8% of weekend days showed work/study profiles.

2. **Weekend × High Volume**: Highly significant association (χ² = 19.794, df = 1, p < 0.0001). High-volume days (high work/study hours) are significantly associated with weekday status, confirming that intensive work/study occurs primarily on weekdays.

---

## 4.6 Hypothesis Testing Results

### 4.6.1 Hypothesis 5.1: Recovery vs. Inertia

**Research Question**: Do "Rest Days" (low work/study, high distraction) typically precede "Deep Work Days" (high work/study, low distraction), or do they precede further low-performance patterns (suggesting inertia)?

**Operational Definitions**:
- **Rest Day**: (Work_Hours + Study_Hours) < median AND Distraction_Time_Mins ≥ median
- **Deep Work Day**: (Work_Hours + Study_Hours) ≥ median AND Distraction_Time_Mins < median

**Results**: 

A total of **8 Rest Days** were identified in the dataset. Transitions from Rest Days to the next day were analyzed:

- **Rest → Deep Work**: 0 transitions (0.0%)
- **Rest → Low Performance**: 3 transitions (37.5%)
- **Rest → Other**: 5 transitions (62.5%)

**Conclusion**: The **inertia pattern dominates**. No recovery transitions (Rest → Deep Work) were observed under the strict criteria used. Instead, Rest Days primarily transition to other patterns (62.5%) or low-performance patterns (37.5%), suggesting that rest days do not consistently precede productive deep work days.

**Interpretation**: This finding suggests that rest days may lead to continued low performance rather than serving as recovery mechanisms that enable subsequent high productivity. The absence of Rest → Deep Work transitions indicates that recovery patterns, if they exist, may require different operational definitions or longer time horizons than single-day transitions.

### 4.6.2 Hypothesis 5.2: Busy vs. Productive Distinction

**Research Question**: Can data analysis distinguish between "High-Volume / Low-Focus" days (Busywork) and "High-Volume / High-Focus" days (Flow State) based on the relationship between Work_Hours and Distraction_Time?

**Operational Definitions**:
- **High-Volume Day**: (Work_Hours + Study_Hours) ≥ median
- **Busywork**: High-volume AND Focus_Rating < median
- **Flow State**: High-volume AND Focus_Rating ≥ median

**Results**:

A total of **44 high-volume days** were identified. These were classified as:
- **Busywork days**: 15 (34.1%)
- **Flow State days**: 29 (65.9%)

**Statistical Test**: Independent samples t-test comparing Focus_Rating between Busywork and Flow State groups.

**TABLE V**  
**BUSY VS. PRODUCTIVE DISTINCTION: t-TEST RESULTS**

| Group | n | Mean Focus_Rating | SD | t-statistic | p-value | Significant (α=0.05) |
|-------|---|-------------------|----|-------------|---------|----------------------|
| Busywork | 15 | 1.73 | 0.80 | -9.820 | <0.0001 | **Yes** |
| Flow State | 29 | 3.93 | 0.96 | | | |

**Conclusion**: The distinction between Busywork and Flow State is **highly statistically significant** (t = -9.820, p < 0.0001). Busywork days show significantly lower focus ratings (M = 1.73) compared to Flow State days (M = 3.93), confirming that high-volume days can be meaningfully distinguished by focus levels.

**Interpretation**: This finding validates the operational distinction between busywork (high volume, low focus) and flow state (high volume, high focus). The large effect size (mean difference of 2.20 points on a 5-point scale) indicates that focus rating is a robust discriminator between these productivity types, supporting the hypothesis that not all high-volume days are equally productive.

### 4.6.3 Hypothesis 5.3: Weekend Bleed Effect

**Research Question**: Do specific habit patterns strictly align with calendar weekends, or do "Work/Study" patterns significantly intrude into weekends, and is this intrusion associated with "Low Mood" outcomes?

**Operational Definitions**:
- **Work/Study Profile**: (Work_Hours + Study_Hours) ≥ median
- **Weekend Bleed**: Work/Study Profile occurring on weekend days

**Results**:

**Weekend Work/Study Intrusion**: 
- Total weekend days: 23
- Weekend days with Work/Study profiles: 8 (34.8%)
- Weekend days without Work/Study profiles: 15 (65.2%)

**Mood Comparisons**:
- **Weekend Bleed Mood**: M = 3.50 (SD = 1.41)
- **Weekend Rest Mood**: M = 2.80 (SD = 1.42)

**Statistical Test**: Chi-square test of independence (Work/Study Profile × Is_Weekend)

**TABLE VI**  
**WEEKEND BLEED EFFECT: CHI-SQUARE TEST RESULTS**

| Test | χ² statistic | df | p-value | Significant (α=0.05) |
|------|--------------|----|---------|----------------------|
| Work/Study Profile × Is_Weekend | 1.984 | 1 | 0.1589 | No |

**Conclusion**: 

1. **Work/Study Intrusion**: Work/Study profiles do intrude into weekends (34.8% of weekend days), confirming that work/study patterns do not strictly align with calendar weekends.

2. **Statistical Association**: The chi-square test shows **no significant association** (χ² = 1.984, df = 1, p = 0.1589) between Work/Study Profile and Weekend status, indicating that work/study patterns occur similarly on weekends and weekdays.

3. **Mood Effect**: Weekend Bleed days show slightly higher mood (M = 3.50) compared to Weekend Rest days (M = 2.80), though this difference was not statistically tested due to small sample sizes.

**Interpretation**: The "Weekend Bleed" effect is observed (34.8% intrusion rate), but it is not statistically associated with weekend status. This suggests that work/study patterns occur naturally on weekends as part of the participant's routine rather than as an exceptional intrusion. The slightly higher mood on Weekend Bleed days contradicts the hypothesis that weekend work/study intrusion is associated with lower mood, though formal statistical testing would be needed to confirm this relationship.

---

## 4.7 Summary of Key Findings

### 4.7.1 Descriptive Patterns

1. **Sleep**: Mean of 6.30 hours with high variability (0-12 hours), indicating inconsistent sleep patterns.
2. **Productivity**: Work hours (M = 4.52) and study hours (M = 4.20) show substantial day-to-day variation.
3. **Well-being**: Mood (M = 3.14) and Focus (M = 2.93) ratings indicate moderate levels with room for improvement.
4. **Distraction**: Mean distraction time of 219 minutes (3.66 hours) suggests significant digital consumption.

### 4.7.2 Temporal Patterns

1. **Weekend vs. Weekday**: Work hours significantly lower on weekends; study hours significantly higher on weekends.
2. **Weekly Cycles**: Clear weekly patterns observed, with work concentrated on weekdays and study more evenly distributed.
3. **Mood and Focus**: Show cyclical patterns but no significant weekend vs. weekday differences.

### 4.7.3 Relationships

1. **Strongest Correlation**: Mood and Focus show strong positive relationship (r = 0.621).
2. **Sleep Relationships**: Sleep correlates moderately with distraction, mood, and focus.
3. **Productivity Relationships**: Work hours correlate moderately with tasks completed.
4. **Travel Relationships**: Commute time correlates moderately with mood and focus.

### 4.7.4 Hypothesis Testing Conclusions

1. **Recovery vs. Inertia**: Inertia pattern dominates; rest days do not consistently precede deep work days.
2. **Busy vs. Productive**: Highly significant distinction validated; focus rating robustly discriminates between busywork and flow state.
3. **Weekend Bleed**: Work/study patterns intrude into weekends (34.8%) but are not statistically associated with weekend status or lower mood.

---

## 4.8 Figures and Tables Summary

**Figures Generated**:
- **Figure 1**: Histograms of All Numerical Variables
- **Figure 2**: Time Series Trends Over 81-Day Period
- **Figure 3**: Correlation Matrix Heatmap
- **Figure 4**: Box Plots Showing Distributions and Outliers
- **Figure 5**: Weekly Trend Analysis
- **Figure 6**: Statistical Correlation Matrix

**Tables Generated**:
- **Table I**: Descriptive Statistics for Numerical Variables
- **Table II**: Significant Correlations (p < 0.05)
- **Table III**: Independent Samples t-Test Results: Weekend vs. Weekday
- **Table IV**: Chi-Square Test Results
- **Table V**: Busy vs. Productive Distinction: t-Test Results
- **Table VI**: Weekend Bleed Effect: Chi-Square Test Results

All figures are saved at 300 DPI resolution suitable for IEEE publication format. All statistical tests were performed at α = 0.05 significance level.
