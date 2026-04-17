from pyspark.sql import SparkSession


def transform_with_spark():
    spark = SparkSession.builder.appName("CloudSalesPipeline").getOrCreate()

    customers = spark.read.csv("data/customers.csv", header=True, inferSchema=True)
    products = spark.read.csv("data/products.csv", header=True, inferSchema=True)
    sales = spark.read.csv("data/sales.csv", header=True, inferSchema=True)

    sales_data = sales.join(customers, on="customer_id", how="left")
    sales_data = sales_data.join(products, on="product_id", how="left")
    sales_data = sales_data.withColumn("revenue", sales_data["quantity"] * sales_data["price"])

    return sales_data