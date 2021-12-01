# Databricks notebook source
a = 1

# COMMAND ----------

a

# COMMAND ----------

spark

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, IntegerType

df = spark.createDataFrame(
    [
        ('Alice', ['math101', 'ee101', 'cs201'], 'Apple, Orange, Pineapple', ['red', 'blue'], 19, 'F', 'CS'), 
        ('Bob', ['ee101', 'math102'], 'Peach, Banana', ['green', 'red'], 22, 'M', 'EE'), 
        ('Jason', ['math101'], 'Stawberry, Blueberry', ['purple'], 20, 'M', 'MATH')
    ], 
    schema=StructType([
        StructField('name', StringType(), False),
        StructField('classes', ArrayType(StringType()), True),
        StructField('fruits', StringType()),
        StructField('favorite_colors', ArrayType(StringType(), False)),
        StructField('age', IntegerType()),
        StructField('gender', StringType()),
        StructField('major', StringType())
    ])
)
df.createOrReplaceTempView('_df')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   name,
# MAGIC   age
# MAGIC FROM _df

# COMMAND ----------

df.count()

# COMMAND ----------
df4 = df
df4.count()

# COMMAND ----------

df.saveAsTable('test')


# COMMAND ----------


