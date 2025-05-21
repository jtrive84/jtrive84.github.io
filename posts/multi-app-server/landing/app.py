import dash
from dash import html, Dash
import dash_bootstrap_components as dbc


app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.title = "Application Dashboard"

app.layout = dbc.Container([

    dbc.Row([
        dbc.Col(
            html.Div([
                html.H1("Application Dashboard", className="display-4"),
            ]),
            width=12,
            className="text-center my-5"
        )
    ]),
    
    dbc.Row([
       
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("app01"),
                dbc.CardBody([
                    # html.H5("Application 2", className="card-title"),
                    html.P("Sample Dash App", className="card-text"),
                    dbc.Button("Launch", href="/app01/", color="success", external_link=True, target="_blank")
                ])
            ], className="mb-4"),
            md=6
        ),

        dbc.Col(
            dbc.Card([
                dbc.CardHeader("app02"),
                dbc.CardBody([
                    # html.H5("Application 2", className="card-title"),
                    html.P("Sample Shiny App", className="card-text"),
                    dbc.Button("Launch", href="/app02/", color="success", external_link=True, target="_blank")
                ])
            ], className="mb-4"),
            md=6
        )
    ], className="mb-5"),
    
    dbc.Row([
        dbc.Col(html.Footer("© 2025 JDT — All rights reserved", className="text-center text-muted"), width=12)
    ])
], fluid=True)

server = app.server

if __name__ == "__main__":

    app.run(debug=True)