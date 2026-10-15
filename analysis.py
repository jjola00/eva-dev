import math
from collections import Counter


def total_hours(records):
    return sum(r.hours for r in records)


def cumulative_hours(records):
    totals, running = [], 0
    for r in records:
        running += r.hours
        totals.append(running)
    return [r.date for r in records], totals


def hours_by(records, field):
    counts = Counter()
    for r in records:
        counts[getattr(r, field)] += r.hours
    return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))


def compare_countries(records, country_a, country_b, start_year, end_year):
    if start_year > end_year:
        raise ValueError("start year is after end year")
    results = []
    for country in (country_a, country_b):
        matches = [r for r in records
                   if r.country == country and start_year <= r.date.year <= end_year]
        count, total = len(matches), total_hours(matches)
        results.append((country, count, total, total / count if count else None))
    total_a, total_b = results[0][2], results[1][2]
    if math.isclose(total_a, total_b):
        winner = None
    else:
        winner = country_a if total_a > total_b else country_b
    return results, winner