import os

import matplotlib.pyplot as plt

LINE = "--------------------------------"


def print_summary(country_hours, size_hours, total):
    print(LINE)
    print("Duation by country:")
    print(LINE)
    for country, hours in country_hours.items():
        print(f"Total hours for {country}: {hours} \n")
    print(LINE)
    print("Duation sizes:")
    print(LINE)
    for size, hours in size_hours.items():
        print(f"Total hours for {size}: {hours} \n")
    print(LINE)
    print(f"Total hours for total: {total} \n {LINE}")


def plot_charts(dates, cumulative, country_hours, path):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(dates, cumulative)
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Cumulative EVA duration (hours)")
    ax1.set_title("Cumulative EVA duration")

    ax2.bar(country_hours.keys(), country_hours.values())
    ax2.set_xlabel("Country")
    ax2.set_ylabel("Cumulative EVA duration per country (hours)(Decending Order)")
    ax2.set_title("EVA duration by country")
    ax2.tick_params(axis="x", rotation=45)

    fig.tight_layout()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path)
    plt.show()


def print_comparison(results, winner):
    print(LINE)
    for country, count, total, average in results:
        average_text = "unavailable" if average is None else f"{average:.2f} hours"
        print(f"{country}: {count} EVAs, {total:.2f} hours total, average {average_text}")
    print(f"Greater total duration: {winner}" if winner else "Result: tie")
    print(LINE)