result.csv
.mode csv
.output results.csv
.open db.sqlite3
SELECT *
FROM IntlSheets
WHERE difficulty = 'master'
;
