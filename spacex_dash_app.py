"""Interactive SpaceX launch dashboard for the IBM capstone project.

Run locally:
    pip install -r requirements.txt
    python spacex_dash_app.py

Then open http://127.0.0.1:8050 in a browser.
"""
from pathlib import Path

import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html

DATA_PATH = Path(__file__).with_name("spacex_launch_dash.csv")
spacex_df = pd.read_csv(DATA_PATH)
spacex_df = spacex_df.drop(columns=["Unnamed: 0"], errors="ignore")

min_payload = int(spacex_df["Payload Mass (kg)"].min())
max_payload = int(spacex_df["Payload Mass (kg)"].max())
launch_sites = sorted(spacex_df["Launch Site"].dropna().unique())

app = Dash(__name__)
server = app.server

app.layout = html.Div(
    [
        html.H1(
            "SpaceX Launch Records Dashboard",
            style={"textAlign": "center", "marginBottom": "1.5rem"},
        ),
        html.Div(
            [
                html.Label("Launch site", htmlFor="site-dropdown"),
                dcc.Dropdown(
                    id="site-dropdown",
                    options=[{"label": "All Sites", "value": "ALL"}]
                    + [{"label": site, "value": site} for site in launch_sites],
                    value="ALL",
                    clearable=False,
                    searchable=True,
                ),
            ],
            style={"maxWidth": "900px", "margin": "0 auto 1rem auto"},
        ),
        dcc.Graph(id="success-pie-chart"),
        html.Div(
            [
                html.Label("Payload range (kg)", htmlFor="payload-slider"),
                dcc.RangeSlider(
                    id="payload-slider",
                    min=min_payload,
                    max=max_payload,
                    step=500,
                    value=[min_payload, max_payload],
                    marks={value: f"{value:,}" for value in range(0, max_payload + 1, 2000)},
                    tooltip={"placement": "bottom", "always_visible": False},
                ),
            ],
            style={"maxWidth": "900px", "margin": "1rem auto"},
        ),
        dcc.Graph(id="success-payload-scatter-chart"),
        html.P(
            "Data source: IBM Skills Network - spacex_launch_dash.csv",
            style={"textAlign": "center", "fontSize": "0.9rem"},
        ),
    ],
    style={"fontFamily": "Arial, sans-serif", "padding": "1rem"},
)


@app.callback(
    Output("success-pie-chart", "figure"),
    Input("site-dropdown", "value"),
)
def update_pie_chart(selected_site: str):
    if selected_site == "ALL":
        successful = (
            spacex_df.loc[spacex_df["class"] == 1]
            .groupby("Launch Site", as_index=False)
            .size()
            .rename(columns={"size": "Successful Launches"})
        )
        return px.pie(
            successful,
            values="Successful Launches",
            names="Launch Site",
            title="Successful launches by site",
            hole=0.25,
        )

    filtered = spacex_df.loc[spacex_df["Launch Site"] == selected_site].copy()
    counts = (
        filtered["class"]
        .value_counts()
        .reindex([0, 1], fill_value=0)
        .rename_axis("class")
        .reset_index(name="Launches")
    )
    counts["Outcome"] = counts["class"].map({0: "Unsuccessful", 1: "Successful"})
    return px.pie(
        counts,
        values="Launches",
        names="Outcome",
        title=f"Landing outcomes at {selected_site}",
        hole=0.25,
    )


@app.callback(
    Output("success-payload-scatter-chart", "figure"),
    [Input("site-dropdown", "value"), Input("payload-slider", "value")],
)
def update_scatter_chart(selected_site: str, payload_range: list[int]):
    low, high = payload_range
    filtered = spacex_df.loc[
        spacex_df["Payload Mass (kg)"].between(low, high, inclusive="both")
    ].copy()
    if selected_site != "ALL":
        filtered = filtered.loc[filtered["Launch Site"] == selected_site]

    site_label = "all sites" if selected_site == "ALL" else selected_site
    return px.scatter(
        filtered,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category",
        symbol="Launch Site",
        hover_data=["Flight Number", "Booster Version", "Launch Site"],
        title=f"Payload and landing outcome - {site_label}",
        labels={"class": "Landing outcome (0 = unsuccessful, 1 = successful)"},
    )


if __name__ == "__main__":
    app.run(debug=True, port=8050)
