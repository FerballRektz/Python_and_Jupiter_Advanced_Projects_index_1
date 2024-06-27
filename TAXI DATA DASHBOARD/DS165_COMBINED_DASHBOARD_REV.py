from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.graph_objects as go 
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from scipy import stats
import dash_daq as daq

app = Dash(__name__)

provider_names = ['Bay Cab',
 'Grand Cab',
 'UVC',
 'Capitol Cab',
 'My taxi Control',
 'DC VIP Cab',
 'Hitch',
 'CMT',
 'VeriFone',
 'Transco',
 'Yellow Cab']



bar_design_temp_arr =  ['', '/', '\\', 'x', '-', '|', '+', '.']

app.layout = html.Div(
    children= [


        # explaination choose, summary, explaination
        html.Div(
            children = [
                html.Div(
                    children = [
                        html.H1("Choose a Provider:", style= {'color': 'white', 'font-family':'Verdana,sans-serif', 'font-size': "2em"}),
                        dcc.Dropdown(id = "dropdown", options= provider_names, value= "Bay Cab",
                                                style={
                                                    'background-color': 'white',  # Set the background color
                                                    'color': 'black',  # Set the font color
                                                    'border': '2px solid #222222',  # Set the border color and width
                                                    'font-family': 'Verdana,sans-serif'  # Set the font style
                                                }
                                     )
                    ],
                    style = {
                        "grid-area": "1 / 1 / 1 / 1", 
                        "background-color":"#5c5757",
                    }
                ),

                html.Div(
                    children = [
                        html.H1("Summary", style = {"grid-area": "1 / 1 / 1 / 2", 'color': 'white', 'font-family':'Verdana,sans-serif', 'font-size': "2em"}),
                        html.H3("Average Trip Fare Ranking:",style = {"grid-area": "2 / 1 / 2 / 1",'color': 'white', 'font-family':'Verdana,sans-serif', 'font-size': "1em"}),
                        html.H3(id= "avg_fare", style= {"grid-area": "2 / 2 / 2 / 2", 'font-family':'Verdana,sans-serif', 'font-size': "1em"}),
                        html.H3("Average Trip Milage Ranking:",style = {"grid-area": "3 / 1 / 3 / 1",'color': 'white', 'font-family':'Verdana,sans-serif', 'font-size': "1em"}),
                        html.H3(id= "avg_milage",style= {"grid-area": "3 / 2 / 3 / 2", 'font-family':'Verdana,sans-serif', 'font-size': "1em"}),
                        html.H3("Average Trip Duration Ranking:",style = {"grid-area": "4 / 1 / 4 / 1",'color': 'white', 'font-family':'Verdana,sans-serif', 'font-size': "1em"}),
                        html.H3(id = "avg_duration", style= {"grid-area": "4 / 2 / 4 / 2", 'font-family':'Verdana,sans-serif', 'font-size': "1em"})
                    ],
                    style = {
                        "grid-area": "2 / 1 / 2 / 1", 
                        "background-color":"#5c5757",
                        "display": "grid",
                        "grid-template": " 1 fr 1fr 1fr 1fr / 1fr 1fr",
                        "gap": "0px"

                    },
                ),

                html.Div(
                    children = [
                        html.H1("Taxi Provider Transporation Efficiency Dashboard", style= {'color': 'white', 'font-family':'Verdana,sans-serif', 'font-size': "1em", "margin": "0px", "padding": "0px 0px 2px 0px"}),
                        html.H4("by Gerard Irao", style= {'color': 'white', 'font-family':'Verdana,sans-serif', 'font-size': "1em", "margin": "0px", "padding": "0px 0px 5px 0px"}),
                        html.P("This Dashboard is for customers in washtington DC to know what taxi providers offers the most efficient ride with the factors of provider fare amount, trip duration, and trip milage by thier mean", 
                               style= {'color': 'white', 'font-family':'Verdana,sans-serif', 'font-size': "1em"}
                               )

                    ],
                    style = {
                        "grid-area": "3 / 1 / 3 / 1", 
                        "background-color":"#5c5757",
                    },
                ),


            ],
            style = {
                "grid-area": "1 / 1 / 1 / 1", # outer grid
                "background-color":"#333333",
                "display": "grid", # inner grid 
                "grid-template": "20% 38% 38%  /  1fr",
                "gap": "10px"

            }
            
        ),

        # visualizations
        html.Div(
            children = [
                html.Div(
                    children = [
                        html.Div(
                            dcc.Graph(id= "graph1"),
                            style= {"grid-area": "1 / 1 / 1 / 1"}
                        ),
                        html.Div(
                            children = [
                                html.H3("Choose a bar design:", style = {'color': 'white', 'font-family':'Verdana,sans-serif', 'font-size': "1em"}),
                                dcc.Dropdown(id = "design_bar1", options= [
                                    {"label": "None", "value": bar_design_temp_arr[0]},
                                    {"label": "Slash Design", "value": bar_design_temp_arr[1]},
                                    {"label": "Slash Design 2", "value": bar_design_temp_arr[2]},
                                    {"label": "X Pattern", "value": bar_design_temp_arr[3]},
                                    {"label": "Horizontal Line Pattern", "value": bar_design_temp_arr[4]},
                                    {"label": "Vertical Line Pattern", "value": bar_design_temp_arr[5]},
                                    {"label": "Cross Pattern", "value": bar_design_temp_arr[6]},
                                    {"label": "Dot Pattern", "value": bar_design_temp_arr[7]}
                                ], value= '.', style={
                                                    'background-color': 'white',  # Set the background color
                                                    'color': 'black',  # Set the font color
                                                    'border': '2px solid #222222',  # Set the border color and width
                                                    'font-family': 'Verdana,sans-serif'  # Set the font style
                                                }),
                            ],
                            style = {"grid-area": "1 / 2 / 1 / 2"}                           
                        ),
                        html.Div(
                            children= [
                                daq.ColorPicker(
                                    id='my-color-picker-1',
                                    label='Bar Color Picker',
                                    value=dict(hex='#FF0000'),
                                    size = 160,
                                    style = {'color': 'white', 'font-family':'Verdana,sans-serif', 'font-size': "1em", "paper_bgcolor":"#5c5757", 'border': 'none', 'border-radius':'0%!important'}
                                )
                            ],
                            style = {"grid-area": "1 / 3 / 1 / 3"} 
                        )
                    
                    ],
                    style = {
                        "grid-area": "1 / 1 / 1 / 1", 
                        "background-color":"#5c5757",
                        "display": "grid",
                        "grid-template": "1fr / 50% 20% 30%"
                    }
                ),
                html.Div(
                    children = [
                        html.Div(
                            dcc.Graph(id= "graph2"),
                            style= {"grid-area": "1 / 1 / 1 / 1"}
                        ),
                        html.Div(
                            children = [
                                html.H3("Choose a bar design:",style = {'color': 'white', 'font-family':'Verdana,sans-serif', 'font-size': "1em"}),
                                dcc.Dropdown(id = "design_bar2", options= [
                                    {"label": "None", "value": bar_design_temp_arr[0]},
                                    {"label": "Slash Design", "value": bar_design_temp_arr[1]},
                                    {"label": "Slash Design 2", "value": bar_design_temp_arr[2]},
                                    {"label": "X Pattern", "value": bar_design_temp_arr[3]},
                                    {"label": "Horizontal Line Pattern", "value": bar_design_temp_arr[4]},
                                    {"label": "Vertical Line Pattern", "value": bar_design_temp_arr[5]},
                                    {"label": "Cross Pattern", "value": bar_design_temp_arr[6]},
                                    {"label": "Dot Pattern", "value": bar_design_temp_arr[7]}
                                ], value= '.', style={
                                                    'background-color': 'white',  # Set the background color
                                                    'color': 'black',  # Set the font color
                                                    'border': '2px solid #222222',  # Set the border color and width
                                                    'font-family': 'Verdana,sans-serif'  # Set the font style
                                                }),
                            ],
                            style = {"grid-area": "1 / 2 / 1 / 2"}                           
                        ),
                        html.Div(
                            children= [
                                daq.ColorPicker(
                                    id='my-color-picker-2',
                                    label='Bar Color Picker',
                                    value=dict(hex='#FF0000'),
                                    size = 160,
                                    style = {'color': 'white', 'font-family':'Verdana,sans-serif', 'font-size': "1em", "paper_bgcolor":"#5c5757", 'border': 'none', 'border-radius':'0%!important'}
                                )
                            ],
                            style = {"grid-area": "1 / 3 / 1 / 3"} 
                        )
                    ],
                    style = {
                        "grid-area": "2 / 1 / 2 / 1", 
                        "background-color":"#5c5757",
                        "display": "grid",
                        "grid-template": "1fr / 50% 20% 30%"
                    }
                ),
                html.Div(
                    children = [
                        html.Div(
                            dcc.Graph(id= "graph3"),
                            style= {"grid-area": "1 / 1 / 1 / 1"}
                        ),
                        html.Div(
                            children = [
                                html.H3("Choose a bar design:",style = {'color': 'white', 'font-family':'Verdana,sans-serif', 'font-size': "1em"}),
                                dcc.Dropdown(id = "design_bar3", options= [
                                    {"label": "None", "value": bar_design_temp_arr[0]},
                                    {"label": "Slash Design", "value": bar_design_temp_arr[1]},
                                    {"label": "Slash Design 2", "value": bar_design_temp_arr[2]},
                                    {"label": "X Pattern", "value": bar_design_temp_arr[3]},
                                    {"label": "Horizontal Line Pattern", "value": bar_design_temp_arr[4]},
                                    {"label": "Vertical Line Pattern", "value": bar_design_temp_arr[5]},
                                    {"label": "Cross Pattern", "value": bar_design_temp_arr[6]},
                                    {"label": "Dot Pattern", "value": bar_design_temp_arr[7]}
                                ], value= '.', style={
                                                    'background-color': 'white',  # Set the background color
                                                    'color': 'black',  # Set the font color
                                                    'border': '2px solid #222222',  # Set the border color and width
                                                    'font-family': 'Verdana,sans-serif'  # Set the font style
                                                }),
                            ],
                            style = {"grid-area": "1 / 2 / 1 / 2"}                           
                        ),
                        html.Div(
                            children= [
                                daq.ColorPicker(
                                    id='my-color-picker-3',
                                    label='Bar Color Picker',
                                    value=dict(hex='#FF0000'),
                                    size = 160,
                                    style = {'color': 'white', 'font-family':'Verdana,sans-serif', 'font-size': "1em", "paper_bgcolor":"#5c5757", 'border': 'none', 'border-radius':'0%!important'}
                                )
                            ],
                            style = {"grid-area": "1 / 3 / 1 / 3"} 
                        )
                    ],
                    style = {
                        "grid-area": "3 / 1 / 3 / 1", 
                        "background-color":"#5c5757",
                        "display": "grid",
                        "grid-template": "1fr / 50% 20% 30%"
                    }
                ),



            ],
            style = {
                "grid-area":" 1 / 2 / 1 / 2", # outer gird
                "background-color":"#333333",
                "display": "grid",
                "grid-template": "32% 32% 32%  /  1fr",
                "gap": "10px"
            }
            
        ),

        
    ],
    style= {
        "position": "absolute",
        "margin": "0px",
        "height": "98vh",
        "width": "97vw",
        "display":"grid",
        "gap": "10px",
        "grid-template": "1fr /  30% 70%",
        "background-color":"#333333",

    }
)

