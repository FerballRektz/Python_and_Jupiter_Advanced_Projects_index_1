from dash import Dash, html, Input, Output, callback, dcc, dash_table
import plotly.graph_objects as go 
from plotly.subplots import make_subplots
import pandas as pd

# cleaned data for visualization
# put needed libraries created by data cleaning here
df_viz = pd.read_csv(filepath_or_buffer= "Zeta_export\\Advanced\\CHESS DATA DASHBOARD\\cleaned_data_act_2.csv") 
player_info_df = pd.read_csv(filepath_or_buffer= "Zeta_export\\Advanced\\CHESS DATA DASHBOARD\chest_player_match_data.csv") 


# dashboard info 
drop_down_data = []
for i,j in enumerate(player_info_df["Players"]):
    drop_down_data.append(j + " (MP: " + str(player_info_df.loc[i,"Matches_Played"]) +", Win Rate: " + str(player_info_df.loc[i,"Win_rate"]) + "% )")
player_info_df["Drop_down_data"] = drop_down_data




# execute dashboard making

# Create a Dash application
app = Dash(__name__)

# Define the layout
app.layout = html.Div(
children= [ # outer background 
# Dashboard name and choices
    html.Div(
        children= [
            html.H1("PLAYER STANDARD CHESS MATCHES DATA DASHBOARD",style= {"font-size": "1.5em", "font-family":"Verdana, sans-serif"}),
            html.H3("By Gerard Irao",style= {"font-size": "1em", "font-family":"Verdana, sans-serif"}),

        ],
        style = {
            "grid-column": "1",
            "grid-row": "1",
            "margin": "0px",
            "padding": "0px",
            "height": "20%",
            "width": "30%"
        }
    ),
    html.Div(
        children= [
            html.H1("CHOOSE YOUR CHESS PLAYER TO ANALYZE",style= {"font-size": "1.5em", "font-family":"Verdana, sans-serif"}),
            dcc.Dropdown(id = 'dropdown-selection',options= drop_down_data, value= drop_down_data[0], style= {"font-size": "1em", "font-family":"Verdana, sans-serif"})

        ],
        style = {
            "grid-column": "2",
            "grid-row": "1",
            "margin": "0px",
            "padding": "0px",
            "height": "20%",
            "width": "70%"
        }
    ),
# player info 
    html.Div(
        children= [
            html.H1("PLAYER INFORMATION",style= {"font-size": "1.5em", "font-family":"Verdana, sans-serif"}),
            html.H3(id = "player-name", style= {"font-size": "1em", "font-family":"Verdana, sans-serif"}),
            html.H3(id = "player-id", style= {"font-size": "1em", "font-family":"Verdana, sans-serif"}),
            html.H3(id = "player-ranking", style= {"font-size": "1em", "font-family":"Verdana, sans-serif"}),
            html.H3(id = "player-match-played", style= {"font-size": "1em", "font-family":"Verdana, sans-serif"}),
            html.H3(id = "player-win-rate", style= {"font-size": "1em", "font-family":"Verdana, sans-serif"}),
            html.H3(id = "player-preferred-strat", style= {"font-size": "1em", "font-family":"Verdana, sans-serif"})
        ],
        style = {
            "grid-column": "1",
            "grid-row": "2",
            "margin": "0px",
            "padding": "0px",
            "height": "30%",
            "width": "30%"
        }
    ),
# History Table 
    html.Div(
        children= [
            html.H1("CHESS HISTORY",style= {"font-size": "1.5em", "font-family":"Verdana, sans-serif"}),
            html.Div(id = "table-container")
        ],
        style = {
            "grid-column": "1",
            "grid-row": "3 / span 2",
            "margin": "0px",
            "padding": "0px",
            "height": "50%",
            "width": "30%"
        }
    ),
# graph vizes
    html.Div(
        children= [
            html.Div(
                dcc.Graph(id = "result-bar-plot"), 
                style= {"font-size": "1.5em", "font-family":"Verdana, sans-serif","grid-column": "1","grid-row": "1","height": "40%","width": "50%","margin": "0px", "padding": "0px","overflow-x:": "hidden"}),

            html.Div(
                dcc.Graph(id = "match-type-plot"), 
                style= {"font-size": "1.5em", "font-family":"Verdana, sans-serif","grid-column": "2","grid-row": "1","height": "40%","width": "50%","margin": "0px", "padding": "0px","overflow-x:": "hidden"}),

            html.Div(
                dcc.Graph(id = "first-move-plot"), 
                style= {"font-size": "1.5em", "font-family":"Verdana, sans-serif","grid-column": "1 / span 2","grid-row": "2","height": "30%","width": "100%","margin": "0px", "padding": "0px","overflow-x:": "hidden"}),

            html.Div(
                dcc.Graph(id = "strategy-plot"), 
                style= {"font-size": "1.5em", "font-family":"Verdana, sans-serif","grid-column": "1 / span 2","grid-row": "3","height": "30%","width": "100%", "margin": "0px", "padding": "0px","overflow-x:": "hidden"})
        ],
        style = {
            "grid-column": "2",
            "grid-row": "2 / span 3",
            "margin": "0px",
            "padding": "0px",
            "height": "50%",
            "width": "70%",
            "display": "grid",
            "grid-template-columns": "50% 50\%",
            "grid-template-rows": "40% 30\% 30\% ",
            "overflow:": "hidden"
        }
    )



],
style={"display": "grid",
"grid-template-columns": "30% 60\%",
"grid-template-rows": "20% 30\% 30\% 20\% ",
"padding": "0px",
"margin":"0px",
"height":"100vh",
"width":"100vw"
    }
)












