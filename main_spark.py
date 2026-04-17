from scripts.transform_pyspark import transform_with_spark
from scripts.load_pyspark import load_with_spark

sales_data = transform_with_spark()
load_with_spark(sales_data)

print("PySpark ETL pipeline completed successfully.")
sales_data.show()