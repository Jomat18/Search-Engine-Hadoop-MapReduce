#!/bin/bash

##############################
#hdfs namenode -format

echo "******************** Starting Daemons ********************"
#start-dfs.sh
#start-yarn.sh

echo "******************** Daemons running ********************"
#jps

echo "******************** Creating data for pagerank ********************"
python3 data_pagerank.py

echo "******************** Creating folder and upload files ********************"
hdfs dfs -mkdir /input
hdfs dfs -put static/corpus/* /input

echo "******************** Calculating inverted index ********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file mapper.py \
        -mapper "python mapper.py" \
        -file reducer.py  \
        -reducer "python reducer.py" \
        -input /input/ \
        -output /output


echo "******************** Download results ********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
               -Dmapred.reduce.tasks=1 \
               -input /output/ \
               -output /result \
               -mapper cat \
               -reducer cat

hdfs dfs -get /result/part-00000

echo "******************** Creating folder and upload files for pagerank ********************"
hdfs dfs -mkdir /input2
hdfs dfs -put pagerank.txt /input2

echo "******************** Calculating pagerank ********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file pagerank_mapper.py \
        -mapper "python pagerank_mapper.py" \
        -file pagerank_reducer.py  \
        -reducer "python pagerank_reducer.py" \
        -input /input2/ \
        -output /output2


echo "******************** Download results ********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
               -Dmapred.reduce.tasks=1 \
               -input /output2/ \
               -output /result2 \
               -mapper cat \
               -reducer cat


echo "******************** Calculating pagerank 2********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file pagerank_reducer.py  \
        -reducer "python pagerank_reducer.py" \
        -input /result2/part-00000 \
        -output /output3


echo "******************** Download results ********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
               -Dmapred.reduce.tasks=1 \
               -input /output3/ \
               -output /result3 \
               -mapper cat \
               -reducer cat



echo "******************** Calculating pagerank ********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file rank_map.py \
        -mapper "python rank_map.py" \
        -input /result3/part-00000 \
        -output /output4


hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
               -Dmapred.reduce.tasks=1 \
               -input /output4/ \
               -output /result4 \
               -mapper cat \
               -reducer cat

hadoop fs -mv /result4/part-00000 /result4/part-00001
hdfs dfs -get /result4/part-00001

#stop-all.sh
#############################

echo "******************** Starting the server ********************"
python3 server.py


