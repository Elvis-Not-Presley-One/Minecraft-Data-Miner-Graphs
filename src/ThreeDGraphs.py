from collections import defaultdict
import numpy as np
import plotly.graph_objs as go

class ThreeDGraphs:

    def __init__(self, x_cord, y_cord, z_cord, name, a_color, pat, unique_names, banners=False):
        self.__x, self.__y, self.__z = x_cord, y_cord, z_cord
        self.__name, self.__color, self.__pat = name, a_color, pat
        self.__unique_names = unique_names

        self.__hover_text = self.__generate_hover_text(banners)
        self.__fig = go.Figure()

        self.__filtered_data = {
            unique_name: {
                'x': [self.__x[i] for i, name in enumerate(self.__name) if name == unique_name],
                'y': [self.__z[i] for i, name in enumerate(self.__name) if name == unique_name],
                'z': [self.__y[i] for i, name in enumerate(self.__name) if name == unique_name],
                'text': [self.__hover_text[i] for i, name in enumerate(self.__name) if name == unique_name]
            }
            for unique_name in self.__unique_names
        }
        self.__filtered_data['all'] = {
            'x': self.__x,
            'y': self.__z,
            'z': self.__y,
            'text': self.__hover_text
        }

    def __generate_hover_text(self, banners):
        hover_template = (
            lambda n, x, y, z, c, p: f"Msg: {n}<br>X: {x}<br>Y: {y}<br>Z: {z}<br>Glow Ink: {c}<br>Sign Color: {p}"
            if not banners else
            lambda n, x, y, z, c, p: f"Name: {n}<br>X: {x}<br>Y: {y}<br>Z: {z}<br>Color: {c}<br>Pat: {p}"
        )
        return [hover_template(n, x, y, z, c, p) for n, x, y, z, c, p in zip(self.__name, self.__x, self.__y, self.__z, self.__color, self.__pat)]

    def scatter_Plot(self):
        try:
            print('Start of the Scatter Plot')
            self.__fig = go.Figure(data=[go.Scatter3d(
                x=self.__x,
                y=self.__z,
                z=self.__y,
                mode='markers',
                text=self.__hover_text,
                hoverinfo="text",
                marker=dict(
                    size=8,
                    color=self.__y,
                    colorscale='rdbu',
                    opacity=0.8,
                    showscale=True,
                    colorbar=dict(
                        title='Y-Level',
                        titleside='top'
                    )
                )
            )])

            print("filter buttons begin ")
            filter_buttons = [
                dict(
                    args=[{
                        'x': [self.__filtered_data[unique_name]['x']],
                        'y': [self.__filtered_data[unique_name]['y']],
                        'z': [self.__filtered_data[unique_name]['z']],
                        'text': [self.__filtered_data[unique_name]['text']]
                    }],
                    label=unique_name,
                    method="update"
                )
                for unique_name in self.__unique_names
            ]

            filter_buttons.insert(0, dict(
                args=[{
                    'x': [self.__filtered_data['all']['x']],
                    'y': [self.__filtered_data['all']['y']],
                    'z': [self.__filtered_data['all']['z']],
                    'text': [self.__filtered_data['all']['text']]
                }],
                label='all',
                method='update'
            ))

            print("Filter Buttons Inserted")

            # create a drop down with the button name and what it does
            print("Start adding buttons to the Graph")
            buttons_types = [
                dict(
                    args=['type', 'scatter3d'],
                    label='3d-Plot',
                    method='restyle'
                ),
                dict(
                    args=['type', 'scatter2d'],
                    label='2d-Plot',
                    method='restyle'
                ),
                dict(
                    args=['type', 'heatmap'],
                    label='heatmap',
                    method='restyle'
                ),
                dict(
                    args=['type', 'mesh3d'],
                    label='Mesh 3d Plot',
                    method='restyle'
                )
            ]

            # makes buttons do shit, and can style them here
            print("Start to update the layout")
            self.__fig.update_layout(
                template='plotly_dark',
                updatemenus=[
                    dict(
                        buttons=buttons_types,
                        direction='down',
                        pad={'r': 10, 't': 10},
                        showactive=True,
                        x=0.1,
                        xanchor='left',
                        y=1.15,
                        yanchor='top',
                        name='Plot Type: '
                    ),
                    dict(
                        buttons=filter_buttons,
                        direction='down',
                        pad={'r': 10, 't': 10},
                        showactive=True,
                        x=0.5,
                        xanchor='left',
                        y=1.15,
                        yanchor='top',
                        name='Filters'

                    ),

                ],

                # make text for the buttons to the side of them

                annotations=[
                    dict(text="Plot Types:", showarrow=False,
                         x=0.024, y=1.13, yref="paper", align="left"),
                    dict(text='Filters:', showarrow=False,
                         x=0.455, y=1.13, yref='paper', align='left')
                ],
                scene=dict(
                    xaxis_title='X Axis',
                    yaxis_title='z Axis',
                    zaxis_title='y Axis',
                ),
                width=1200,
                height=800,
                margin=dict(r=60, l=60, b=60, t=60)
            )
            print("Done with graph")
        except Exception as e:
            raise RuntimeError(f"Error creating the first plot: {e}")

    def show(self):
        self.__fig.show()
        self.__fig.write_html("Spawn Signs.html")


#"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

