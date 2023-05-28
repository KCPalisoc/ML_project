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
                               hl_data_table_text, bar_filter, bar_options, \
                                ll_data_table_cell
                               # country_options, hl_data_table_options, 
from Dashboard.load_and_clean.yelp_preprocess import yelp_sample_unequal, yelp_sample_equal, \
                                                     x_unequal, y_unequal, x_equal, y_equal
# from Dashboard.graphs.starting_graphs import logreg_fig, linreg_fig, hist_fig, \
                                         # map_fig, scatter_fig, bar_fig, avg_commit_fig


## App Layout

app.layout = dbc.Container([
    html.Br(),
    dbc.Row(html.H1(""), 
                    style=header_style,
                    justify='center'),
    html.Br(),

    dbc.Row(html.H3(""), 
                    style=header_style,
                    justify="center"),

    html.Br(),

    html.Br(),

    html.Br(),

    dbc.Row(html.H3("Static Regressions: "), 
                    style=header_style,
                    justify="center"),
    html.Br(),

    dbc.Row(html.Br()),
    html.Br(),

    dbc.Row(html.H3("Static Histograms: "), 
                    style=header_style,
                    justify="center"),
    
    html.Br(),

    dbc.Row(html.Br()),
    dbc.Row(html.Br()),
    html.Br(),
    
    dbc.Row(html.H2("Climate Change Project Deep Dive by Country"), 
                    style=header_style,
                    justify="center"),
    html.Br(),

    dbc.Row(html.H4("Primary Filter: Select a Country"), 
                    style=header_style,
                    justify="center"),

    html.Br(),

    dbc.Row(html.H4("Secondary Filter: Select Another Country to Compare"), 
                    style=header_style,
                    justify="center"),
    
    html.Br(),
    
    dbc.Row(html.H3("Data Table: Comparison of Country GDP and Climate Vulnerability"), 
                    style=header_style,
                    justify="center"),

    html.Br(),

    html.Br(),

    html.Br(),
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
    html.Br(),

    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row(html.H3("Data Table: "), 
                    style=header_style,
                    justify="center"),
    html.Br(),

    html.Br(),
    html.Br(),

    html.Br()],

fluid=True, style={"backgroundColor": "#D2E5D0"})

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=3105)
