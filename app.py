from dash import Dash, html, dcc, Input, Output
import altair as alt
from vega_datasets import data


# Read in global data
barley = data.barley()
cols_to_use = ['variety','site']

# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server
app.layout = html.Div([
    html.Iframe(
        id='bar',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='xcol-widget',
        value='variety',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in cols_to_use])])

# Set up callbacks/backend
@app.callback(
    Output('bar', 'srcDoc'),
    Input('xcol-widget', 'value'))
def plot_altair(xcol):
    chart = alt.Chart(barley).mark_bar().encode(
        x=xcol,
        y='mean(yield)',
        tooltip='mean(yield)').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)