# Data Update

@callback(
    [
        Output(component_id= "player-name", component_property= 'children'),
        Output(component_id= "player-id", component_property= 'children'),
        Output(component_id= "player-ranking", component_property= 'children'),
        Output(component_id= "player-match-played", component_property= 'children'),
        Output(component_id= "player-win-rate", component_property= 'children'),
        Output(component_id= "player-preferred-strat", component_property= 'children'),
        Output(component_id= "table-container", component_property= 'children'),
        Output(component_id= "result-bar-plot", component_property= 'figure'),
        Output(component_id= "first-move-plot", component_property= 'figure'),
        Output(component_id= "strategy-plot", component_property= 'figure'),
        Output(component_id= "match-type-plot", component_property= 'figure')
    
    ],
    [
        Input('dropdown-selection', 'value')
    
    
    ]
)
def update_outputs(input_value):
    #target name 
    target_name = player_info_df[player_info_df["Drop_down_data"] == str(input_value)]["Players"].reset_index(drop= True)[0]


    # Match Results Data Viz
    win_pie_arr = {}
    win_pie_arr["win"] = (df_viz.loc[((df_viz["white_player"] == target_name) | (df_viz["black_player"] == target_name)) & (df_viz["match_winner"] == target_name),"match_winner"].count())
    win_pie_arr["loss"] = (df_viz.loc[((df_viz["white_player"] == target_name) | (df_viz["black_player"] == target_name)) & (df_viz["match_winner"] != target_name) & (df_viz["match_winner"] != "draw"),"match_winner"].count())
    win_pie_arr["draw"] = (df_viz.loc[((df_viz["white_player"] == target_name) | (df_viz["black_player"] == target_name)) & (df_viz["match_winner"] != target_name) & (df_viz["match_winner"] == "draw"),"match_winner"].count())

    win_df = pd.DataFrame({"Events":win_pie_arr.keys(),"Counts": win_pie_arr.values()})

    fig1 =  go.Figure()
    fig1.add_trace(go.Bar(x= win_df["Counts"], y= win_df["Events"],orientation= 'h',text = win_df["Counts"],textposition="outside",marker_pattern_shape = ['.','+','x']))
    fig1.update_traces(marker = dict(color = ["purple","grey","grey"]), textfont=dict(family="verdana, sans-serif", size=10))
    fig1.update_layout(
        height = 250,
        width = 500,
        title = "Result Data",
        xaxis=dict(
            title='Count',
            title_font=dict(size=14, family="verdana, sans-serif"),
            tickfont=dict(size=14, family="verdana, sans-serif")  # Set the font size of the tick labels
        ),
        yaxis=dict(
            title='Results',
            title_font=dict(size=14, family="verdana, sans-serif"),
            tickfont=dict(size=14, family="verdana, sans-serif")  # Set the font size of the tick labels
        ),
        font=dict(family="verdana, sans-serif", size=8, color="Black")
    )


    # most used opening moves
    strat_num = df_viz.loc[((df_viz["white_player"] == target_name) | (df_viz["black_player"] == target_name))].groupby("opening_data").count()["createdAt"].sort_values(ascending= False)
    string_strat_values = str()
    
    Strat_data_values = {"Other Moves":0}
    for i,j in enumerate(strat_num):
        if j == strat_num.values.max():
            Strat_data_values[strat_num.keys()[i]] = j
            string_strat_values += str(strat_num.keys()[i]) + ", "
            continue
        Strat_data_values["Other Moves"] += j
    # constraint
    if len(string_strat_values) >= 140:
        string_strat_values = "No Preffered Moves.."

    # Create a pie chart
    fig2 = go.Figure(data=[go.Pie(labels=list(Strat_data_values.keys()), values= list(Strat_data_values.values()))])

    # Update the layout
    fig2.update_layout(
        height = 300,
        width = 750,
        title='Strategies Used',
        xaxis=dict(title='X-axis', title_font=dict(size=14, family="verdana, sans-serif")),
        yaxis=dict(title='Y-axis', title_font=dict(size=14, family="verdana, sans-serif")),
        font=dict(family="verdana, sans-serif", size=10, color="Black")
    )

    # Update the pie chart properties
    fig2.update_traces( 
                    textposition='outside',
                    hoverinfo='label+value', 
                    textinfo='percent', 
                    marker=dict(colors =["grey","purple"], 
                                line=dict(color='black', width=2),
                            ),
                    textfont=dict(family="verdana, sans-serif", size=18, color = "black")          
    )



    # first chest piece move 

    df_open_white = df_viz[((df_viz["white_player"] == target_name))]
    df_open_black = df_viz[((df_viz["black_player"] == target_name))]
    first_move_white_data = df_open_white.groupby("white_first_move").count()["createdAt"].sort_values(ascending= False)
    first_move_black_data = df_open_black.groupby("black_first_move").count()["createdAt"].sort_values(ascending= False)

    fig3 = go.Figure(data=[go.Pie(labels= list(first_move_white_data.keys()), values= list(first_move_white_data.values))])

    # Update the layout
    fig3.update_layout(
        autosize=True,
        font=dict(family="verdana, sans-serif", size=12, color="Black"),
    )

    # Update the pie chart properties
    fig3.update_traces(
                    textposition='outside',
                    hole=0.55, 
                    hoverinfo='label+value', 
                    textinfo='percent', 
                    marker=dict( 
                                line=dict(color='black', width=2)
                    ),
                    textfont=dict(family="verdana, sans-serif", size=18, color = "black")          
    )

    fig4 = go.Figure(data=[go.Pie(labels= list(first_move_black_data.keys()), values= list(first_move_black_data.values))])

    # Update the layout
    fig4.update_layout(
        autosize=True,
        font=dict(family="verdana, sans-serif", size=12, color ="Black"),
    )

    # Update the pie chart properties
    fig4.update_traces(
                    textposition='outside',
                    hole=0.55, 
                    hoverinfo='label+value', 
                    textinfo='percent', 
                    marker=dict( 
                                line=dict(color='black', width=2)),
                    textfont=dict(family="verdana, sans-serif", size=18, color = "black")              
    )

    fig3_4 = make_subplots(rows = 1, cols= 2,specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    fig3_4.add_trace(fig3.data[0], row=1, col=1)
    fig3_4.add_trace(fig4.data[0], row=1, col=2)
    fig3_4.update_layout(title_text="Player First Moves",
        height = 300,
        width = 750,
        annotations = [
            dict(text='<b>WHITE</b>', x=0.175, y=0.5, font = dict(family="verdana, sans-serif", size=13, color = "black"), showarrow=False),
            dict(text='<b>BLACK</b>', x=0.825, y=0.5, font = dict(family="verdana, sans-serif", size=13, color = "black"), showarrow=False)
        ],
        font = dict(family="verdana, sans-serif", size=10, color = "black"), 
        legend_title_text= "Chest Moves"               
    )


    # type of chest match played 

    chest_type = df_viz[((df_viz["white_player"] == target_name) | (df_viz["black_player"] == target_name))]
    chest_type_data = chest_type.groupby("match_type").count()["createdAt"]

    fig5 = go.Figure(data=[go.Pie(labels= list(chest_type_data.keys()), values= list(chest_type_data.values))])

    # Update the layout
    fig5.update_layout(
        height = 250,
        width = 250,
        title='Type of Chest Match Played',
        xaxis=dict(title='X-axis', title_font=dict(size=18, family="verdana, sans-serif")),
        yaxis=dict(title='Y-axis', title_font=dict(size=18, family="verdana, sans-serif")),
        font=dict(family="verdana, sans-serif", size=8, color="Black")
    )

    # Update the pie chart properties
    fig5.update_traces( 
                    textposition='outside',
                    hoverinfo='label+value', 
                    textinfo='percent', 
                    marker=dict( 
                                line=dict(color='black', width=2),
                            ),
                    textfont=dict(family="verdana, sans-serif", size=18, color = "black")   
    )    


    # match history

    chest_type_white = df_viz.loc[df_viz["white_player"] == target_name,["createdAt","match_type","white_rating","white_player","black_player","black_rating","match_winner"]]
    chest_type_white["player_side"] = "white"
    chest_type_white["enemy_side"] = "black"
    chest_type_white = chest_type_white.rename(columns= {"white_player": "player_name","white_rating":"player_rating","black_player": "enemy_name","black_rating":"enemy_rating"})

    chest_type_black = df_viz.loc[df_viz["black_player"] == target_name,["createdAt","match_type","black_rating","black_player","white_player","white_rating","match_winner"]]
    chest_type_black["player_side"] = "black"
    chest_type_black["enemy_side"] = "white"
    chest_type_black = chest_type_black.rename(columns= {"black_player": "player_name","black_rating":"player_rating","white_player": "enemy_name","white_rating":"enemy_rating"})

    chest_type_inital_data = pd.concat([chest_type_white,chest_type_black]).sort_values(by= "createdAt",ascending= False).reset_index(drop = True)

    versus_data_arr = []
    for i in chest_type_inital_data.index:
        versus_data_arr.append(chest_type_inital_data.loc[i,"player_name"] + " vs " + chest_type_inital_data.loc[i,"enemy_name"]) 

    changed_match_winner = []
    for i in chest_type_inital_data["match_winner"]:
        if i == "draw":
            changed_match_winner.append("draw")
            continue
        if i == target_name:
            changed_match_winner.append("win")
        else:
            changed_match_winner.append("loss")

    chest_type_inital_data["matches"] = versus_data_arr
    chest_type_inital_data["result"] = changed_match_winner
    chest_type_hist_final = chest_type_inital_data.loc[:,["match_type","player_side","player_rating","matches", "enemy_rating","enemy_side","result"]]
    table_viz = dash_table.DataTable(
        data=chest_type_hist_final.to_dict('records'),
        columns=[{'name': col, 'id': col} for col in chest_type_hist_final.columns],
        style_cell={
            "font-size": "8px",
            'fontFamily': 'Verdana, sans-serif',
            'textAlign': 'center', 
         },
        style_header={
            "font-size": "10px",
            'fontFamily': 'Verdana, sans-serif',  
            'fontWeight': 'bold'  
        },
        page_size = 13
    )






    # player information 
    player_id = player_info_df[player_info_df["Players"] == target_name]["Player_ID"].reset_index(drop= True)[0]
    player_ranking = chest_type_inital_data[chest_type_inital_data["player_name"] == target_name]["player_rating"][0]
    player_match_played = player_info_df[player_info_df["Players"] == target_name]["Matches_Played"].reset_index(drop= True)[0]
    player_win_rate  = player_info_df[player_info_df["Players"] == target_name]["Win_rate"].reset_index(drop= True)[0]
    player_pref_strat = string_strat_values[:-2]



    return  f"Player Name: {target_name}",f"Player ID: {player_id}", f"Player Ranking: {player_ranking}", f"Matches Played : {player_match_played}", f"Win Rate {player_win_rate}%", f"Preffered Strategy: {player_pref_strat}", table_viz,fig1, fig3_4, fig2, fig5









# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)