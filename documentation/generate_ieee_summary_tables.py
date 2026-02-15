"""
Script to generate summary tables for IEEE Data Science Paper
Run this after executing all notebooks to compile statistical results
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import ttest_ind, chi2_contingency

# Load data
df = pd.read_csv('data/cleaned_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

if 'Is_Weekend' not in df.columns:
    df['Is_Weekend'] = df['Date'].dt.dayofweek.isin([5, 6])

# Load hypothesis analysis data if available
try:
    df_hypothesis = pd.read_csv('data/data_with_hypothesis_analysis.csv')
    df_hypothesis['Date'] = pd.to_datetime(df_hypothesis['Date'])
except:
    df_hypothesis = df.copy()
    print("Warning: data_with_hypothesis_analysis.csv not found. Using cleaned_data.csv")

print("="*80)
print("GENERATING IEEE SUMMARY TABLES")
print("="*80)

# ============================================================================
# TABLE 1: Descriptive Statistics Summary
# ============================================================================
print("\n[TABLE 1] Descriptive Statistics")
print("-"*80)

desc_stats = df.describe()
desc_stats.loc['range'] = desc_stats.loc['max'] - desc_stats.loc['min']

# Select key variables for paper
key_vars = ['Sleep_Hours', 'Work_Hours', 'Study_Hours', 'Travel Time (Hours)', 
            'Distraction_Time_Mins', 'Tasks_Completed', 'Mood_Rating', 'Focus_Rating']

table1 = desc_stats[key_vars].T[['mean', 'std', 'min', 'max', 'range']]
table1.columns = ['Mean', 'Std Dev', 'Min', 'Max', 'Range']
table1.index.name = 'Variable'

print(table1.to_string())
table1.to_csv('data/ieee_table1_descriptive_statistics.csv')
print("\n✓ Saved to: data/ieee_table1_descriptive_statistics.csv")

# ============================================================================
# TABLE 2: Statistical Test Results Summary
# ============================================================================
print("\n[TABLE 2] Statistical Test Results Summary")
print("-"*80)

test_results = []

# T-test: Work_Hours (Weekend vs Weekday)
weekend_work = df[df['Is_Weekend']]['Work_Hours'].dropna()
weekday_work = df[~df['Is_Weekend']]['Work_Hours'].dropna()
if len(weekend_work) > 0 and len(weekday_work) > 0:
    t_stat, p_val = ttest_ind(weekend_work, weekday_work)
    test_results.append({
        'Test': 'Independent Samples t-test',
        'Variable': 'Work_Hours',
        'Group 1': f'Weekend (n={len(weekend_work)})',
        'Group 2': f'Weekday (n={len(weekday_work)})',
        'Mean 1': f'{weekend_work.mean():.2f}',
        'Mean 2': f'{weekday_work.mean():.2f}',
        't-statistic': f'{t_stat:.3f}',
        'p-value': f'{p_val:.4f}',
        'df': len(weekend_work) + len(weekday_work) - 2,
        'Significant': 'Yes' if p_val < 0.05 else 'No'
    })

# T-test: Study_Hours (Weekend vs Weekday)
weekend_study = df[df['Is_Weekend']]['Study_Hours'].dropna()
weekday_study = df[~df['Is_Weekend']]['Study_Hours'].dropna()
if len(weekend_study) > 0 and len(weekday_study) > 0:
    t_stat, p_val = ttest_ind(weekend_study, weekday_study)
    test_results.append({
        'Test': 'Independent Samples t-test',
        'Variable': 'Study_Hours',
        'Group 1': f'Weekend (n={len(weekend_study)})',
        'Group 2': f'Weekday (n={len(weekday_study)})',
        'Mean 1': f'{weekend_study.mean():.2f}',
        'Mean 2': f'{weekday_study.mean():.2f}',
        't-statistic': f'{t_stat:.3f}',
        'p-value': f'{p_val:.4f}',
        'df': len(weekend_study) + len(weekday_study) - 2,
        'Significant': 'Yes' if p_val < 0.05 else 'No'
    })

# T-test: Mood_Rating (Weekend vs Weekday)
weekend_mood = df[df['Is_Weekend']]['Mood_Rating'].dropna()
weekday_mood = df[~df['Is_Weekend']]['Mood_Rating'].dropna()
if len(weekend_mood) > 0 and len(weekday_mood) > 0:
    t_stat, p_val = ttest_ind(weekend_mood, weekday_mood)
    test_results.append({
        'Test': 'Independent Samples t-test',
        'Variable': 'Mood_Rating',
        'Group 1': f'Weekend (n={len(weekend_mood)})',
        'Group 2': f'Weekday (n={len(weekday_mood)})',
        'Mean 1': f'{weekend_mood.mean():.2f}',
        'Mean 2': f'{weekday_mood.mean():.2f}',
        't-statistic': f'{t_stat:.3f}',
        'p-value': f'{p_val:.4f}',
        'df': len(weekend_mood) + len(weekday_mood) - 2,
        'Significant': 'Yes' if p_val < 0.05 else 'No'
    })

# T-test: Sleep_Hours (Weekend vs Weekday)
weekend_sleep = df[df['Is_Weekend']]['Sleep_Hours'].dropna()
weekday_sleep = df[~df['Is_Weekend']]['Sleep_Hours'].dropna()
if len(weekend_sleep) > 0 and len(weekday_sleep) > 0:
    t_stat, p_val = ttest_ind(weekend_sleep, weekday_sleep)
    test_results.append({
        'Test': 'Independent Samples t-test',
        'Variable': 'Sleep_Hours',
        'Group 1': f'Weekend (n={len(weekend_sleep)})',
        'Group 2': f'Weekday (n={len(weekday_sleep)})',
        'Mean 1': f'{weekend_sleep.mean():.2f}',
        'Mean 2': f'{weekday_sleep.mean():.2f}',
        't-statistic': f'{t_stat:.3f}',
        'p-value': f'{p_val:.4f}',
        'df': len(weekend_sleep) + len(weekday_sleep) - 2,
        'Significant': 'Yes' if p_val < 0.05 else 'No'
    })

# T-test: Focus_Rating (Weekend vs Weekday)
weekend_focus = df[df['Is_Weekend']]['Focus_Rating'].dropna()
weekday_focus = df[~df['Is_Weekend']]['Focus_Rating'].dropna()
if len(weekend_focus) > 0 and len(weekday_focus) > 0:
    t_stat, p_val = ttest_ind(weekend_focus, weekday_focus)
    test_results.append({
        'Test': 'Independent Samples t-test',
        'Variable': 'Focus_Rating',
        'Group 1': f'Weekend (n={len(weekend_focus)})',
        'Group 2': f'Weekday (n={len(weekday_focus)})',
        'Mean 1': f'{weekend_focus.mean():.2f}',
        'Mean 2': f'{weekday_focus.mean():.2f}',
        't-statistic': f'{t_stat:.3f}',
        'p-value': f'{p_val:.4f}',
        'df': len(weekend_focus) + len(weekday_focus) - 2,
        'Significant': 'Yes' if p_val < 0.05 else 'No'
    })

# Chi-square: Work/Study Profile × Weekend
if 'Work_Study_Profile' in df_hypothesis.columns:
    crosstab = pd.crosstab(df_hypothesis['Work_Study_Profile'], df_hypothesis['Is_Weekend'])
    chi2, p_val, dof, expected = chi2_contingency(crosstab)
    test_results.append({
        'Test': 'Chi-square test',
        'Variable': 'Work/Study Profile × Weekend',
        'Group 1': 'Work/Study Profile',
        'Group 2': 'Is_Weekend',
        'Mean 1': '-',
        'Mean 2': '-',
        't-statistic': f'{chi2:.3f}',
        'p-value': f'{p_val:.4f}',
        'df': dof,
        'Significant': 'Yes' if p_val < 0.05 else 'No'
    })

table2 = pd.DataFrame(test_results)
print(table2.to_string(index=False))
table2.to_csv('data/ieee_table2_statistical_tests.csv', index=False)
print("\n✓ Saved to: data/ieee_table2_statistical_tests.csv")

# ============================================================================
# TABLE 3: Hypothesis Testing Results Summary
# ============================================================================
print("\n[TABLE 3] Hypothesis Testing Results Summary")
print("-"*80)

hypothesis_results = []

# Hypothesis 5.1: Recovery vs. Inertia
try:
    transitions_df = pd.read_csv('data/recovery_inertia_transitions.csv')
    if len(transitions_df) > 0:
        rest_to_deep_work = (transitions_df['Next_Day_Type'] == 'Deep Work').sum()
        rest_to_low_perf = (transitions_df['Next_Day_Type'] == 'Low Performance').sum()
        rest_to_other = len(transitions_df) - rest_to_deep_work - rest_to_low_perf
        
        recovery_rate = rest_to_deep_work / len(transitions_df) * 100
        inertia_rate = rest_to_low_perf / len(transitions_df) * 100
        
        hypothesis_results.append({
            'Hypothesis': '5.1: Recovery vs. Inertia',
            'Test Type': 'Transition Analysis',
            'Result': f'Rest → Deep Work: {recovery_rate:.1f}% ({rest_to_deep_work}/{len(transitions_df)}), Rest → Low Performance: {inertia_rate:.1f}% ({rest_to_low_perf}/{len(transitions_df)})',
            'Conclusion': 'Inertia pattern dominates' if inertia_rate > recovery_rate else 'Recovery pattern dominates',
            'Statistical Test': '-',
            'Test Statistic': '-',
            'p-value': '-',
            'Significant': '-'
        })
except:
    hypothesis_results.append({
        'Hypothesis': '5.1: Recovery vs. Inertia',
        'Test Type': 'Transition Analysis',
        'Result': 'Data not available - run hypothesis_testing notebook',
        'Conclusion': 'Pending',
        'Statistical Test': '-',
        'Test Statistic': '-',
        'p-value': '-',
        'Significant': '-'
    })

# Hypothesis 5.2: Busy vs. Productive
if 'Productivity_Type' in df_hypothesis.columns:
    high_volume = df_hypothesis[(df_hypothesis['Work_Hours'] + df_hypothesis['Study_Hours']) >= 
                                (df_hypothesis['Work_Hours'] + df_hypothesis['Study_Hours']).median()]
    
    busywork = high_volume[high_volume['Productivity_Type'] == 'Busywork (High Volume, Low Focus)']['Focus_Rating']
    flow_state = high_volume[high_volume['Productivity_Type'] == 'Flow State (High Volume, High Focus)']['Focus_Rating']
    
    if len(busywork) > 0 and len(flow_state) > 0:
        t_stat, p_val = ttest_ind(busywork, flow_state)
        hypothesis_results.append({
            'Hypothesis': '5.2: Busy vs. Productive',
            'Test Type': 'Independent Samples t-test',
            'Result': f'Busywork: {busywork.mean():.2f} (n={len(busywork)}), Flow State: {flow_state.mean():.2f} (n={len(flow_state)})',
            'Conclusion': 'Significant difference in Focus_Rating between groups',
            'Statistical Test': 't-test (Focus_Rating)',
            'Test Statistic': f'{t_stat:.3f}',
            'p-value': f'{p_val:.4f}',
            'Significant': 'Yes' if p_val < 0.05 else 'No'
        })
else:
    hypothesis_results.append({
        'Hypothesis': '5.2: Busy vs. Productive',
        'Test Type': 'Independent Samples t-test',
        'Result': 'Data not available - run hypothesis_testing notebook',
        'Conclusion': 'Pending',
        'Statistical Test': '-',
        'Test Statistic': '-',
        'p-value': '-',
        'Significant': '-'
    })

# Hypothesis 5.3: Weekend Bleed
if 'Work_Study_Profile' in df_hypothesis.columns:
    crosstab = pd.crosstab(df_hypothesis['Work_Study_Profile'], df_hypothesis['Is_Weekend'])
    chi2, p_val, dof, expected = chi2_contingency(crosstab)
    
    weekend_work_study = df_hypothesis[df_hypothesis['Is_Weekend'] & df_hypothesis['Work_Study_Profile']]
    weekend_rest = df_hypothesis[df_hypothesis['Is_Weekend'] & ~df_hypothesis['Work_Study_Profile']]
    
    if len(weekend_work_study) > 0 and len(weekend_rest) > 0:
        hypothesis_results.append({
            'Hypothesis': '5.3: Weekend Bleed Effect',
            'Test Type': 'Chi-square test',
            'Result': f'Weekend Work/Study: {len(weekend_work_study)}/{df_hypothesis["Is_Weekend"].sum()} ({len(weekend_work_study)/df_hypothesis["Is_Weekend"].sum()*100:.1f}%), Mood: Work/Study={weekend_work_study["Mood_Rating"].mean():.2f}, Rest={weekend_rest["Mood_Rating"].mean():.2f}',
            'Conclusion': 'Weekend bleed observed' if len(weekend_work_study) > 0 else 'No weekend bleed',
            'Statistical Test': 'Chi-square',
            'Test Statistic': f'{chi2:.3f}',
            'p-value': f'{p_val:.4f}',
            'Significant': 'Yes' if p_val < 0.05 else 'No'
        })
else:
    hypothesis_results.append({
        'Hypothesis': '5.3: Weekend Bleed Effect',
        'Test Type': 'Chi-square test',
        'Result': 'Data not available - run hypothesis_testing notebook',
        'Conclusion': 'Pending',
        'Statistical Test': '-',
        'Test Statistic': '-',
        'p-value': '-',
        'Significant': '-'
    })

table3 = pd.DataFrame(hypothesis_results)
print(table3.to_string(index=False))
table3.to_csv('data/ieee_table3_hypothesis_results.csv', index=False)
print("\n✓ Saved to: data/ieee_table3_hypothesis_results.csv")

# ============================================================================
# TABLE 4: Significant Correlations Summary
# ============================================================================
print("\n[TABLE 4] Significant Correlations (p < 0.05)")
print("-"*80)

correlations = []
numeric_cols = ['Sleep_Hours', 'Work_Hours', 'Study_Hours', 'Travel Time (Hours)', 
                'Distraction_Time_Mins', 'Tasks_Completed', 'Mood_Rating', 'Focus_Rating']

for i, col1 in enumerate(numeric_cols):
    for col2 in numeric_cols[i+1:]:
        if col1 in df.columns and col2 in df.columns:
            corr_data = df[[col1, col2]].dropna()
            if len(corr_data) > 2:
                corr_coef, p_val = stats.pearsonr(corr_data[col1], corr_data[col2])
                if p_val < 0.05:
                    correlations.append({
                        'Variable 1': col1,
                        'Variable 2': col2,
                        'Correlation': f'{corr_coef:.3f}',
                        'p-value': f'{p_val:.4f}',
                        'Interpretation': 'Strong' if abs(corr_coef) > 0.7 else 'Moderate' if abs(corr_coef) > 0.4 else 'Weak'
                    })

if correlations:
    table4 = pd.DataFrame(correlations)
    print(table4.to_string(index=False))
    table4.to_csv('data/ieee_table4_significant_correlations.csv', index=False)
    print("\n✓ Saved to: data/ieee_table4_significant_correlations.csv")
else:
    print("No significant correlations found (p < 0.05)")

print("\n" + "="*80)
print("SUMMARY TABLES GENERATION COMPLETE")
print("="*80)
print("\nGenerated files:")
print("  1. data/ieee_table1_descriptive_statistics.csv")
print("  2. data/ieee_table2_statistical_tests.csv")
print("  3. data/ieee_table3_hypothesis_results.csv")
print("  4. data/ieee_table4_significant_correlations.csv")
print("\nThese tables can be formatted for inclusion in your IEEE paper.")
