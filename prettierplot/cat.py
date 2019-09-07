import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm

import prettierplot.style as style
import prettierplot.util as util


import textwrap


def prettyBarV(self, x, counts, color=style.styleGrey, xLabels=None, xTickWrap = True, labelRotate=0,
                yUnits="f", ax=None):
    """
    Documentation:
        Description:
            Create vertical bar plot.
        Parameters:
            x : array
                1-dimensional array of values to be plotted on x-axis representing distinct categories.
            counts : array or string
                1-dimensional array of value counts for categories.
            color : string (some sort of color code), default = style.styleHexMid[0]
                Bar color.
            xLabels : list, default = None
                Custom x-axis text labels.
            xTickWrap : boolean, default = True
                Wrap x-axis tick labels.
            labelRotate : float or int, default = 0
                Degrees by which the xtick labels are rotated.
            yUnits : string, default = 'f'
                Determines units of y-axis tick labels. 's' displays string. 'f' displays float. 'p' displays
                percentages, 'd' displays dollars. Repeat character (e.g 'ff' or 'ddd') for additional
                decimal places.
            ax : Axes object, default = None
                Axis on which to place visual.
    """
    # custom labela
    labels = xLabels if xLabels is not None else x

    # create vertical bar plot.
    plt.bar(
        x=x,
        height=counts,
        color=color,
        tick_label=labels,
        alpha=0.8,
    )

    # rotate x-tick labels.
    plt.xticks(rotation=labelRotate)

    # resize x-axis labels as needed.
    if len(x) > 10 and len(x) <= 20:
        ax.tick_params(axis="x", colors=style.styleGrey, labelsize=1.0 * self.chartProp)
    elif len(x) > 20:
        ax.tick_params(axis="x", colors=style.styleGrey, labelsize=0.9 * self.chartProp)
    else:
        ax.tick_params(axis="x", colors=style.styleGrey, labelsize=1.2 * self.chartProp)

    if xTickWrap and type(labels):
        try:
            x = ['\n'.join(textwrap.wrap(i.replace('_'," "),12)) for i in labels]
            ax.set_xticklabels(x)
        except AttributeError:
            pass

    # format y ticklabels
    ax.set_yticklabels(
        ax.get_yticklabels() * 100 if "p" in yUnits else ax.get_yticklabels(),
        rotation=0,
        fontsize=1.2 * self.chartProp,
        color=style.styleGrey,
    )

    # use label formatter utility function to customize chart labels.
    util.utilLabelFormatter(ax=ax, yUnits=yUnits)


def prettyBarH(self, y, counts, color=style.styleGrey, labelRotate=45, xUnits="f", ax=None):
    """
    Documentation:
        Description:
            Create vertical bar plot.
        Parameters:
            y : array
                1-dimensional array of values to be plotted on x-axis representing distinct categories.
            counts : array or string
                1-dimensional array of value counts for categories.
            color : string (some sort of color code), default = style.styleHexMid[0]
                Bar color.
            labelRotate : float or int, default = 45
                Degrees by which the xtick labels are rotated.
            xUnits : string, default = 'f'
                Determines units of x-axis tick labels. 's' displays string. 'f' displays float. 'p' displays
                percentages, 'd' displays dollars. Repeat character (e.g 'ff' or 'ddd') for additional
                decimal places.
            ax : Axes object, default = None
                Axis on which to place visual.
    """
    # plot horizontal bar plot.
    plt.barh(y=y, width=counts, color=color, tick_label=y, alpha=0.8)

    # rotate x-tick labels.
    plt.xticks(rotation=labelRotate)

    ax.set_xticklabels(
        ax.get_xticklabels() * 100 if "p" in xUnits else ax.get_xticklabels(),
        rotation=0,
        fontsize=0.9 * self.chartProp,
        color=style.styleGrey,
    )

    # use label formatter utility function to customize chart labels.
    util.utilLabelFormatter(ax=ax, xUnits=xUnits)


