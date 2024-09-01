"""Megasena da virada.ipynb (https://colab.research.google.com/drive/1PuNpcwGjkfC-DjOyKfr3wTe7oJlyCimK)"""

"""##Imports"""

import pyspark
import os

from datetime import datetime
from itertools import combinations
from time import time_ns
from pyspark.sql import SparkSession

def print_and_log(*args, **kwargs):
    message = " ".join(map(str, args))
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file_name = kwargs.pop("log_file", "log.txt")
    log_file_path = os.path.join(script_dir, log_file_name)
    timestamp = datetime.now().strftime('[%d/%m/%Y %H:%M:%S] ')
    message_with_timestamp = timestamp + message

    print(message, **kwargs)

    with open(log_file_path, 'a') as f:
        f.write(message_with_timestamp + "\n")

"""## Programa 1"""

# Números possíveis
start_time = time_ns()
numbers = list(range(1, 26))
print_and_log(numbers)
print_and_log(f"{((time_ns()-start_time)/1_000_000_000):.2f}s")

start_time = time_ns()
s15 = tuple(combinations(numbers, 15))
print_and_log(len(s15))
print_and_log(f"{((time_ns()-start_time)/1_000_000_000):.2f}s")

start_time = time_ns()
s14 = tuple(combinations(numbers, 14))
print_and_log(len(s14))
print_and_log(f"{((time_ns()-start_time)/1_000_000_000):.2f}s")

start_time = time_ns()
s13 = tuple(combinations(numbers, 13))
print_and_log(len(s13))
print_and_log(f"{((time_ns()-start_time)/1_000_000_000):.2f}s")

start_time = time_ns()
s12 = tuple(combinations(numbers, 12))
print_and_log(len(s12))
print_and_log(f"{((time_ns()-start_time)/1_000_000_000):.2f}s")

start_time = time_ns()
s11 = tuple(combinations(numbers, 11))
print_and_log(len(s11))
print_and_log(f"{((time_ns()-start_time)/1_000_000_000):.2f}s")

"""## Função find_subset"""
conf = pyspark.SparkConf() \
    .setAppName("SB") \
    .set("spark.executor.memory", "6g") \
    .set("spark.driver.memory", "3g") \
    .set("spark.executor.cores", "8") \
    .set("spark.sql.shuffle.partitions", "100")

spark = SparkSession.builder \
    .config(conf=conf) \
    .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("OFF")

def find_subset(set_p1, p2):
  # Retorna um subconjunto de "set_p1" que contém todos os elementos de um conjunto com elementos de "p2" posições
  subset_p1 = sc.parallelize(set_p1)
  subset_p1 = subset_p1.repartition(100)
  subset_p1 = subset_p1.flatMap(lambda x: [(y, x) for y in combinations(x, p2)])
  subset_p1 = subset_p1.groupByKey()
  subset_p1 = subset_p1.map(lambda x: (x[0], sorted(x[1])[0]))
  #subset_p1 = subset_p1.map(lambda x: (x[0], len(x[1])))
  subset_p1 = subset_p1.values()
  subset_p1 = subset_p1.distinct()

  # subset_p1.persist()

  return subset_p1

"""##Programa 2"""

start_time = time_ns()
sb15_14 = find_subset(s15, 14)

for row in sb15_14.take(10):
  print_and_log(row)

print_and_log(sb15_14.count())
print_and_log(f"{((time_ns()-start_time)/1_000_000_000):.2f}s")

"""##Programa 3"""

start_time = time_ns()
sb15_13 = find_subset(s15, 13)

for row in sb15_13.take(10):
  print_and_log(row)

print_and_log(sb15_13.count())
print_and_log(f"{((time_ns()-start_time)/1_000_000_000):.2f}s")

"""##Programa 4"""

start_time = time_ns()
sb15_12 = find_subset(s15, 12)

for row in sb15_12.take(10):
  print_and_log(row)

print_and_log(sb15_12.count())
print_and_log(f"{((time_ns()-start_time)/1_000_000_000):.2f}s")

"""##Programa 5"""

start_time = time_ns()
sb15_11 = find_subset(s15, 11)

for row in sb15_11.take(10):
  print_and_log(row)

print_and_log(sb15_11.count())
print_and_log(f"{((time_ns()-start_time)/1_000_000_000):.2f}s")

"""##Análise de complexidade dos programas"""

spark.stop()
