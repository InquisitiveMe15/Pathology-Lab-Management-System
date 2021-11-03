USE pathology;

LOAD DATA LOCAL INFILE 'metro-price-list-ALL.csv' 
INTO TABLE test 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 4 ROWS
(testId,testName,price);
