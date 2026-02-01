import matplotlib.pyplot as plt


def plot_time_series(df, x, y, title, ylabel, label=None):
    """
    Generic line plot for time series data.
    """
    plt.figure(figsize=(8, 5))
    plt.plot(df[x], df[y], marker="o", label=label)
    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel(ylabel)
    if label:
        plt.legend()
    plt.grid(True)
    plt.show()


def plot_growth_bar(df, x, y, title):
    """
    Bar chart for growth rates.
    """
    plt.figure(figsize=(8, 5))
    plt.bar(df[x], df[y])
    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel("Percentage Point Change")
    plt.grid(True, axis="y")
    plt.show()


def plot_multiple_indicators(df, indicator_col, year_col, value_col, title, ylabel):
    """
    Plot multiple indicators on the same chart.
    """
    plt.figure(figsize=(8, 5))

    for indicator in df[indicator_col].unique():
        subset = df[df[indicator_col] == indicator]
        plt.plot(
            subset[year_col],
            subset[value_col],
            marker="o",
            label=indicator
        )

    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()
