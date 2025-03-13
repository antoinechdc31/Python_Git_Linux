import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import os

def load_data_from_csv(file_path):
    df = pd.read_csv(file_path, sep=',', header=0)
    df.columns = ['timestamp', 'USD/GBP','USD/CAD','USD/EUR','USD/AUD','GBP/USD','GBP/CAD','GBP/EUR','GBP/AUD',
                  'CAD/USD','CAD/GBP','CAD/EUR','CAD/AUD','EUR/USD','EUR/GBP','EUR/CAD','EUR/AUD',
                  'AUD/USD','AUD/GBP','AUD/CAD','AUD/EUR']
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

REPORTS_DIR = "/home/azureuser/scraping_dir/reports/"
def load_latest_report():
    report_files = sorted([f for f in os.listdir(REPORTS_DIR) if f.startswith("report_")], reverse=True)
    if report_files:
        with open(os.path.join(REPORTS_DIR, report_files[0]), "r") as file:
            return file.read()
    return "No report available."

currency_pairs = [
    'USD/GBP', 'USD/CAD', 'USD/EUR', 'USD/AUD',
    'GBP/USD', 'GBP/CAD', 'GBP/EUR', 'GBP/AUD',
    'CAD/USD', 'CAD/GBP', 'CAD/EUR', 'CAD/AUD',
    'EUR/USD', 'EUR/GBP', 'EUR/CAD', 'EUR/AUD',
    'AUD/USD', 'AUD/GBP', 'AUD/CAD', 'AUD/EUR'
]
app = dash.Dash(__name__, external_stylesheets=[
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css",
    "https://fonts.googleapis.com/css2?family=Bodoni+Moda:wght@400;700&display=swap"
])

app.layout = html.Div(style={"backgroundColor": "#0a192f", "color": "#FFFDE7", "fontFamily": "'Bodoni Moda', Didot, serif"}, children=[
    html.H1("FX Exchange Rates Dashboard", className="text-center mt-4", style={"fontWeight": "600"}),
    html.P("Stay informed with real-time exchange rate data. This dashboard provides key information on currency trends, including volatility and daily returns. You can consult our daily reports on our website, which summarize the day's news in a short summary for each currency pair. This site has been created for information purposes only and does not represent financial advice of any kind.", style={"marginLeft": "20px", "marginRight": "20px", "textAlign": "left", "color": "#FFFDE7"}),

    html.Div(className="container mt-3", children=[
        html.Label("Select Currency Pair:", className="form-label", style={"fontWeight": "400", "fontSize": "18px"}),
        dcc.Dropdown(
            id="currency-pair-dropdown",
            options=[{"label": pair, "value": pair} for pair in currency_pairs],
            value="USD/EUR",
            clearable=False,
            className="mb-3",
            style={
            "backgroundColor": "#FFFDE7",
            "color": "#000000",
            "fontWeight": "600",
            "textAlign": "center", 
	    },

        ),
        dcc.Graph(id="currency-pair-graph")
    ]),

    html.Div(className="container mt-4", children=[
        html.Div(className="row justify-content-center", children=[
            html.Div(className="col-md-3", children=[
                html.Div(className="card text-white shadow-sm", style={"backgroundColor": "#13568E", "borderRadius": "0px", "color": "#FFFDE7"}, children=[
                    html.Div(className="card-body text-center", children=[
                        html.H5("High", className="card-title",style={"color": "#FFFDE7"}),
                        html.H3(id="high-value", style={"fontWeight": "600", "color": "#FFFDE7"})
                    ])
                ])
            ]),
            html.Div(className="col-md-3", children=[
                html.Div(className="card text-white shadow-sm", style={"backgroundColor": "#13568E", "borderRadius": "0px", "color": "#FFFDE7"}, children=[
                    html.Div(className="card-body text-center", children=[
                        html.H5("Low", className="card-title",style={"color": "#FFFDE7"}),
                        html.H3(id="low-value", style={"fontWeight": "600","color": "#FFFDE7"})
                    ])
                ])
            ]),
            html.Div(className="col-md-3", children=[
                html.Div(className="card text-white shadow-sm", style={"backgroundColor": "#13568E", "borderRadius": "0px",  "color": "#FFFDE7"}, children=[
                    html.Div(className="card-body text-center", children=[
                        html.H5("Volatility", className="card-title",style={"color": "#FFFDE7"}),
                        html.H3(id="volatility-value", style={"fontWeight": "600","color": "#FFFDE7"})
                    ])
                ])
            ]),
            html.Div(className="col-md-3", children=[
                html.Div(className="card text-white shadow-sm", style={"backgroundColor": "#13568E", "borderRadius": "0px", "color": "#FFFDE7"}, children=[
                    html.Div(className="card-body text-center", children=[
                        html.H5("Daily Return", className="card-title",style={"color": "#FFFDE7"}),
                        html.H3(id="return-value", style={"fontWeight": "600","color": "#FFFDE7"})
                    ])
                ])
            ])
        ])
    ]),

    html.Div(className="container mt-4", children=[
        html.H3("Daily Report", className="text-center"),
        html.Pre(id="daily-report", className="p-3 bg-dark text-white", style={"whiteSpace": "pre-wrap", "borderRadius": "0px"})
    ]),

    dcc.Interval(
        id='interval-component',
        interval=5*60*1000,
        n_intervals=0
    )
])
def update_report(n_intervals):
    return load_latest_report()
