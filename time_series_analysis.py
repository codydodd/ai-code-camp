import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Simulate monthly CX survey scores (e.g., satisfaction scores from 1–10)
np.random.seed(42)
dates = pd.date_range(start="2022-01-01", periods=24, freq="M")
scores = np.random.normal(loc=7.5, scale=0.8, size=len(dates)).clip(1, 10)

# Create DataFrame
df = pd.DataFrame({"Date": dates, "CX_Score": scores})
df.set_index("Date", inplace=True)

# Plot the time series
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["CX_Score"], marker="o", linestyle="-", color="teal")
plt.title("Monthly CX Survey Scores")
plt.xlabel("Date")
plt.ylabel("Average Score (1–10)")
plt.grid(True)
plt.tight_layout()
plt.show()


## Advanced - find trends
#-------------------------
# Convert dates to ordinal for regression
x = df.index.map(pd.Timestamp.toordinal).values
y = df["CX_Score"].values

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
line = slope * x + intercept

# Plot original data and regression line
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["CX_Score"], marker="o", label="CX Score", color="teal")
plt.plot(df.index, line, label="Trend Line", color="orange", linestyle="--")
plt.title("CX Survey Scores with Trend Line")
plt.xlabel("Date")
plt.ylabel("Average Score (1–10)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Print regression stats
print(f"Slope: {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
print(f"R-squared: {r_value**2:.4f}")
print(f"P-value: {p_value:.4f}")

# Classify trend
if p_value < 0.05:
    if slope > 0:
        trend = "Significant upward trend"
    elif slope < 0:
        trend = "Significant downward trend"
    else:
        trend = "No trend"
else:
    trend = "No significant trend"

print(f"Trend classification: {trend}")