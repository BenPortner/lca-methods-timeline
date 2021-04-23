import pandas as pd
import plotly.graph_objs as go
import numpy as np
import plotly.io as pio

def draw_circles(df, fig, **kwargs):
    h = go.Scatter(x=df['release year'], y=df['y'], mode='markers', **kwargs)
    fig.add_trace(h)

def draw_vertical_lines(df, fig, **kwargs):
    # add one vertical line per year

    for name, group in df.groupby('release year'):
        x = group.iloc[0]['release year']
        y = group['y'].max()
        fig.add_shape(type="line", **kwargs, x0=x, y0=0, x1=x, y1=y)

def draw_text_labels(df, fig, **kwargs):
    for i, row in df.iterrows():
        fig.add_annotation(text=row['name'], x=row['release year'], y=row['y'], xanchor='left',
                           showarrow=False, **kwargs)

def draw_x_axis(xs, fig, line_kwargs, arrow_kwargs, tick_kwargs, axis_padding=(4,5)):
    x_max = xs.max()+axis_padding[1]
    # line
    fig.add_shape(type="line", x0=xs.min()-axis_padding[0], y0=0, x1=x_max, y1=0, **line_kwargs)
    # arrow head
    fig.add_annotation(x=x_max+0.1, y=0, ay=0, **arrow_kwargs)
    # x ticks
    for x in xs.unique():
        fig.add_annotation(text=str(x), x=x, ax=0, **tick_kwargs)


def calculate_y_coordinates(xs, min_distance=4, y_offset=1):
    # calculate y coordinates for circles

    y = np.zeros(len(xs),)
    layer = 0
    blocks = pd.DataFrame(columns=range(xs.min(),xs.max()+1), data=True, index=range(len(xs)))
    for i,x in enumerate(xs):
        x_range = list(range(x,x+min_distance))
        # find first free layer
        layer = blocks[x].idxmax()
        y[i] = y_offset + layer * y_offset
        # block this layer for `min_distance` steps
        blocks.loc[layer,x_range] = False
        pass
    return y

if __name__ == "__main__":

    # read data
    df = pd.read_json('../methods.json')

    # sort ascending years
    df = df.sort_values(by=['release year','name'], ascending=True)


    # create hover info
    hover = '<br>'.join([str(c)+': %{customdata['+str(i)+']}' for i,c in enumerate(df.columns)])
    hoverdata = df.fillna(' - ').values


    # make figure
    fig = go.Figure()


    # calculate y-coordinates for circles
    xs = df['release year']
    df['y'] = calculate_y_coordinates(xs, min_distance=4, y_offset=1)


    # draw one circle for each method
    template = 'plotly_white'
    color = pio.templates[template]['layout']['colorway'][0]
    circle_kwargs = {
        'hovertemplate': hover,
        'customdata': hoverdata,
        'marker': {'size': 10, 'color':color},
    }
    draw_circles(df, fig, **circle_kwargs)


    # add method names as text labels
    text_kwargs = {
        'xshift': 8,
        'bgcolor': 'rgba(255,255,255,0.5)'
    }
    draw_text_labels(df, fig, **text_kwargs)


    # draw vertical line to the x-axis
    vline_kwargs = {
        'line': {'color':'rgba(0, 0, 0, 0.2)', 'width':4}
    }
    draw_vertical_lines(df, fig, **vline_kwargs)


    # draw x-axis
    line_kwargs = {'line':{'color':circle_kwargs['marker']['color'], 'width':4}}
    arrow_kwargs = dict(showarrow=True, arrowhead=5, arrowsize=4,
                       arrowcolor=color, ax=-1000)
    tick_kwargs = dict(y=df['y'].abs().min() * 0.1, showarrow=True,
                       arrowhead=0, textangle=-45, ay=30,
                       arrowwidth=vline_kwargs['line']['width'],
                       arrowcolor=vline_kwargs['line']['color'])
    draw_x_axis(xs, fig, line_kwargs, arrow_kwargs, tick_kwargs, axis_padding=(4, 5))


    # hide default x and y-axes
    # hide legend
    # use plotly_white template
    # increase font size
    fig.update_layout({
        'yaxis': {
            'showgrid': False,
            'zeroline': False,
            'visible': False,
        },
        'xaxis': {
            'showgrid': False,
            'zeroline': False,
            'visible': False,
        },
        'showlegend':False,
        'template': template,
        'font_size': 15
    })

    # save as html
    fig.write_html('timeline.html')
    pass