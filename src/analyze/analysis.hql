CREATE DATABASE IF NOT EXISTS energy_db;
USE energy_db;

DROP TABLE IF EXISTS energy_transition;
CREATE EXTERNAL TABLE IF NOT EXISTS energy_transition (
    iso_code STRING,
    year INT,
    country STRING,
    co2 DOUBLE,
    population BIGINT,
    gdp DOUBLE,
    carbon_intensity DOUBLE
)
STORED AS PARQUET
LOCATION '/user/project/processed_data/energy_transition';

INSERT OVERWRITE DIRECTORY '/user/project/results/top10_efficiency'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT country, gdp, co2, carbon_intensity
FROM energy_transition
WHERE year = 2020 AND gdp > 100000000000
ORDER BY carbon_intensity ASC
LIMIT 10;

INSERT OVERWRITE DIRECTORY '/user/project/results/yearly_trend'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT year, AVG(carbon_intensity) as avg_intensity, SUM(co2) as total_co2
FROM energy_transition
WHERE year >= 1990
GROUP BY year
ORDER BY year ASC;

INSERT OVERWRITE DIRECTORY '/user/project/results/top10_per_capita'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT country, co2, population, (co2 / population) as co2_per_capita
FROM energy_transition
WHERE year = 2020 AND population > 1000000
ORDER BY co2_per_capita DESC
LIMIT 10;

INSERT OVERWRITE DIRECTORY '/user/project/results/major_economies'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT country, gdp, co2, carbon_intensity
FROM energy_transition
WHERE year = 2020 AND iso_code IN ('USA', 'CHN', 'IND', 'JPN', 'DEU')
ORDER BY gdp DESC;
