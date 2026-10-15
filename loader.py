import json
from collections import namedtuple
from datetime import datetime

EvaRecord = namedtuple("EvaRecord", "date hours country size")


def read_eva_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def duration_size(hours):
    return "SHORT" if hours < 4 else "STANDARD" if hours < 7 else "LONG"


def prepare_records(raw):
    records = []
    for eva in raw:
        if not eva.get("date") or not eva.get("duration"):
            continue
        hours, minutes = map(int, eva["duration"].split(":"))
        duration_hours = hours + minutes / 60
        records.append(EvaRecord(datetime.fromisoformat(eva["date"]), duration_hours,
                                 eva.get("country"), duration_size(duration_hours)))
    records.sort(key=lambda record: record.date)
    return records