# load dataser
df_sample_cleaned_full = pd.read_csv("Zeta_export\\Advanced\\TAXI DATA DASHBOARD\\df_taxi_cleaned_data.csv")

# compute average of total fare mean, trip milage mean, and trip duration mean and sort
total_fare_amount_data = df_sample_cleaned_full.groupby("PROVIDER NAME",observed=True)["TotalAmount"].mean().round(2).sort_values(ascending =True)
milage_data =  df_sample_cleaned_full.groupby("PROVIDER NAME",observed=True)["Milage"].mean().round(2).sort_values(ascending = False)
duration_data =  df_sample_cleaned_full.groupby("PROVIDER NAME",observed=True)["Duration"].mean().round(2).sort_values(ascending =True)

# create maps of ranks of each provider in respective field of average trip fare, trip milage, and trip duration
total_fare_ranking = dict()
for i,j in enumerate(total_fare_amount_data.keys()):
    total_fare_ranking[j] = i + 1

milage_ranking = dict()
for i,j in enumerate(milage_data.keys()):
    milage_ranking[j] = i + 1

duration_ranking = dict()
for i,j in enumerate(duration_data.keys()):
    duration_ranking[j] = i + 1

# create color and design map for each provider
fare_marker_color_index_map_arr = dict()
i2 =0
for i,j in enumerate(total_fare_amount_data.keys()):
    if i < 5:
        fare_marker_color_index_map_arr[j] = i 
    else:
        fare_marker_color_index_map_arr[j] = i2
        i2+=1

