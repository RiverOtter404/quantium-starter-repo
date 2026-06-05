from dash import Dash, html, dcc
import pandas
import csv
import plotly.express as px

DATA_PATH = "proccessed_sales_data.csv"
app = Dash()

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
    "Sales": sales
})

fig = px.line(dataFrame, x='Date', y='Sales')

app.layout = html.Div(children=[
    html.H1(children='Sales Data'),

    html.Div(children='''
        The sales data for Pink Morsels
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
