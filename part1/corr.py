import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('../data/SpeedDatingData.csv',  encoding='latin1')


data.drop(['iid', 'field', 'undergra', 'mn_sat', 'tuition', 'from', 'zipcode', 'income',
       'career'], axis = 1, inplace = True)
"""
corr_matrix = data.corr(method='spearman')
threshold = 0.7
corr_pairs = corr_matrix.abs().unstack()
corr_pairs = corr_pairs[corr_pairs < 1.0]  # Exclude self-correlation
strong_pairs = corr_pairs[corr_pairs > threshold].drop_duplicates()
strong_features = set(strong_pairs.index.get_level_values(0)) | set(strong_pairs.index.get_level_values(1))
strong_features = list(strong_features)
filtered_corr = corr_matrix.loc[strong_features, strong_features]

plt.figure(figsize=(40, 40))
ax = sns.heatmap(filtered_corr, annot=True, fmt=".2f", cmap='coolwarm', center=0)

# Rotate axis labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='center', fontsize = 35)  # pionowo
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, va='center', fontsize = 35)   # poziomo

plt.title('Spearman Correlation Heatmap')
plt.savefig("plots/corr_08.png")
plt.show()

"""

target = 'match'

# Oblicz korelacje Spearmana względem targetu
corr_with_target = data.corr(method='spearman')[target].dropna()

# Posortuj według wartości bezwzględnej i wybierz top N (pomijając samego siebie)
top_corr = corr_with_target.drop(target).abs().sort_values(ascending=False).head(40)
top_corr_signed = corr_with_target[top_corr.index]  # Z zachowaniem znaku korelacji

# Wykres słupkowy
plt.figure(figsize=(10, 6))
sns.barplot(x=top_corr_signed.values, y=top_corr_signed.index, palette='coolwarm', orient='h')
plt.title(f'Top 20 Features Most Correlated with "{target}" (Spearman)', fontsize=16)
plt.xlabel('Spearman Correlation')
plt.ylabel('Feature')
plt.xlim(-1, 1)
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("plots/bar_corr_target.png")
plt.show()