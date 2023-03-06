.mode csv
.output results3.csv
.open db.sqlite3
SELECT song,score
FROM playerscores
WHERE level = '14+'
;