def prettyBoxPlotV(self, x, y, data, color, labelRotate=0, yUnits="f", colorMap="viridis", ax=None):
    """
    Documentation:
        Description:
            Create vertical box plots. Useful for evaluated a continuous target on the y-axis
            vs. several different category segments on the x-axis
        Parameters:
            x : string
                Name of independent variable in dataframe. Represents a category.
            y : string
                Name of continuous target variable.
            data : Pandas DataFrame
                Pandas DataFrame including both indpedent variable and target variable.
            color : string
                Determines color of box plot figures. Ideally this object is a color palette,
                which can be a default seaborn palette, a custom seaborn palette, or a custom
                matplotlib cmap.
            labelRotate : float or int, default = 45
                Degrees by which the xtick labels are rotated.
            yUnits : string, default = 'f'
                Determines units of y-axis tick labels. 's' displays string. 'f' displays float. 'p' displays
                percentages, 'd' displays dollars. Repeat character (e.g 'ff' or 'ddd') for additional
                decimal places.
            colorMap : string specifying built-in matplotlib colormap, default = "viridis"
                Colormap from which to draw plot colors.
            ax : Axes object, default = None
                Axis on which to place visual.
    """
    # create vertical box plot.
    g = sns.boxplot(
        x=x,
        y=y,
        data=data,
        orient="v",
        palette=sns.color_palette(style.colorGen(colorMap, num=len(np.unique(data[x].values)))), ax=ax
    ).set(xlabel=None, ylabel=None)

    # resize x-axis labels as needed.
    unique = np.unique(data[x])
    if len(unique) > 10 and len(unique) <= 20:
        ax.tick_params(axis="x", labelsize=0.9 * self.chartProp)
    elif len(unique) > 20:
        ax.tick_params(axis="x", labelsize=0.9 * self.chartProp)

    # fade box plot figures by reducing alpha.
    plt.setp(ax.artists, alpha=0.8)

    # rotate x-tick labels.
    plt.xticks(rotation=labelRotate)
    ax.yaxis.set_visible(True)

    # use label formatter utility function to customize chart labels.
    util.utilLabelFormatter(ax=ax, yUnits=yUnits)


def prettyBoxPlotH(self, x, y, data, color=style.styleGrey, xUnits="f", bbox=(1.05, 1), colorMap="viridis", ax=None):
    """
    Documentation:
        Description:
            Create horizontal box plots. Useful for evaluating a categorical target on the y-axis
            vs. a continuous independent variable on the x-axis.
        Parameters:
            x : string
                Name of independent variable in dataframe. Represents a category.
            y : string
                Name of continuous target variable.
            data : Pandas DataFrame
                Pandas DataFrame including both indpedent variable and target variable.
            color : string (some sort of color code), default = style.styleHexMid
                Determines color of box plot figures. Ideally this object is a color palette,
                which can be a default seaborn palette, a custom seaborn palette, or a custom
                matplotlib cmap.
            xUnits : string, default = 'f'
                Determines units of x-axis tick labels. 's' displays string. 'f' displays float. 'p' displays
                percentages, 'd' displays dollars. Repeat character (e.g 'ff' or 'ddd') for additional
                decimal places.
            bbox : tuple of floats, default = (1.05, 1.0)
                Coordinates for determining legend position.
            colorMap : string specifying built-in matplotlib colormap, default = "viridis"
                Colormap from which to draw plot colors.
            ax : Axes object, default = None
                Axis on which to place visual.
    """
    # create horizontal box plot.
    g = sns.boxplot(
        x=x,
        y=y,
        hue=y,
        data=data,
        orient="h",
        palette=sns.color_palette(style.colorGen(colorMap, num=len(np.unique(data[y].values)))),
        # palette=sns.color_palette(style.colorGen(colorMap, num=len(np.unique(y)))),
        ax=ax,
    ).set(xlabel=None, ylabel=None)

    # fade box plot figures by reducing alpha.
    plt.setp(ax.artists, alpha=0.8)
    ax.yaxis.set_visible(False)

    # use label formatter utility function to customize chart labels.
    util.utilLabelFormatter(ax=ax, xUnits=xUnits)

    # legend placement.
    plt.legend(bbox_to_anchor=bbox, loc=2, borderaxespad=0.0)