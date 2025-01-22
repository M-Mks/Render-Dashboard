import plotly.express as px
import pandas as pd
from dash import html, dcc
import matplotlib.pyplot as plt
from assets.layouts import GRAPH_LAYOUT

def create_pie_chart(df, question):
    fig = px.pie(df, names=question, title=f"{question}".replace("/", "<br>"))
    fig.update_traces(marker=dict(colors=px.colors.sequential.Blues_r))
    fig.update_layout(title=None, legend=GRAPH_LAYOUT["legend"], **GRAPH_LAYOUT["general"])

    title_html = html.Div(
        f"{question}".replace("/", "<br>"),
        style={
            'textAlign': 'center', 'fontSize': '20px', 'color': '#1f2a44',
            'fontFamily': 'Helvetica, Arial, sans-serif', 'fontWeight': 'normal', 'marginBottom': '2px'
        }
    )
    return html.Div([title_html, dcc.Graph(figure=fig)])

def create_multi_select_pie_chart(df, question):
    options = df[question].dropna().str.split(",").explode().str.strip()
    unique_options = sorted(options.unique())
    option_counts = pd.DataFrame({
        "Option": unique_options,
        "Count": [options.tolist().count(opt) for opt in unique_options]
    })
    fig = px.pie(
        option_counts, names="Option", values="Count", 
        color="Option", color_discrete_map={
            option: px.colors.sequential.Blues_r[i % len(px.colors.sequential.Blues_r)] 
            for i, option in enumerate(unique_options)
        },
        category_orders={"Option": unique_options}
    )
    fig.update_layout(title=None, legend=GRAPH_LAYOUT["legend"], **GRAPH_LAYOUT["general"])
    
    title_html = html.Div(
        f"{question}".replace("/", "<br>"),
        style={
            'textAlign': 'center', 'fontSize': '20px', 'color': '#1f2a44',
            'fontFamily': 'Helvetica, Arial, sans-serif', 'fontWeight': 'normal', 'marginBottom': '2px'
        }
    )
    return html.Div([title_html, dcc.Graph(figure=fig)])

def create_numeric_pie_chart(df, question, value_mapping, category_order):
    value_counts = df[question].map(value_mapping).value_counts()
    value_counts = value_counts.reindex(category_order, fill_value=0).reset_index()
    value_counts.columns = ["Value", "Count"]
    fig = px.pie(
        value_counts, names="Value", values="Count", 
        color="Value", color_discrete_sequence=px.colors.sequential.Blues_r, 
        category_orders={"Value": category_order}
    )
    fig.update_layout(title=None, legend=GRAPH_LAYOUT["legend"], **GRAPH_LAYOUT["general"])
    
    title_html = html.Div(
        f"{question}".replace("/", "<br>"),
        style={
            'textAlign': 'center', 'fontSize': '20px', 'color': '#1f2a44',
            'fontFamily': 'Helvetica, Arial, sans-serif', 'fontWeight': 'normal', 'marginBottom': '2px'
        }
    )
    return html.Div([title_html, dcc.Graph(figure=fig)])

def create_ordered_pie_chart(df, question, category_order):
    value_counts = df[question].value_counts()
    value_counts = value_counts.reindex(category_order, fill_value=0).reset_index()
    value_counts.columns = ["Value", "Count"]
    fig = px.pie(
        value_counts, names="Value", values="Count", 
        color="Value", color_discrete_sequence=px.colors.sequential.Blues_r, 
        category_orders={"Value": category_order}
    )
    fig.update_layout(title=None, legend=GRAPH_LAYOUT["legend"], **GRAPH_LAYOUT["general"])
    
    title_html = html.Div(
        f"{question}".replace("/", "<br>"),
        style={
            'textAlign': 'center', 'fontSize': '20px', 'color': '#1f2a44',
            'fontFamily': 'Helvetica, Arial, sans-serif', 'fontWeight': 'normal', 'marginBottom': '2px'
        }
    )
    return html.Div([title_html, dcc.Graph(figure=fig)])
pass