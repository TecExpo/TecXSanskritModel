import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import re

app = dash.Dash(__name__)

def parse_logs(file_path):
    rows = []
    # Regex to extract: Date Time, Level (INFO/WARNING), and Message
    log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2}) \d{2}:\d{2}:\d{2} - (\w+) - (.*)')
    
    try:
        with open(file_path, 'r') as f:
            for line in f:
                match = log_pattern.search(line)
                if match:
                    date, level, msg = match.groups()
                    # Mark 'WARNING' as an escalation
                    rows.append({"Date": date, "Type": level, "IsEscalated": 1 if level == "WARNING" else 0})
        return pd.DataFrame(rows)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Type", "IsEscalated"])

app.layout = html.Div([
    html.H1("Sanskrit SLM Organizer Monitor"),
    dcc.Interval(id='interval-component', interval=60*1000, n_intervals=0), # Refresh every minute
    html.Div([
        dcc.Graph(id='escalation-rate-graph'),
        dcc.Graph(id='intent-pie-chart')
    ], style={'display': 'flex'})
])

@app.callback(
    [Output('escalation-rate-graph', 'figure'),
     Output('intent-pie-chart', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_metrics(n):
    df = parse_logs('processing_errors.log')
    if df.empty:
        return {}, {}

    # Calculate Daily Escalation Rate (%)
    daily_stats = df.groupby('Date')['IsEscalated'].mean().reset_index()
    daily_stats['Escalation Rate (%)'] = daily_stats['IsEscalated'] * 100
    
    line_fig = px.line(daily_stats, x='Date', y='Escalation Rate (%)', title='Daily SLM Escalation Rate')
    pie_fig = px.pie(df, names='Type', title='Local vs. Escalated Task Distribution')
    
    return line_fig, pie_fig

if __name__ == '__main__':
    app.run_server(debug=True)