milage_marker_color_index_map_arr = dict()
i2 =0
for i,j in enumerate(milage_data.keys()):
    if i < 5:
        milage_marker_color_index_map_arr[j] = i 
    else:
        milage_marker_color_index_map_arr[j] = i2
        i2+=1

duration_marker_color_index_map_arr = dict()
i2 =0
for i,j in enumerate(duration_data.keys()):
    if i < 5:
        duration_marker_color_index_map_arr[j] = i 
    else:
        duration_marker_color_index_map_arr[j] = i2
        i2+=1



# summary callback 

@callback(
    [
        Output(component_id= "avg_fare", component_property= "children"),
        Output(component_id= "avg_milage", component_property= "children"),
        Output(component_id= "avg_duration", component_property= "children")



    ],
    [
        Input(component_id= "dropdown",component_property= "value")
    ]
)
def summary_data(value):
    funct_avg_fare = total_fare_ranking[value] 
    funct_avg_milage = milage_ranking[value] 
    funct_avg_duration = duration_ranking[value] 
    div_arr = [funct_avg_fare, funct_avg_milage, funct_avg_duration]

    style_per_div_arr = []
    for i,j in enumerate(div_arr):
        if (j <=5):
            style_per_div_arr.append({'color': '#00ff00', 'font-family':'Verdana,sans-serif'})
        elif (j > 5) and (j <= 9):
            style_per_div_arr.append({'color': '#ffffff', 'font-family':'Verdana,sans-serif'})
        else:
            style_per_div_arr.append({'color': '#f54949', 'font-family':'Verdana,sans-serif'})

        
    return html.Div(f"#{div_arr[0]} / {total_fare_amount_data[value]}", style= style_per_div_arr[0]),  html.Div(f"#{div_arr[1]} / {milage_data[value]}", style= style_per_div_arr[1]),  html.Div(f"#{div_arr[2]} / {duration_data[value]}", style= style_per_div_arr[2])


