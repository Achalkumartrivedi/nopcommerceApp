pytest -v -m "sanity" --html=./Reports/report.html testCases/ --browser firefox
rem pytest -v -m "regression" --html=./Reports/report.html testCases/ --browser firefox
rem pytest -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome
rem pytest -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser edge
