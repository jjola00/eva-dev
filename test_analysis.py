import unittest
from datetime import datetime

from analysis import compare_countries, hours_by
from loader import EvaRecord, duration_size


def rec(year, hours, country):
    return EvaRecord(datetime(year, 6, 1), hours, country, duration_size(hours))


RECORDS = [rec(1990, 2.0, "USA"), rec(1995, 4.0, "USA"), rec(2000, 6.0, "USA"),
           rec(1990, 3.0, "Russia"), rec(2001, 5.0, "Russia")]


class TestAnalysis(unittest.TestCase):
    def test_hours_by_country(self):
        self.assertEqual(hours_by(RECORDS, "country"), {"USA": 12.0, "Russia": 8.0})

    def test_compare_includes_start_and_end_years(self):
        results, winner = compare_countries(RECORDS, "USA", "Russia", 1990, 2000)
        self.assertEqual(results, [("USA", 3, 12.0, 4.0), ("Russia", 1, 3.0, 3.0)])
        self.assertEqual(winner, "USA")

    def test_no_matches_gives_zero_and_unavailable(self):
        results, _ = compare_countries(RECORDS, "USA", "Russia", 1995, 1995)
        self.assertEqual(results[1], ("Russia", 0, 0, None))

    def test_equal_totals_is_tie(self):
        records = [rec(2010, 3.0, "USA"), rec(2010, 3.0, "Russia")]
        _, winner = compare_countries(records, "USA", "Russia", 2010, 2010)
        self.assertIsNone(winner)

    def test_start_after_end_raises(self):
        with self.assertRaises(ValueError):
            compare_countries(RECORDS, "USA", "Russia", 2000, 1990)

    def test_duration_size_boundaries(self):
        self.assertEqual(duration_size(4.0), "STANDARD")
        self.assertEqual(duration_size(7.0), "LONG")


if __name__ == "__main__":
    unittest.main()