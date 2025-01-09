import os
import sqlite3
import pandas as pd
import datashader as ds
import datashader.transfer_functions as tf
import matplotlib.pyplot as plt
from colorcet import glasbey_category10



class Biomes:
    """
    NOTE* This Class does not work properly
    Needs work on, at this point the biomes bs is not working well for me
    """
    def __init__(self, csv_file, db_file="data.db"):
        self.csv_file = csv_file
        self.db_file = db_file
    def load_csv_to_sqlite(self):
        if not os.path.exists(self.csv_file):
            raise FileNotFoundError(f"CSV file {self.csv_file} does not exist.")

        connection = sqlite3.connect(self.db_file)
        chunk_size = 10 ** 6  # Adjust based on memory capacity

        try:
            for chunk in pd.read_csv(self.csv_file, header=None, chunksize=chunk_size):
                chunk.columns = ['x_coordinate', 'z_coordinate', 'biome']
                chunk.to_sql("biomes", connection, if_exists="append", index=False)
        finally:
            connection.close()

    def fetch_all_data(self):
        connection = sqlite3.connect(self.db_file)
        try:
            query = "SELECT x_coordinate, z_coordinate, biome FROM biomes"
            return pd.read_sql_query(query, connection)
        finally:
            connection.close()

    def generate_datashader_image(self, output_image):
        print("Fetching data from SQLite...")
        df = self.fetch_all_data()

        print("Creating Datashader canvas...")
        cvs = ds.Canvas(plot_width=1000, plot_height=1000)
        agg = cvs.points(df, x="x_coordinate", y="z_coordinate", agg=ds.count_cat("biome"))

        print("Shading the data...")
        biome_colors = glasbey_category10  # Predefined color palette for categories
        img = tf.shade(agg, color_key=dict(zip(df['biome'].unique(), biome_colors)))

        print("Saving the image...")
        img.to_pil().save(output_image)
        print(f"Image saved to {output_image}")

    def generate_plotly_overlay(self, output_image, output_html):
        """
        Overlay Datashader raster output onto a Plotly figure for interactivity.
        """
        import plotly.graph_objects as go
        from PIL import Image

        # Load the Datashader image
        img = Image.open(output_image)

        # Create a blank Plotly figure
        fig = go.Figure()

        # Overlay the rasterized image
        fig.add_trace(go.Image(z=img))

        # Customize layout for interactivity
        fig.update_layout(
            title="Biome Distribution with Datashader",
            xaxis=dict(title="X Coordinate"),
            yaxis=dict(title="Z Coordinate"),
        )

        # Save and show
        fig.write_html(output_html)
        fig.show()
        print(f"Plotly figure saved to {output_html}")
