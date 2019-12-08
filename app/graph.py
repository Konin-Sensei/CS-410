import plotly
import plotly.graph_objs as go
import json

def create_plot2(df):
    m = df.groupby(['LOSS_LOC_ST_ABBR'])['CLM_TTL_INC_AMT'].agg('sum').reset_index()
    trace = go.Choropleth(
        locations=m['LOSS_LOC_ST_ABBR'],
        z=m['CLM_TTL_INC_AMT'],
        locationmode='USA-states',
        colorscale='Reds',
        colorbar_title="Total Claims Cost",
    )
    data = [trace]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def create_plot(df):
    m = df.groupby(['LOSS_LOC_ST_ABBR'])['CLM_TTL_INC_AMT'].agg('sum').reset_index()
    data = [
        go.Bar(
            x=m['LOSS_LOC_ST_ABBR'],
            y=m['CLM_TTL_INC_AMT'],
        )
    ]

    graph1JSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graph1JSON