# graph 1
@callback(
    [
        Output(component_id= "graph1", component_property= "figure"),


    ],
    [
        Input(component_id= "dropdown",component_property= "value"),
        Input(component_id= "design_bar1", component_property= "value"),
        Input(component_id= "my-color-picker-1", component_property= "value"),
        
    ]
)
def graph1_data(value1, value2, value3):
    color_matrix = ['#000000','#000000','#000000','#000000','#000000','#000000']
    design_matrix = ['','','','','','']
    design_matrix[fare_marker_color_index_map_arr[value1]] = value2
    color_matrix[fare_marker_color_index_map_arr[value1]] = value3['hex']
    # change plot size, text font, marker shape, and color 
    if total_fare_ranking[value1] < 6:
        bottom_top_index = [0,5]
    elif total_fare_ranking[value1] >= 6:
        bottom_top_index = [5,11]

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x= total_fare_amount_data.values[bottom_top_index[0]:bottom_top_index[1]], y= total_fare_amount_data.keys()[bottom_top_index[0]:bottom_top_index[1]],orientation= 'h',
                        text = [f'#{total_fare_ranking[i]}' for i in total_fare_amount_data.keys()][bottom_top_index[0]:bottom_top_index[1]],textposition="outside",marker_pattern_shape = design_matrix))
    fig2.update_traces(marker = dict(color = color_matrix), textfont=dict(family="verdana, sans-serif", size=7.5, color = "black"))
    fig2.update_layout(
        height = 235,
        width = 510,
        paper_bgcolor="#5c5757",  # Set the background color
        plot_bgcolor='#CCCCCC',
        title = "Ranking of Average Fare Means by Provider (lower is better)",
        margin=dict(t=40),
        xaxis=dict(
            title='Trip Fare Means',
            title_font=dict(size=10, family="verdana, sans-serif"),
            tickfont=dict(size=9, family="verdana, sans-serif")  # Set the font size of the tick labels
        ),
        yaxis=dict(
            title='Providers',
            title_font=dict(size=10, family="verdana, sans-serif"),
            tickfont=dict(size=9, family="verdana, sans-serif")  # Set the font size of the tick labels
        ),
        font=dict(family="verdana, sans-serif", size=10, color="white")
    )
    return [fig2]

