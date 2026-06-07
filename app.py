from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas
import csv
import plotly.express as px

DATA_PATH = "proccessed_sales_data.csv"
app = Dash()

colours = {
    'background': "#241B1B",
    'text': "#5385C8"
}

sales: list[float] = []
dates: list[str] = []
region: list[str] = []

with open(DATA_PATH, 'r') as csvData:
    csvReader = csv.reader(csvData)
    for item in csvReader:
        if not (item[0] == 'Sales'):
            sales.append(float(item[0]))
            dates.append(item[1])
            region.append(item[2])

dataFrame = pandas.DataFrame({
    "Date": dates,
    "Sales": sales,
    "Region": region
})

app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            html, body {
                margin: 0;
                padding: 0;
                height: 100%;
                background-color: #1e1e1e; 
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""

app.layout = html.Div(
    
    style={
        'backgroundColor': colours['background'],
        "minHeight": "100vh",
        "padding": "20px"
    },

    children=[
    html.H1(
        children='Sales Data', 
        style={'color': colours['text'], "textAlign": "center"}
    ),

    html.Div(
        children='The sales data for Pink Morsels',
        style={'color':colours['text'], "textAlign": "center"}
    ),

    html.Div(
        children='Select Region:',
        style={'color':colours['text'], "textAlign": "center"}
    ),

    dcc.RadioItems(
        id='Region_radio',
        options=[
            {'label': html.Div(['North'], style={'color': colours['text']}), 'value': 'north'},
            {'label': html.Div(['East'], style={'color': colours['text']}), 'value': 'south'},
            {'label': html.Div(['South'], style={'color': colours['text']}), 'value': 'east'},
            {'label': html.Div(['West'], style={'color': colours['text']}), 'value': 'west'},
        ],
        value='north', 
        labelStyle={'display': 'block'},
        inline=True,
        style={"textAlign": "center"}
    ),

    dcc.Graph(
        id='sales_plot'
    )
])

@app.callback(
    Output('sales_plot', 'figure'),
    Input('Region_radio', 'value')
)
def update_graph(selected_region):
    try:
        filtered_df = dataFrame[dataFrame['Region'] == selected_region]

        fig = px.line(filtered_df, x='Date', y='Sales')

        fig.update_layout(
            plot_bgcolor=colours['background'],
            paper_bgcolor=colours['background'],
            font_color=colours['text']
        )

        fig.update_traces(line=dict(color=colours['text'], width=3))
        return fig

    except Exception as e:
        return px.line(title=f"Error: {e}")


if __name__ == '__main__':
    app.run(debug=True)
