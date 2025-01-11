import matplotlib.pyplot as plt
import seaborn as sns


def set_plot_style():
    plt.style.use('seaborn-darkgrid')
    sns.set_context('paper')
    sns.set_palette('muted')