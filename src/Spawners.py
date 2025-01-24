import plotly.graph_objs as go
import pandas as pd
import plotly.express as px


class Spawners:
    def __init__(self, df):
        self.df = df
        self.fig = go.Figure()


    def create_plot(self):
        """
        Create a 3D scatter plot.
        """
        self.fig = px.scatter(
            self.df,
            x='x',
            y='z',
            color='delay',
            color_continuous_scale='rdbu',
            title='2D Scatter Plot of Spawner Data',
            labels={'x': 'X Coordinate', 'Y': 'Y Coordinate', 'z': 'Z Coordinate', 'delay': 'Delay'},
            opacity=0.8,
            hover_data={'x': True, 'y': True, 'z': True, 'delay': True}  # Show all values in hover tooltip
        )

        # Update layout to include color scale and buttons
        self.fig.update_layout(
            template='plotly_dark',
            width=1000,
            height=700,
            margin=dict(l=50, r=50, t=50, b=50),
            coloraxis_colorbar=dict(
                title='Delay',
                titleside='right',
                tickmode='array',
                tickvals=[self.df['delay'].min(), self.df['delay'].max()],
                ticktext=[f"Min: {self.df['delay'].min()}", f"Max: {self.df['delay'].max()}"]
            ),
            updatemenus=[
                {
                    'buttons': [
                        {
                            'label': 'Show All',
                            'method': 'update',
                            'args': [{'x': [self.df['x']], 'y': [self.df['z']], 'marker': {'color': self.df['delay']}}],
                        },
                        {
                            'label': 'Delay > 20',
                            'method': 'update',
                            'args': [{'x': [self.df[self.df['delay'] > 20]['x']],
                                      'y': [self.df[self.df['delay'] > 20]['z']],
                                      'marker': {'color': self.df[self.df['delay'] > 20]['delay']}}],
                        },
                        {
                            'label': 'Delay <= 20',
                            'method': 'update',
                            'args': [{'x': [self.df[self.df['delay'] <= 20]['x']],
                                      'y': [self.df[self.df['delay'] <= 20]['z']],
                                      'marker': {'color': self.df[self.df['delay'] <= 20]['delay']}}],
                        },
                        {
                            'label': 'Delay <= 1',
                            'method': 'update',
                            'args': [{'x': [self.df[self.df['delay'] <= 1]['x']],
                                      'y': [self.df[self.df['delay'] <= 1]['z']],
                                      'marker': {'color': self.df[self.df['delay'] <= 1]['delay']}}],
                        },
                        {
                            'label': '1.19+',
                            'method': 'update',
                            'args': [{'x': [self.df[self.df['delay'] <= 0]['x']],
                                      'y': [self.df[self.df['delay'] <= 0]['z']],
                                      'marker': {'color': self.df[self.df['y'] <= 0]['delay']}}],
                        },
                        {
                            'label': '<1.12',
                            'method': 'update',
                            'args': [{'x': [self.df[self.df['delay'] >= 0]['x']],
                                      'y': [self.df[self.df['delay'] >= 0]['z']],
                                      'marker': {'color': self.df[self.df['y'] >= 0]['delay']}}],
                        },
                    ],
                    'direction': 'down',
                    'showactive': True,
                    'x': 1.1,
                    'xanchor': 'left',
                    'y': 1.15,
                    'yanchor': 'top'
                }
            ]
        )


    def show(self, output_html=None):
            """
            Show the plot and optionally save it to an HTML file.
            """
            self.fig.show()
            self.fig.write_html(output_html)
