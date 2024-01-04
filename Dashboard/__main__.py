'''
Dashboard Constructor
______________________
'''

from dash import html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import datetime as dt
import pandas as pd

from Dashboard.dashboard import app
from Dashboard.inputs import header_style, small_dropdown_style, \
                             plot_style, hl_reg_style, hl_reg_layout_style, \
                             ngram_filter, star_filter, equality_filter, \
                             model_filter, yelp_sample_style, token_options, \
                             tweet_sample_style
from Dashboard.Graphs.graph_constructor import scatter_graph, graph_score, graph_time
from Dashboard.load_and_clean.yelp_preprocess import yelp_sample_unequal, yelp_sample_equal, \
                                                     hyper_tuning, combo, list_builder
from Dashboard.load_and_clean.tweet_preprocess import twitter_df 
from Dashboard.exploratory_analysis.explore_twitter import tweet_bar, word_dict

scatter_fig = px.scatter(yelp_sample_unequal, 
                         x="length", 
                         y="stars",
                         title="",
                         trendline="ols")

top_100_words, top_100_count = word_dict(twitter_df.loc[:, 'Tokenized_Text'], 'word')
twitter_bar_fig = px.bar(top_100_words, top_100_count)

sample_tweets = twitter_df.iloc[:10, 1:3]
sample_tweets['Date'] = pd.to_datetime(sample_tweets['Date']).dt.date

sample_reviews = yelp_sample_unequal.iloc[:10, 3:]


## App Layout

