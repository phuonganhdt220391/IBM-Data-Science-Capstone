# IBM Data Science Capstone - SpaceX Falcon 9

This repository contains the final project for the **IBM Data Science Professional Certificate**. The project applies an end-to-end data science workflow to analyze and predict whether the SpaceX Falcon 9 first stage will land successfully.

## Project workflow

| Stage | File |
|---|---|
| SpaceX API data collection | [jupyter-labs-spacex-data-collection-api.ipynb](jupyter-labs-spacex-data-collection-api.ipynb) |
| Web scraping | [jupyter-labs-webscraping.ipynb](jupyter-labs-webscraping.ipynb) |
| Data wrangling and target creation | [labs-jupyter-spacex-Data-wrangling.ipynb](labs-jupyter-spacex-Data-wrangling.ipynb) |
| Exploratory data analysis and feature engineering | [eda_visualization.ipynb](eda_visualization.ipynb) |
| Exploratory analysis with SQL | [jupyter_labs_eda_sql_coursera_sqllite.ipynb](jupyter_labs_eda_sql_coursera_sqllite.ipynb) |
| Launch-site analysis with Folium | [lab_jupyter_launch_site_location.ipynb](lab_jupyter_launch_site_location.ipynb) |
| Interactive Plotly Dash application | [spacex_dash_app.py](spacex_dash_app.py) |
| Machine-learning prediction | [SpaceX_Machine_Learning_Prediction.ipynb](SpaceX_Machine_Learning_Prediction.ipynb) |
| Final report (PDF) | [Course 10_Data Science Capstone Project Report_PA.pdf](Course%2010_Data%20Science%20Capstone%20Project%20Report_PA.pdf) |

## Data files

- `dataset_part_1.csv`: cleaned API data before target labeling.
- `dataset_part_2.csv`: labeled data with the binary `Class` target.
- `dataset_part_3.csv`: one-hot encoded feature matrix.
- `Spacex.csv`: course dataset used for SQL analysis.
- `spacex_web_scraped.csv`: stable snapshot for the web-scraping notebook.
- `spacex_launch_dash.csv`: data for the Plotly Dash application.
- `spacex_launch_geo.csv`: coordinates and outcomes for Folium mapping.

## Run locally

```bash
python -m pip install -r requirements.txt
jupyter notebook
```

Run the dashboard separately:

```bash
python spacex_dash_app.py
```

Then open `http://127.0.0.1:8050`.

## Main methods

Data acquisition, data wrangling, exploratory data analysis, SQL, Folium, Plotly Dash, feature engineering, logistic regression, support vector machines, decision trees and k-nearest neighbors.

## Author

GitHub: [phuonganhdt220391](https://github.com/phuonganhdt220391)

## Data source

The included course datasets are from IBM Skills Network resources for the Applied Data Science Capstone course. See [DATA_SOURCES.md](DATA_SOURCES.md).
