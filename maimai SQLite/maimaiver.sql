.mode csv
.output results2.csv
.open db.sqlite3
SELECT songId
FROM Songs
WHERE version = 'maimai'
;