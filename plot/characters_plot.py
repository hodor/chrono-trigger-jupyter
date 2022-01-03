import matplotlib
import seaborn as sns


class ComparisonPlotter(object):
    def __init__(self, character_colors, width, height):
        self.character_colors = character_colors
        self.set_size(width, height)

    def get_character_line_colors(self):
        return self.character_colors

    def set_size(self, width, height):
        matplotlib.rcParams['figure.figsize'] = [width, height]
        sns.set(font_scale=1.5)

    def plot_line(self, data, title=None):
        sns.set_style("darkgrid")
        line = sns.lineplot(data=data, linewidth=2.5, palette=self.get_character_line_colors())
        if title is not None:
            line.set(title=title)


class DeltaComparisonPlotter(object):
    def __init__(self, character_colors, width, height):
        self.character_colors = character_colors
        self.line_plotter = ComparisonPlotter(self.character_colors, width, height)

    def plot_deltas(self, data, title=None):
        self.line_plotter.plot_line(data, title)
