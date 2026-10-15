# Activity 5: Verify and Evaluate

## Test evidence

6 automated tests in test_analysis.py.
Covers the new comparison, one existing operation (hours_by), and invalid or boundary input (start after end, no matches, tie, 4h and 7h size limits).

```
$ python3 -m unittest -v
test_compare_includes_start_and_end_years (test_analysis.TestAnalysis.test_compare_includes_start_and_end_years) ... ok
test_duration_size_boundaries (test_analysis.TestAnalysis.test_duration_size_boundaries) ... ok
test_equal_totals_is_tie (test_analysis.TestAnalysis.test_equal_totals_is_tie) ... ok
test_hours_by_country (test_analysis.TestAnalysis.test_hours_by_country) ... ok
test_no_matches_gives_zero_and_unavailable (test_analysis.TestAnalysis.test_no_matches_gives_zero_and_unavailable) ... ok
test_start_after_end_raises (test_analysis.TestAnalysis.test_start_after_end_raises) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

## Existing functionality

Ran Eddie's original script (commit 97dfa5a) and the restructured version on the same data, then compared the console output.

$ diff before.txt after.txt
> Compare two countries? (y/n):

All existing output is identical. The only difference is the new FR prompt at the end. The chart is still generated.

## Before vs after

- Before: 1 file, top-level script, no functions, shared globals, untestable without running everything.
- After: 4 modules (loader, analysis, report, evacodev2), calculations as functions that take records and return results, 6 automated tests.

## Maintainability evaluation

- Modules modified for the FR: 3 of 4 (analysis, report, evacodev2). loader was untouched.
- Dependencies: only evacodev2 imports the other modules. analysis and report don't depend on each other or on loader.
- Testing without files or display: yes. The tests build records in memory and never read JSON or print.
- Responsibilities: easier to identify, with one module per job instead of one 80-line script.
- Duplication: reduced. The comparison reuses total_hours, and one hours_by replaces two separate counting loops.
- Unnecessary complexity: minimal. 3 new files, no classes, no frameworks, no new dependencies.

## ADR-002: Test analysis with unittest and in-memory records

- Context: AR6 requires the analysis to be tested independently, using known inputs.
- Alternatives: pytest; running the whole script and checking its output; a test JSON file; unittest with in-memory records.
- Decision: unittest with in-memory EvaRecords.
- Rationale: it's in the standard library (no new dependency), it isolates the calculations from files and display, and the inputs and results are known.
- Consequences: tests are fast and focused. Trade-off: file reading and plotting aren't covered by automated tests, so the before and after comparison covers them. unittest is also more verbose than pytest.