# graph 2
@callback(
    [
        Output(component_id= "graph2", component_property= "figure"),


    ],
    [
        Input(component_id= "dropdown",component_property= "value"),
        Input(component_id= "design_bar2", component_property= "value"),
        Input(component_id= "my-color-picker-2", component_property= "value"),
        
    ]
)
def graph2_data(value1,value2,value3):
    color_matrix = ['#000000','#000000','#000000','#000000','#000000','#000000']
    design_matrix = ['','','','','','']
    design_matrix[milage_marker_color_index_map_arr[value1]] = value2
    color_matrix[milage_marker_color_index_map_arr[value1]] = value3['hex']
    # change plot size, text font, marker shape, and color 
    if milage_ranking[value1] < 6:
        bottom_top_index = [0,5]
    elif milage_ranking[value1] >= 6:
        bottom_top_index = [5,11]


    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x= milage_data.values[bottom_top_index[0]:bottom_top_index[1]], y= milage_data.keys()[bottom_top_index[0]:bottom_top_index[1]],orientation= 'h',
                        text = [f'#{milage_ranking[i]}' for i in milage_data.keys()][bottom_top_index[0]:bottom_top_index[1]],textposition="outside",marker_pattern_shape = design_matrix))
    fig2.update_traces(marker = dict(color = color_matrix), textfont=dict(family="verdana, sans-serif", size= 7.5, color = "black"))
    fig2.update_layout(
        height = 235,
        width = 510,
        paper_bgcolor="#5c5757",  # Set the background color
        plot_bgcolor='#CCCCCC',
        title = "Ranking of Average Trip Milage Means by Provider (higher is better)",
        margin=dict(t=40),
        xaxis=dict(
            title='Trip Milage Means',
            title_font=dict(size=10, family="verdana, sans-serif"),
            tickfont=dict(size=9, family="verdana, sans-serif")  # Set the font size of the tick labels
        ),
        yaxis=dict(
            title='Providers',
            title_font=dict(size=10, family="verdana, sans-serif"),
            tickfont=dict(size=9, family="verdana, sans-serif")  # Set the font size of the tick labels
        ),
        font=dict(family="verdana, sans-serif", size=10, color="White")
    )
    return [fig2]

# graph 3
@callback(
    [
        Output(component_id= "graph3", component_property= "figure"),


    ],
    [
        Input(component_id= "dropdown",component_property= "value"),
        Input(component_id= "design_bar3", component_property= "value"),
        Input(component_id= "my-color-picker-3", component_property= "value"),
        
    ]
)
def graph3_data(value1,value2,value3):
    color_matrix = ['#000000','#000000','#000000','#000000','#000000','#000000']
    design_matrix = ['','','','','','']
    design_matrix[duration_marker_color_index_map_arr[value1]] = value2
    color_matrix[duration_marker_color_index_map_arr[value1]] = value3['hex']
    # change plot size, text font, marker shape, and color 
    if duration_ranking[value1] < 6:
        bottom_top_index = [0,5]
    elif duration_ranking[value1] >= 6:
        bottom_top_index = [5,11]

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x= duration_data.values[bottom_top_index[0]:bottom_top_index[1]], y= duration_data.keys()[bottom_top_index[0]:bottom_top_index[1]],orientation= 'h',
                        text = [f'#{duration_ranking[i]}' for i in duration_data.keys()][bottom_top_index[0]:bottom_top_index[1]], textposition="outside",marker_pattern_shape = design_matrix ))
    fig2.update_traces(marker = dict(color = color_matrix), textfont=dict(family="verdana, sans-serif", size=7.5, color = "black"))
    fig2.update_layout(
        height = 235,
        width = 510,
        paper_bgcolor="#5c5757",  # Set the background color
        plot_bgcolor='#CCCCCC',
        title = "Ranking of Trip Duration Means by Provider (lower is better)",
        margin=dict(t=40),
        xaxis=dict(
            title='Trip Duration Means',
            title_font=dict(size=10, family="verdana, sans-serif"),
            tickfont=dict(size=9, family="verdana, sans-serif")  # Set the font size of the tick labels
        ),
        yaxis=dict(
            title='Providers',
            title_font=dict(size=10, family="verdana, sans-serif"),
            tickfont=dict(size=9, family="verdana, sans-serif")  # Set the font size of the tick labels
        ),
        font=dict(family="verdana, sans-serif", size=10, color="White")
    )
    return [fig2]


if __name__ == "__main__":
    app.run(debug= True)

