import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

############# Make changes here


app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Graphs are awesome for conveying information'),
    dcc.Graph(
        id='this_is_an_id',
        figure={
            'data': [
                {'x': ['Music', 'Podcasts', 'Audio Books'], 'y': [8, 2, 3], 'type': 'bar', 'name': 'Intelligence'},
                {'x': ['Music', 'Podcasts', 'Audio Books'], 'y': [7, 1, 5], 'type': 'bar', 'name': 'Beauty'},
            ],
            'layout': {
                'title': "Much wow!",
                'xaxis':{'title':'Choice of data visualization'},
                'yaxis':{'title':'Approval rating by average data scientist'},
            }
        }
    )]
)


###### Don't change anything here



if __name__ == '__main__':
    app.run_server()
