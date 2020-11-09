#!/usr/bin/python

import re
import sys
from operator import add

from pyspark.sql import SparkSession


def computeContribs(urls, rank):
    # Calcular la contribucion del URL con el rank de otros URLs
    num_urls = len(urls)
    for url in urls:
        yield (url, rank / num_urls)


def parseNeighbors(urls):
    # Parsear los urls
    parts = re.split(r'\s+', urls)
    return parts[0], parts[1]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(-1)

    # Inicializa el spark context.
    spark = SparkSession\
        .builder\
        .appName("PageRank")\
        .getOrCreate()

    # Carga el archivo de entrada
    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])

    # Carga todas las URL del archivo de entrada e inicializa sus vecinos.
    links = lines.map(lambda urls: parseNeighbors(urls)).distinct().groupByKey().cache()

    # Carga todas las URL con otras URL enlazadas desde el archivo de entrada e inicializa las filas de ellas en una.
    ranks = links.map(lambda url_neighbors: (url_neighbors[0], 1.0))

    # Calcula y actualiza los rank de URL continuamente usando el algoritmo PageRank.  
    for iteration in range(int(sys.argv[2])):
        # Calcula las contribuciones de URL al rank de otras URL.
        contribs = links.join(ranks).flatMap(
            lambda url_urls_rank: computeContribs(url_urls_rank[1][0], url_urls_rank[1][1]))

        ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank * 0.85 + 0.15)

    # Imprima todos los rank de URL en la consola.
    for (link, rank) in ranks.collect():
        print("%s tiene un rank de: %s." % (link, rank))

    spark.stop()
    

"""
Permanecer en la página: 0.05
Siga aleatoriamente un enlace: 0.85
Ir aleatoriamente a cualquier página del gráfo: 0.10    
"""