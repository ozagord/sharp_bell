# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "numpy",
#     "pandas",
#     "plotly",
#     "scipy",
# ]
# ///
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from scipy.optimize import curve_fit

# 1. Filter out USA and ZAF
# Equivalent to: filter(!(country_code %in% c('USA', 'ZAF')))
life_exp_spending = (
    pd.read_csv("src/assets/life_exp_spending.csv")
    .query("country_code not in ['USA', 'ZAF']")
    .sort_values("health_spending_USD_ppp")
)

# 2. Define the non-linear model function
# In Python, the independent variable (x) must be the first argument
def model_func(x, le_max, a, b):
    return le_max * (1 - np.exp(a - b * x))

# 3. Fit the non-linear model
# start = list(...) maps to p0=[le_max, a, b]
x_data = life_exp_spending["health_spending_USD_ppp"]
y_data = life_exp_spending["life_expectancy"]

popt, pcov = curve_fit(f=model_func, xdata=x_data, ydata=y_data, p0=[80, 10, 0.001])

# Extract fitted parameters
le_max_fit, a_fit, b_fit = popt

# 4. Generate predictions and residuals
# Predict using the fitted parameters
life_exp_spending["fit"] = model_func(x_data, le_max_fit, a_fit, b_fit)

# Residuals = Observed - Predicted
life_exp_spending["residuals"] = np.round(
    life_exp_spending["life_expectancy"] - life_exp_spending["fit"], 1
)


# 5. Create the Plotly visualization
fig = go.Figure()

# Add observed scatter trace
fig.add_trace(
    go.Scatter(
        x=life_exp_spending["health_spending_USD_ppp"],
        y=life_exp_spending["life_expectancy"],
        mode="markers",
        name="observed",
        text=life_exp_spending["country"],
        hovertemplate="<b>%{text}</b><br>Spending: %{x}<br>Expectancy: %{y}<extra></extra>",
    )
)

# Add predicted line trace
fig.add_trace(
    go.Scatter(
        x=life_exp_spending["health_spending_USD_ppp"],
        y=life_exp_spending["fit"],
        mode="lines",
        name="predicted",
    )
)

# Layout adjustments
fig.update_layout(
    title="Health spending per capita and life expectancy at birth, 2015 (or nearest year)",
    xaxis=dict(title="Health spending per capita (USD at PPP)", zeroline=False),
    yaxis=dict(title="Life expectancy at birth (years)"),
)


output_path = "src/assets/healthcare_spending_2.json"
pio.write_json(fig, output_path)
