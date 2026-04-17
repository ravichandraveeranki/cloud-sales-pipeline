def transform(customers, products, sales):
    sales_data = sales.merge(customers, on="customer_id", how="left")
    sales_data = sales_data.merge(products, on="product_id", how="left")
    sales_data["revenue"] = sales_data["quantity"] * sales_data["price"]

    return sales_data