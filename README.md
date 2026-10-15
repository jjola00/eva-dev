# EVA Analysis

Analyses spacewalk (EVA) records from `eva-data.json`: totals hours by country and duration size, plots charts, and compares two countries over a period.

## Setup
```
pip install -r requirements.txt
```

## Run
```
python3 evacodev2.py
```
Prints totals, shows and saves a chart to `images/`, then asks whether to compare two countries.

## Module structure
- `loader.py`: reads `eva-data.json` and prepares clean records
- `analysis.py`: calculations only, including the country comparison
- `report.py`: console output and charts
- `evacodev2.py`: entry point, coordinates the modules and handles user input
- `test_analysis.py`: automated tests

Only `evacodev2.py` imports the other modules. See `docs/architecture.png`.

## Tests
```
python3 -m unittest -v
```

## Documentation
- `docs/in_arch_assessment.docx`: Activity 1 initial assessment
- `docs/ADR-001.md`: split into four modules
- `docs/activity4.md`: FR implementation notes
- `docs/activity5.md`: test evidence, evaluation and ADR-002