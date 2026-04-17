def load_with_spark(sales_data):
    sales_data.write.mode("overwrite").csv("data/final_sales_data_spark", header=True)