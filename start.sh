#!/bin/bash

##############################
hdfs namenode -format

echo "Starting Daemons"
start-dfs.sh
start-yarn.sh

echo "Daemons running"
jps

echo "Cleanning files and removing stopwords"
python3 files.py

echo "Creating folder and upload files"
hdfs dfs -mkdir /input
hdfs dfs -put corpus/* /input

echo "Calculating inverted index"
hadoop jar /home/joma/hadoop/share/hadoop/tools/lib/hadoop-streaming*.jar \
        -file mapper.py \
        -mapper "python mapper.py" \
        -file reducer.py  \
        -reducer "python reducer.py" \
        -input /input/ \
        -output /output        


echo "Download results"
hdfs dfs -get /output/part-00000


stop-all.sh
#############################

echo "Starting the server"
python3 server.py