app.layout = dbc.Container([
    html.Br(),
    dbc.Row(html.H1("Understanding Public Perceptions of the ObamaCare Program: \
                    A Sentiment Analysis Approach Utilizing Open-Source Data"), 
                    style=header_style,
                    justify='center'),
    html.Br(),

    dbc.Row(html.H3("10 Yelp Reviews"), 
                    style=header_style,
                    justify="center"),
    
    dbc.Row(dash_table.DataTable(id="yelp_data_table",
                                 style_data={'whiteSpace': 'normal',
                                             'height': 'auto'},
                                 data=sample_reviews.to_dict('records'),
                                 columns=[{"name": i, "id": i} for i in sample_reviews.columns],
                                 css=[{'selector': '.dash-spreadsheet td div',
                                       'rule': '''display': 'inline'''}],
                                 tooltip_data=[{column: {'value': str(value), 'type': 'markdown'}
                                                for column, value in row.items()} 
                                                for row in sample_reviews.to_dict('records')],
                                 tooltip_duration=None,
                                 page_current=0,
                                 page_size=5,
                                 style_cell_conditional=yelp_sample_style,
                                 sort_action="native",
                                 filter_action="native",
                                 sort_mode="multi")),
    html.Br(),

    dbc.Row(html.H3("Exploratory Review of Yelp Review Data"), 
                    style=header_style,
                    justify="center"),

    html.Br(),

    dbc.Row(html.H3("10 Tweets"), 
                    style=header_style,
                    justify="center"),

    dbc.Row(dash_table.DataTable(id="twitter_data_table", 
                                 style_data={'whiteSpace': 'normal',
                                             'height': 'auto'},
                                 data=sample_tweets.to_dict('records'),
                                 columns=[{"name": i, "id": i} for i in sample_tweets.columns],
                                 css=[{'selector': '.dash-spreadsheet td div',
                                       'rule': '''display': 'inline'''}],
                                 tooltip_data=[{column: {'value': str(value), 'type': 'markdown'}
                                                for column, value in row.items()} 
                                                for row in sample_tweets.to_dict('records')],
                                 tooltip_duration=None,
                                 page_current=0,
                                 page_size=5,
                                 style_cell_conditional=tweet_sample_style,
                                 sort_action="native",
                                 filter_action="native",
                                 sort_mode="multi")),
    html.Br(),

    dbc.Row(html.H3("Exploratory Review of Twitter Data"), 
                    style=header_style,
                    justify="center"),
    html.Br(),

    html.Div(html.H5("Token Filter:"), 
                     style=hl_reg_layout_style),
    
    html.Br(),

    dbc.Row(dcc.Dropdown(id="token_dd",
                         options=token_options,
                         multi=False,
                         style=small_dropdown_style),
                         justify="center"),

    dbc.Row(html.Br()),
    html.Br(),

    dbc.Row(dcc.Graph(id="twitter_bar",
                      figure=twitter_bar_fig,
                      style=plot_style), 
                      style=hl_reg_style),
    
    dbc.Row(html.Br()),
    html.Br(),

    dbc.Row(html.H3("Specific Sentiment Analysis"), 
                    style=header_style,
                    justify="center"),
    
    dbc.Row(html.H4("Filter: Star Rating"), 
                    style=header_style,
                    justify="center"),

    dbc.Row(dcc.Dropdown(id="star_dd",
                         options=star_filter,
                         multi=False,
                         style=small_dropdown_style),
                         justify="center"),

    dbc.Row(html.H4("Filter: Ngram"), 
                    style=header_style,
                    justify="center"),

    dbc.Row(dcc.Dropdown(id="ngram_dd",
                         options=ngram_filter,
                         multi=False,
                         style=small_dropdown_style),
                         justify="center"),
    
    dbc.Row(html.H4("Filter: Star Equality"), 
                    style=header_style,
                    justify="center"),

    dbc.Row(dcc.Dropdown(id="equality_dd",
                         options=equality_filter,
                         multi=False,
                         style=small_dropdown_style),
                         justify="center"),

    dbc.Row(html.H4("Filter: Model"), 
                    style=header_style,
                    justify="center"),

    dbc.Row(dcc.Dropdown(id="model_dd2",
                         options=model_filter,
                         multi=False,
                         style=small_dropdown_style),
                         justify="center"),
    
    html.Br(),

    dbc.Row(html.Div(id="result")),

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
    
    dbc.Row(html.H2("Modeling Sentiment Analysis"), 
                    style=header_style,
                    justify="center"),

    html.Br(),

    html.Div(html.H5("Model Filter:"), 
                     style=hl_reg_layout_style),
    
    html.Br(),

    dbc.Row(dcc.Dropdown(id="model_dd",
                         options=model_filter,
                         multi=False,
                         style=small_dropdown_style),
                         justify="center"),
    
    html.Br(),

    dbc.Row(dcc.Graph(id="scatter",
                      figure=scatter_fig,
                      style=plot_style), 
                      style=hl_reg_style),

    html.Br()],

fluid=True, style={"backgroundColor": "#4CB5F5"})

@app.callback(Output("result", "children"),
              [Input("star_dd", "value"),
               Input("ngram_dd", "value"),
               Input("equality_dd", "value"),
               Input("model_dd", "value")])

def update_result(star, ngram, equality, model):
    """
    This function updates the result
    """

    score, runtime = hyper_tuning(yelp_sample_equal, 
                                  yelp_sample_unequal,
                                  model, star, ngram, equality)
    
    return (html.P([f"Score: {score}", html.Br(), f"Runtime in minutes: {runtime}"]))

@app.callback(Output("twitter_bar", "figure"),
              Input("token_dd", "value"))

def update_twitter_bar(token):
    """
    This function plots 
    """
    top_100_words, top_100_count = word_dict(twitter_df.loc[:, 'Tokenized_Text'], token)
    tweet_bar(top_100_words, top_100_count, token)


@app.callback(Output("scatter", "figure"),
              Input("model_dd2", "value"))

def update_scatter(model):
    """
    This function plots accuracy for each varation for a given model 
    """

    score_lst, time_lst = list_builder(yelp_sample_equal, yelp_sample_unequal, model, combo)
    scatter_graph(combo, score_lst, time_lst, model)

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=3105)
   