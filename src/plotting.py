import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

def plot_graph(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    figsize=(7, 3),
    linewidth=1
):
    """
    Create a publication-quality x vs y plot.
    """

    mpl.rcParams['font.family'] = 'Arial'
    mpl.rcParams['font.size'] = 12

    fig, ax = plt.subplots(figsize=figsize, dpi=300)

    ax.plot(df[x_col], df[y_col], color='black', linewidth=linewidth)

    # Axes styling
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('black')
    ax.spines['bottom'].set_color('black')

    ax.tick_params(axis='both', colors='black')

    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    ax.grid(False)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    return fig
