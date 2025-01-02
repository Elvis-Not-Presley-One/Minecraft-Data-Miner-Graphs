
import plotly.graph_objs as go

class ThreeDGraphs:

    def __init__(self, x_cord, y_cord, z_cord, name, color, pat, unique_names):
        """
        This is the constructor for the ThreeDGraphs class, initialized all attributes,
        and creates the base figure that will be added onto later on

        :param x_cord: the x cord list from pandas
        :param y_cord: the y cord list from pandas
        :param z_cord: the z cord list from pandas
        :param name: the main name/msg list from pandas
        :param color: the color list from pandas
        :param pat: the pat list from pandas
        :param unique_names: the list of unique names/msg from pandas
        """
        try:
            self.__x = x_cord
            self.__y = y_cord
            self.__z = z_cord
            self.__name = name
            self.__color = color
            self.__pat = pat
            self.__unique_names = unique_names

            self.__fig = go.Figure()

            # hideous peace of code for the hover text but I need to do it this way or I cant have it split up
            self.__hover_text = [
                (f"Name: {self.__name[i]}<br>X: {self.__x[i]}<br>Y: {self.__y[i]}<br>Z: {self.__z[i]}<br>Color:,"
                 f" {self.__color[i]}<br>Pat: {self.__pat[i]}")
                for i in range(len(self.__x))
            ]
        except Exception as e:
            raise RuntimeError(f"Error initializing 3d Grpahs: {e}")


    def scatter_Plot(self):
        """
        this function creates the scatter plot
        :return: Nothing
        """
        try:
            x = self.__x
            y = self.__y
            z = self.__z

            # creates title marker type color and text with a scale
            self.__fig = go.Figure(data=[go.Scatter3d(
                x=x,
                y=z,
                z=y,
                mode='markers',
                text=self.__hover_text,
                hoverinfo="text",
                marker=dict(
                    size=8,
                    color=y,
                    colorscale='rdbu',
                    opacity=0.8,
                    showscale=True,
                    colorbar=dict(
                        title='Y-Level',
                        titleside='top'
                    )
                )
            )])
        except Exception as e:
            raise RuntimeError(f"Error creating the first plot: {e}")

    def add_Drop_Downs(self):
        """
        the add_drop_downs function adds all the drop-down menus and also they styling
        :return: notiing
        """
        # creates an automatic args to be able to filter out info basically creating traces
        try:
            filter_buttons = [
                dict(
                    args=[{

                        'x': [[self.__x[i] for i in range(len(self.__name)) if self.__name[i] == unique_name]],
                        'y': [[self.__z[i] for i in range(len(self.__name)) if self.__name[i] == unique_name]],
                        'z': [[self.__y[i] for i in range(len(self.__name)) if self.__name[i] == unique_name]],
                        'text': [[self.__hover_text[i] for i in range(len(self.__name)) if self.__name[i] == unique_name]]
                    }],

                    label=unique_name,
                    method="update"
                )
                    for unique_name in self.__unique_names
            ]

            filter_buttons.insert(0, dict(
                args=[{
                    'x': [self.__x],
                    'y': [self.__z],
                    'z': [self.__y],
                    'text': [self.__hover_text]
                }],
                label='all',
                method='update'

            ))

            # create a drop down with the button name and what it does
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
        except Exception as e:
            raise RuntimeError(f"Error with adding dropdowns: {e}" )

    def show(self):
        """
        the show method shows the figure
        :return: nothing
        """
        self.__fig.show()

    def html(self, name_of_file):
        """
        the html function creates and html file of the graph
        :param name_of_file: a str of the name of the file NOTE * Needs .html at the end
        :return: nothing
        """

        #if there's any issue with the html like input name raise and error
        try:
            self.__fig.write_html(name_of_file)
        except Exception as e:
            raise IOError(f"Error Saving The file '{name_of_file}' {e}")


