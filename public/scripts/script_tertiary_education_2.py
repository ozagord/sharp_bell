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

# 1. Creazione del DataFrame con Pandas
data = pd.DataFrame({
    'age_groups': ["55-64", "45-54", "35-44", "25-34"],
    'Italy': [12.4, 14.0, 20.5, 25.6],
    'OECD': [26.5, 32.1, 40.5, 43.1]
}).sort_values(by="Italy", ascending=False)

# 2. Inizializzazione della figura con la prima traccia (Italy)
fig = go.Figure(
    data=[
        go.Bar(
            x=data['age_groups'],
            y=data['Italy'],
            name='Italy',
            marker=dict(color='#bdc9e1')
        )
    ]
)

# 3. Aggiunta della seconda traccia (OECD) equivalente ad add_trace()
fig.add_trace(
    go.Bar(
        x=data['age_groups'],
        y=data['OECD'],
        name='OECD',
        marker=dict(color='#74a9cf')
    )
)

# 4. Configurazione del Layout (Titoli, Assi e Barmode)
fig.update_layout(
    title="Tertiary education by age group",
    xaxis=dict(title=''),  # Rimosso il titolo come nel tuo script R originale
    yaxis=dict(title='percentage in same age group (2016)'),
    barmode='group'        # Barre affiancate raggruppate
)

# Se vuoi visualizzarlo localmente nel notebook:
# fig.show()

# Se vuoi esportarlo in JSON per il tuo blog Astro:

pio.write_json(fig, "/Users/ozagordi/Projects/vaults/sharp_bell/src/assets/italy_data_by_age_group.json")