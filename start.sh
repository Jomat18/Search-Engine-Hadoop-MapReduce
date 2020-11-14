#!/bin/bash

##############################
#hdfs namenode -format

echo "******************** Starting Daemons ********************"
start-dfs.sh
start-yarn.sh

echo "******************** Daemons running ********************"
jps

echo "******************** Creating data for pagerank ********************"
python3 data_pagerank.py

echo "******************** Creating folder and upload files ********************"
hdfs dfs -mkdir /input
hdfs dfs -put static/corpus/* /input

echo "******************** Calculating inverted index ********************"
hadoop jar /home/joma/hadoop/share/hadoop/tools/lib/hadoop-streaming*.jar \
        -file mapper.py \
        -mapper "python mapper.py" \
        -file reducer.py  \
        -reducer "python reducer.py" \
        -input /input/ \
        -output /output        


echo "******************** Download results ********************"
hdfs dfs -get /output/part-00000

echo "******************** Creating folder and upload files for pagerank ********************"
hdfs dfs -mkdir /input2
hdfs dfs -put pagerank.txt /input2

echo "******************** Calculating pagerank ********************"
hadoop jar /home/joma/hadoop/share/hadoop/tools/lib/hadoop-streaming*.jar \
        -file pagerank_mapper.py \
        -mapper "python pagerank_mapper.py" \
        -file pagerank_reducer.py  \
        -reducer "python pagerank_reducer.py" \
        -input /input2/ \
        -output /output2        


echo "******************** Download results ********************"
hadoop fs -mv /output2/part-00000 /output2/part-00001
hdfs dfs -get /output2/part-00001


stop-all.sh
#############################

echo "******************** Starting the server ********************"
python3 server.py


