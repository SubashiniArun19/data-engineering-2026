import dlt
from pyspark.sql.functions import *
data = [
(101,"Arjun Reddy","Hyderabad","Cardiology",5000,1),
(102,"Sneha Kapoor","Delhi","Orthopedics",3000,2),
(103,"Rahul Sharma","Mumbai","Dermatology",1500,1),
(104,"Priya Nair","Bangalore","Cardiology",5000,2),
(105,"Vikram Singh","Chennai","Neurology",7000,1),
(106,"Ananya Das","Kolkata","Orthopedics",3000,3),
(107,"Karan Patel","Ahmedabad","Cardiology",5000,1),
(108,"Meera Iyer","Bangalore","Dermatology",1500,2)
]
columns = ["visit_id","patient_name","city","department","consultation_fee","tests_count"]
@dlt.table(name="bronze_patients")
def bronze():
    return spark.createDataFrame(data, columns)
@dlt.table(name="silver_patients")
def silver():
    df = dlt.read("bronze_patients")
    return df.withColumn("total_bill",col("consultation_fee") + col("tests_count") * 500).withColumn("category",when(col("total_bill") >= 6000, "High").when(col("total_bill") >= 3000, "Medium").otherwise("Low"))
@dlt.table(name="gold_department_revenue")
def gold():
    df = dlt.read("silver_patients")
    return df.groupBy("department").agg(count("*").alias("total_patients"),sum("total_bill").alias("total_revenue"))