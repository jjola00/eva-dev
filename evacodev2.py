from analysis import cumulative_hours, hours_by, total_hours
from loader import prepare_records, read_eva_file
from report import plot_charts, print_summary

DATA_PATH = "eva-data.json"
CHART_PATH = "images/cumulative_duration_combined.png"


def main():
    records = prepare_records(read_eva_file(DATA_PATH))
    country_hours = hours_by(records, "country")
    size_hours = hours_by(records, "size")
    print_summary(country_hours, size_hours, total_hours(records))
    dates, cumulative = cumulative_hours(records)
    plot_charts(dates, cumulative, country_hours, CHART_PATH)


if __name__ == "__main__":
    main()