# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pandas",
#     "plotly",
# ]
# ///

import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Define the color palette (matches your cpalette)
cpalette = ['#bdc9e1', '#74a9cf', '#2b8cbe', '#045a8d']

# Filtering and selecting
edu = (
    # 1. Load Data
    pd.read_csv("/private/tmp/education_oecd.csv")
    # 2. Data Wrangling (The dplyr/tidyr equivalent)
    .query("ISC11A in ['L5', 'L6', 'L7', 'L8']")
    .query("Measure == 'Value'")
    .query("SEX == 'T'")
    [['country_code', 'ISC11A', 'Value']]
    # Pivot (spread) and handle missing values
    .pivot(index='country_code', columns='ISC11A', values='Value')
    .reset_index()
)

# Fill NaNs and round (mutate)
cols = ['L5', 'L6', 'L7', 'L8']
for col in cols:
    if col in edu.columns:
        edu[col] = edu[col].fillna(0.0).round(1)
    else:
        edu[col] = 0.0

# Arrange by L7 descending
edu = edu.sort_values(by='L5', ascending=False)
cpalette = ['#bdc9e1', '#74a9cf', '#2b8cbe', '#045a8d']
# 3. Create Plotly Visualization
fig = go.Figure()

# Add Short-cycle (L5)
fig.add_trace(go.Bar(
    x=edu['country_code'],
    y=edu['L5'],
    name="Short-cycle",
    marker_color=cpalette[0]
))

# Add Bachelor's (L6)
fig.add_trace(go.Bar(
    x=edu['country_code'],
    y=edu['L6'],
    name="Bachelor's",
    marker_color=cpalette[1]
))

# Add Master's (L7)
fig.add_trace(go.Bar(
    x=edu['country_code'],
    y=edu['L7'],
    name="Master's",
    marker_color=cpalette[2]
))

# Add Doctoral (L8)
fig.add_trace(go.Bar(
    x=edu['country_code'],
    y=edu['L8'],
    name="Doctoral",
    marker_color=cpalette[3]
))


# Set layout for stacked bar chart
fig.update_layout(
    barmode='stack',
    xaxis={'type': 'category'} # Ensures order matches the sorted dataframe
)

# 4. Export to JSON
# Replicating plotly_build(p)$x[c("data", "layout")]
chart_dict = {
    "data": fig.to_dict()["data"],
    "layout": fig.to_dict()["layout"]
}

output_path = "../assets/tertiary_education.json"
pio.write_json(fig, output_path)
