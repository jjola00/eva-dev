# Activity 4: Country Comparison

## Architectural changes

No structural change was needed. The FR fitted into the existing modules.

- analysis.py: added compare_countries, which reuses total_hours instead of duplicating the calculation.
- report.py: added print_comparison. plot_charts now creates the images folder if it is missing.
- evacodev2.py: added input collection and validation, because coordinating the user flow is its job.
- loader.py: unchanged. The FR didn't need to modify an unrelated module.
- 3 of 4 modules changed.
- Unknown countries are rejected and re-asked rather than reported as zero; "0 / unavailable" applies to a valid country with no EVAs in the range.
- Records without a date (44) can't fall in any year range, so they are excluded from comparisons.

## Manual test evidence

### Terminal output

Run 1 (checks 1, 2, 3):

```
--------------------------------
Duation by country:
--------------------------------
Total hours for USA: 1257.1333333333334 

Total hours for Russia: 527.9000000000001 

--------------------------------
Duation sizes:
--------------------------------
Total hours for STANDARD: 1105.566666666667 

Total hours for LONG: 537.9666666666666 

Total hours for SHORT: 141.49999999999997 

--------------------------------
Total hours for total: 1785.0333333333333 
 --------------------------------
Compare two countries? (y/n): y
Countries: Russia, USA
Country A: y
Unknown country, try again.
Country A: USA
Country B: Russia
Start year: 1990
End year: 2000
--------------------------------
USA: 36 EVAs, 233.13 hours total, average 6.48 hours
Russia: 58 EVAs, 272.45 hours total, average 4.70 hours
Greater total duration: Russia
--------------------------------
```

Run 2 (checks 4, 5):

```
Compare two countries? (y/n): y
Countries: Russia, USA
Country A: USA
Country B: Russia
Start year: 2000
End year: 1990
Years must be numbers and start must not be after end, try again.
Country A: y
Unknown country, try again.
Country A: USA
Country B: Russia
Start year: 1966
End year: 1966
--------------------------------
USA: 8 EVAs, 12.00 hours total, average 1.50 hours
Russia: 0 EVAs, 0.00 hours total, average unavailable
Greater total duration: USA
--------------------------------
```
