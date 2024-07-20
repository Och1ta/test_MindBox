from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

# Инициализация SparkSession
spark = SparkSession.builder.appName("ProductCategory").getOrCreate()

# Пример данных для датафреймов
products_data = [(1, "Product1"), (2, "Product2"), (3, "Product3")]
categories_data = [(1, "Category1"), (2, "Category2")]
product_category_data = [(1, 1), (1, 2), (2, 1)]

# Создание датафреймов
products = spark.createDataFrame(products_data, ["product_id", "product_name"])
categories = spark.createDataFrame(categories_data, ["category_id", "category_name"])
product_category = spark.createDataFrame(product_category_data, ["product_id", "category_id"])

# Джойн продуктов и категорий через таблицу связей
product_category_joined = product_category.join(categories, "category_id", "inner") \
    .join(products, "product_id", "inner") \
    .select("product_name", "category_name")

# Нахождение продуктов, у которых нет категорий
products_with_categories = product_category.select("product_id").distinct()
products_without_categories = products.join(products_with_categories, "product_id", "leftanti") \
    .select("product_name", lit(None).alias("category_name"))

# Объединение двух датафреймов
result = product_category_joined.union(products_without_categories)

# Показ результата
result.show()
