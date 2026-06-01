from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("GreenEnergyTransitionPipeline") \
    .enableHiveSupport() \
    .getOrCreate()

co2_df = spark.read.csv("/user/project/raw_data/co2/owid_co2.csv", header=True, inferSchema=True)
gdp_df = spark.read.csv("/user/project/raw_data/gdp/gdp.csv", header=True, inferSchema=True)

co2_clean = co2_df.select(
    col("iso_code"),
    col("country"),
    col("year"),
    col("co2"),
    col("population")
).filter(col("iso_code").isNotNull() & col("co2").isNotNull())

gdp_clean = gdp_df.select(
    col("Country Code").alias("iso_code"),
    col("Year").alias("year"),
    col("Value").alias("gdp")
).filter(col("iso_code").isNotNull() & col("gdp").isNotNull())

joined_df = co2_clean.join(gdp_clean, ["iso_code", "year"], "inner")

final_df = joined_df.withColumn("carbon_intensity", col("co2") / col("gdp"))

output_path = "/user/project/processed_data/energy_transition"
final_df.write.mode("overwrite").parquet(output_path)

spark.stop()
