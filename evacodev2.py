from analysis import compare_countries, cumulative_hours, hours_by, total_hours
from loader import prepare_records, read_eva_file
from report import plot_charts, print_comparison, print_summary

DATA_PATH = "eva-data.json"
CHART_PATH = "images/cumulative_duration_combined.png"


def run_comparison(records):
    countries = {r.country.lower(): r.country for r in records if r.country}
    print("Countries:", ", ".join(sorted(countries.values())))
    while True:
        try:
            country_a = countries[input("Country A: ").strip().lower()]
            country_b = countries[input("Country B: ").strip().lower()]
            start = int(input("Start year: "))
            end = int(input("End year: "))
            print_comparison(*compare_countries(records, country_a, country_b, start, end))
            return
        except KeyError:
            print("Unknown country, try again.")
        except ValueError:
            print("Years must be numbers and start must not be after end, try again.")


def main():
    records = prepare_records(read_eva_file(DATA_PATH))
    country_hours = hours_by(records, "country")
    size_hours = hours_by(records, "size")
    print_summary(country_hours, size_hours, total_hours(records))
    dates, cumulative = cumulative_hours(records)
    plot_charts(dates, cumulative, country_hours, CHART_PATH)
    try:
        if input("Compare two countries? (y/n): ").strip().lower() == "y":
            run_comparison(records)
    except (EOFError, KeyboardInterrupt):
        print("\nComparison cancelled.")


if __name__ == "__main__":
    main()