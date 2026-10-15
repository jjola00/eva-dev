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