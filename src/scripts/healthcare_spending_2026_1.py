# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pandas",
#     "plotly",
# ]
# ///
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Load processed data
df = pd.read_csv("src/assets/data/health_data_2026.csv")

# Get latest available data per country
df_latest = df.sort_values("Year").groupby("Code").last().reset_index()
latest_year = df["Year"].max()

# Plot 1: Life Expectancy vs Health Spending (Interactive Scatter)
fig = px.scatter(
    df_latest,
    x="Health_Spending",
    y="Life_Expectancy",
    hover_name="Country",
    title=f"Life Expectancy vs Health Spending per Capita (Latest data up to {latest_year})",
)

# Update layout and axis labels
# (Equivalent to layout(...))
fig.update_layout(
    xaxis=dict(title="Health spending per capita (USD at PPP)", zeroline=False),
    yaxis=dict(title="Life expectancy at birth (years)"),
    font_color="#0055FF",
    title_font_color="#0055FF",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)
fig.update_traces(marker=dict(color='#FF5500', size=12))
output_path = "src/assets/healthcare_spending_2026_1.json"
pio.write_json(fig, output_path)
