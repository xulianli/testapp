from dash import *
from testapp import *

app = Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H1('You work'),
    github_info_header(),
    html.Img(src="assets/batman.png")
])

if __name__ == '__main__':
    app.run_server(debug=True)






