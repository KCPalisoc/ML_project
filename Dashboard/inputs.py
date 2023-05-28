"""
Dictionary and List Inputs for the Dashboard
"""

# Style Dictionaries

header_style = {"text-align": "center",
                "font-family": "Helvetica"}

small_dropdown_style = {"display": "inline-block",
                        "text-align": "center",
                        "font-family": "Helvetica",
                        "width": "60%"}

big_dropdown_style = {"display": "inline-block",
                      "text-align": "center",
                      "font-family": "Helvetica",
                      "width": "85%"}

plot_style = {'width': "100%"}

map_dd_style = {"text-align": "center",
                "width": "75%",
                "padding": "2rem 1rem"}

hl_reg_style = {'display': 'inline-block'}

bar_filter = {"width": "40%", 
              "display": "inline-block", 
              "font-family": "Helvetica"}

hl_reg_layout_style = {"width": "100%", 
                       "display": "inline-block"}

hl_data_table_text = {"width": "100px", 
                      "minWidth": "100px", 
                      "maxWidth": "100px", 
                      "textOverflow": "ellipsis", 
                      "font-family": "Helvetica"}

ll_data_table_cell = {"text-align": "left", 
                      "width": 4,
                      "textOverflow": "ellipsis",
                      "font-family": "Helvetica"}

# Column Lists

compare_col = ['Country',
               '2020 GDP Per Capita', 
               '2020 Gain Index', 
               'Project Funding (in Millions)',
               'Climate Change Project Funding (in Millions)']

bottom_table_cols = [{"name": "Project Name", "id": "Project Name"},
                     {"name": "Status", "id": "Status"},
                     {"name": "Commitment Amount", "id": "Commitment Amount"},
                     {"name": "Effective Date", "id": "Effective Date"},
                     {"name": "Project URL", "id": "Project URL"},
                     {"name": "Search Terms", "id": "Tokens"}]

# Filter Options

ngram_filter = [{'label': 'Unigram', 'value': 'unigram'}, 
                {'label': 'Bigram', 'value': 'bigram'}, 
                {'label': 'Trigram', 'value': 'trigram'}]

star_filter = [{'label': 'All Stars', 'value': 'all_stars'}, 
                {'label': '1 and 5 Stars', 'value': '1_5_stars'}, 
                {'label': '1, 3, and 5 Stars', 'value': '1_3_5_stars'}]

equality_filter = [{'label': 'Equal', 'value': 'equal'},
                   {'label': 'Unequal', 'value': 'unequal'}]

# country_options = [{"label": country, "value": country} for country in ll_df["Country"].unique()]

# hl_data_table_options = [{"name": i, "id": i} for i in hl_df.loc[:, compare_col]]