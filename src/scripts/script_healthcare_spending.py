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

# 1. Read and sort the data
# (Equivalent to read_csv %>% arrange)
life_exp_spending = (
    pd.read_csv("src/assets/life_exp_spending.csv")
    .sort_values("health_spending_USD_ppp")
)

# 2. Create the Plotly figure
# (Equivalent to plot_ly(..., type='scatter', mode='markers'))
fig = px.scatter(
    life_exp_spending,
    x="health_spending_USD_ppp",
    y="life_expectancy",
    hover_name="country",  # 'text = ~country' maps to hover information
    title="Health spending per capita and life expectancy at birth, 2015 (or nearest year)",
)

# 3. Update layout and axis labels
# (Equivalent to layout(...))
fig.update_layout(
    xaxis=dict(title="Health spending per capita (USD at PPP)", zeroline=False),
    yaxis=dict(title="Life expectancy at birth (years)"),
)

output_path = "src/assets/healthcare_spending.json"
pio.write_json(fig, output_path)
