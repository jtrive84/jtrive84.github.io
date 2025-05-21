import dash
from dash import dcc, html, Dash, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Sample dataset
df = pd.DataFrame({
    'Fruit': ['Apples', 'Bananas', 'Cherries', 'Dates'],
    'Sales Q1': [30, 45, 10, 20],
    'Sales Q2': [40, 30, 15, 25]
})

app = Dash(
    __name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    url_base_pathname="/app01/"
)

app.layout = dbc.Container([
    html.H3("Fruit Sales by Quarter", className="my-3"),
    dcc.Dropdown(
        id='quarter-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns if col != 'Fruit'],
        value='Sales Q1',
        clearable=False,
        className="mb-4"
    ),
    dcc.Graph(id='sales-chart')
], className="p-4")

@app.callback(
    Output('sales-chart', 'figure'),
    Input('quarter-dropdown', 'value')
)
def update_chart(selected_col):
    fig = px.bar(df, x='Fruit', y=selected_col, title=f"{selected_col} per Fruit", labels={'y': 'Sales'})
    return fig

server = app.server

if __name__ == '__main__':
    app.run(debug=True)