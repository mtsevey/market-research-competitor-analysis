import pandas as pd
import matplotlib
matplotlib.use('Agg')  # use non-interactive backend
import matplotlib.pyplot as plt

# Load dataset
file_path = 'us_streaming_market_share.csv'
df = pd.read_csv(file_path)

# Rank platforms by market share
# Highest market share gets rank 1
# Use descending order
df['Rank'] = df['MarketShare'].rank(method='first', ascending=False).astype(int)

# Compute difference from top competitor
top_share = df['MarketShare'].max()
df['Difference_from_Top'] = top_share - df['MarketShare']

# Save summary sorted by rank
summary = df.sort_values('Rank')
summary.to_csv('market_share_summary.csv', index=False)

# Plot bar chart
plt.figure(figsize=(10, 6))
plt.bar(summary['Platform'], summary['MarketShare'], color='skyblue')
plt.title('U.S. Streaming Services Market Share (2025)')
plt.xlabel('Platform')
plt.ylabel('Market Share (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('us_streaming_market_share_bar.png')

# Create pie chart (optional)
plt.figure(figsize=(8, 8))
plt.pie(summary['MarketShare'], labels=summary['Platform'], autopct='%1.1f%%', startangle=140)
plt.title('Market Share Distribution of U.S. Streaming Services')
plt.tight_layout()
plt.savefig('us_streaming_market_share_pie.png')
