#!/bin/bash
#mysql -u dbuser -pstopdb < 0-create-database.sql  
#mysql -u dbuser -pstopdb < 1-create-races.sql  
#mysql -u dbuser -pstopdb < 2-create-competitors.sql  
#mysql -u dbuser -pstopdb < 3-create-results.sql

cat ?-*.sql | mysql -uroot -p
