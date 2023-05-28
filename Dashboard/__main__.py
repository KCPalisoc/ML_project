'''
Dashboard Constructor
______________________
'''

from dash import html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px

from Dashboard.dashboard import app
from Dashboard.inputs import header_style, small_dropdown_style, \
                               big_dropdown_style, plot_style, bottom_table_cols, \
                               paris_filter, source_filter, map_dd_options, \
                               map_dd_style, hl_reg_style, hl_reg_layout_style, \
                               hl_data_table_text, ngram_filter, star_filter, \
                               equality_filter
                               # country_options, hl_data_table_options, 
from Dashboard.Graphs.graph_constructor import scatter_graph, graph_score, graph_time

## App Layout

app.layout = dbc.Container([
    html.Br(),
    dbc.Row(html.H1("Understanding Public Perceptions of the ObamaCare Program: \
                    A Sentiment Analysis Approach Utilizing Open-Source Data"), 
                    style=header_style,
                    justify='center'),
    html.Br(),

    dbc.Row(html.H3("Exploratory Review of Yelp Review Data"), 
                    style=header_style,
                    justify="center"),

    html.Br(),

    dbc.Row(html.H3("Exploratory Review of Twitter Data"), 
                    style=header_style,
                    justify="center"),
    html.Br(),

    dbc.Row(html.Br()),
    html.Br(),

    dbc.Row(html.H3("Modeling Sentiment Analysis"), 
                    style=header_style,
                    justify="center"),
    
    html.Br(),

    dbc.Row(html.Br()),
    dbc.Row(html.Br()),
    html.Br(),
    
    dbc.Row(html.H2("Applying Twitter Data to Optimal ML Model"), 
                    style=header_style,
                    justify="center"),
    html.Br(),

    dbc.Row(html.H4("Primary Filter: "), 
                    style=header_style,
                    justify="center"),

    html.Br(),

    dbc.Row(html.H4("Secondary Filter: "), 
                    style=header_style,
                    justify="center"),
    
    html.Br(),
    
    dbc.Row(html.H3("Data Table: "), 
                    style=header_style,
                    justify="center"),

    html.Br(),

    dbc.Row(html.H3("Graphs "), 
                    style=header_style,
                    justify="center"),

    html.Div(html.Br()),

    html.Div(html.H5("Category Filter: "), 
                     style=hl_reg_layout_style),

    html.Div(html.Br()),

    html.Div(html.H5("Color Filter: "), 
                     style=hl_reg_layout_style),
    
    html.Br(),

    dbc.Row(html.H3("Data Table: "), 
                    style=header_style,
                    justify="center"),

    html.Br()],

fluid=True, style={"backgroundColor": "#4CB5F5"})

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=3105)
