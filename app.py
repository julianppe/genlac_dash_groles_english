import dash
from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container

from dash_extensions.enrich import (
    DashProxy,
    MultiplexerTransform,
    html,
    dcc,
)

external_stylesheets = [dbc.themes.JOURNAL]

app = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    use_pages=True,
    prevent_initial_callbacks=True,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
)

server = app.server

GENLAC_LOGO = "/assets/genlac.png"

dropdown = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Political", header=True),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “Men make better political leaders than women do”", href="/"),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “Half of Parliament members are women”", href="/half-parliament"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Labor", header=True),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “When jobs are scarce, men should have more right to a job than women”", href="/right-job"),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “Men make better business executives than women do”", href="/executives"),
            dbc.DropdownMenuItem("Adult population that thinks that employers do not hire women with children", href="/employers-donot-mothers"),
            dbc.DropdownMenuItem("Adult population that thinks that a team composed of men and women achieves better outcomes than a team composed of only men", href="/balance-team"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Education", header=True),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “A university education is more important for a boy than for a girl”", href="/university"),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “women have the same capabilities for science and technology as men”", href="/science-capabilities"),
            dbc.DropdownMenuItem("Third-grade teachers who think that boys or girls learn faster math or language due to their innate characteristics", href="/learn-faster-3rd"),
            dbc.DropdownMenuItem("Sixth-grade teachers who think that boys or girls learn faster math, language or science due to their innate characteristics", href="/learn-faster-6th"),
            dbc.DropdownMenuItem("Percentage of 15 year-old students who expect to work in STEM-related occupations at the age of 30", href="/stem-15"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Family", header=True),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “If a woman earns more money than her husband, it’s almost certain to cause problems”", href="/woman-earns-more"),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “When a mother works for pay, the children suffer”", href="/mother-works"),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “Being a housewife is just as fulfilling as working for pay”", href="/housewife"),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “Women have to work for pay only if their husband does not earn enough”", href="/woman-work-husband"),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “It is better if man works and woman stays at home”", href="/woman-stays-man-work"),
            dbc.DropdownMenuItem("Percentage of women who think that husbands are justified to beat their wives in some situations", href="/justified-beat"),
        ],
        size="lg",
        nav=True,
        in_navbar=True,
        label="Indicators",
        className="ms-0",
        toggle_style={"color": "#460074"},
        align_end=False,
        style={'width':'100%'}

        )
    )
],
className="g-0 ms-auto flex-nowrap mt-5 mt-md-0",
align="center",
)


navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        dbc.Collapse(
                            dropdown, 
                            className="ml-auto",
                            id="navbar-collapse",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
        ],
    fluid=True),
    #outline=True, 
    color="light",
    dark=True,
)
# Definimos el layout:
app.layout = html.Div(
    [
        dcc.Store(id="store", data='Argentina'),
        dbc.Container([
    dbc.Row(
        [
            navbar # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True)
    ]
)


if __name__ == "__main__":
    app.run_server()