@app.callback(
    [Output("currency-pair-graph", "figure"),
     Output("high-value", "children"),
     Output("low-value", "children"),
     Output("volatility-value", "children"),
     Output("return-value", "children"),
     Output("daily-report", "children")],
    [Input("currency-pair-dropdown", "value"),
     Input("interval-component", "n_intervals")]
)
def update_dashboard(currency_pair, n_intervals):
    data = load_data_from_csv('/home/azureuser/scraping_dir/data/exchange_rates.csv')
    filtered_data = data[['timestamp', currency_pair]].dropna()
    filtered_data = filtered_data[filtered_data[currency_pair] != filtered_data[currency_pair].iloc[0]]
    
    if filtered_data.empty:
        return px.line(title="No Data Available"), "N/A", "N/A", "N/A", "No data available"
    filtered_data['return'] = filtered_data[currency_pair].pct_change()

    if filtered_data.empty:
        return px.line(title="No Data Available"), "N/A", "N/A", "N/A", "No data available"


    daily_return = round(filtered_data['return'].iloc[-1] * 100, 4) if len(filtered_data) > 1 else 0


    fig = px.line(filtered_data, x="timestamp", y=currency_pair,
                  title=f"Exchange Rates for {currency_pair}",
                  labels={"value": "Exchange Rate", "timestamp": "Time"},
                  template="plotly_dark")
    fig.update_traces(line=dict(color="#13568E"))
    fig.update_layout(
        plot_bgcolor="#FFFDE7",
        paper_bgcolor="#FFFDE7",
        font=dict(color="#0a192f",family="Bodoni Moda"),
        title_font=dict(color="#0a192f",family="Bodoni Moda"),
        xaxis=dict(
            showgrid=True,
            gridcolor="rgba(0,0,0,0.1)",  
            tickfont=dict(color="#0a192f",family="Bodoni Moda"),
            title_font=dict(color="#0a192f",family="Bodoni Moda")
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(0,0,0,0.1)",
            tickfont=dict(color="#0a192f",family="Bodoni Moda"),
            title_font=dict(color="#0a192f",family="Bodoni Moda")
        )
    )
    high_rate = round(filtered_data[currency_pair].max(), 4)
    low_rate = round(filtered_data[currency_pair].min(), 4)
    volatility = round(filtered_data[currency_pair].std(), 4)

    return fig, high_rate, low_rate, volatility, f"{daily_return}%", load_latest_report()
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)

