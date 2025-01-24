import plotly.graph_objs as go
import pandas as pd
import plotly.express as px

class Shulkers:

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
            color='y',
            color_continuous_scale='rdbu',
            title='2D Scatter Plot of Shulker Data',
            labels={'x': 'X Coordinate', 'Y': 'Y Coordinate', 'z': 'Z Coordinate', 'Name': 'Name', 'id': 'id'},
            opacity=0.8,
            hover_data={'x': True, 'y': True, 'z': True, 'Name': True, 'id': True}  # Show all values in hover tooltip
        )

        # Update layout to include color scale and buttons
        self.fig.update_layout(
            template='plotly_dark',
            width=1000,
            height=700,
            margin=dict(l=50, r=50, t=50, b=50),
            coloraxis_colorbar=dict(
                title='y',
                titleside='right',
                tickmode='array',
                tickvals=[self.df['y'].min(), self.df['y'].max()],
                ticktext=[f"Min: {self.df['y'].min()}", f"Max: {self.df['y'].max()}"]
            ),

        )

    def show(self, output_html=None):
        """
        Show the plot and optionally save it to an HTML file.
        """
        self.fig.show()
        self.fig.write_html(output_html)
