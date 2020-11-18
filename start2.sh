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

hadoop fs -mv /result/part-00000 /result12/part-00004
hdfs dfs -get /result/part-00004

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



echo "******************** Calculating pagerank 3********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file pagerank_reducer.py  \
        -reducer "python pagerank_reducer.py" \
        -input /result3/part-00000 \
        -output /output4


echo "******************** Download results ********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
               -Dmapred.reduce.tasks=1 \
               -input /output4/ \
               -output /result4 \
               -mapper cat \
               -reducer cat


echo "******************** Calculating pagerank 4********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file pagerank_reducer.py  \
        -reducer "python pagerank_reducer.py" \
        -input /result4/part-00000 \
        -output /output5


echo "******************** Download results ********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
               -Dmapred.reduce.tasks=1 \
               -input /output5/ \
               -output /result5 \
               -mapper cat \
               -reducer cat



echo "******************** Calculating pagerank 5********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file pagerank_reducer.py  \
        -reducer "python pagerank_reducer.py" \
        -input /result5/part-00000 \
        -output /output6


echo "******************** Download results ********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
               -Dmapred.reduce.tasks=1 \
               -input /output6/ \
               -output /result6 \
               -mapper cat \
               -reducer cat



echo "******************** Calculating pagerank 6********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file pagerank_reducer.py  \
        -reducer "python pagerank_reducer.py" \
        -input /result6/part-00000 \
        -output /output7


echo "******************** Download results ********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
               -Dmapred.reduce.tasks=1 \
               -input /output7/ \
               -output /result7 \
               -mapper cat \
               -reducer cat



echo "******************** Calculating pagerank 7********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file pagerank_reducer.py  \
        -reducer "python pagerank_reducer.py" \
        -input /result7/part-00000 \
        -output /output8


echo "******************** Download results ********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
               -Dmapred.reduce.tasks=1 \
               -input /output8/ \
               -output /result8 \
               -mapper cat \
               -reducer cat



echo "******************** Calculating pagerank 8********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file pagerank_reducer.py  \
        -reducer "python pagerank_reducer.py" \
        -input /result8/part-00000 \
        -output /output9


echo "******************** Download results ********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
               -Dmapred.reduce.tasks=1 \
               -input /output9/ \
               -output /result9 \
               -mapper cat \
               -reducer cat




echo "******************** Calculating pagerank 9********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file pagerank_reducer.py  \
        -reducer "python pagerank_reducer.py" \
        -input /result9/part-00000 \
        -output /output10


echo "******************** Download results ********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
               -Dmapred.reduce.tasks=1 \
               -input /output10/ \
               -output /result10 \
               -mapper cat \
               -reducer cat


echo "******************** Calculating pagerank 10********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file pagerank_reducer.py  \
        -reducer "python pagerank_reducer.py" \
        -input /result10/part-00000 \
        -output /output11


echo "******************** Download results ********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
               -Dmapred.reduce.tasks=1 \
               -input /output11/ \
               -output /result11 \
               -mapper cat \
               -reducer cat



echo "******************** Calculating pagerank ********************"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file rank_map.py \
        -mapper "python rank_map.py" \
        -input /result11/part-00000 \
        -output /output12


hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
               -Dmapred.reduce.tasks=1 \
               -input /output12/ \
               -output /result12 \
               -mapper cat \
               -reducer cat

hadoop fs -mv /result12/part-00000 /result12/part-00005
hdfs dfs -get /result12/part-00005

#stop-all.sh
#############################

echo "******************** Starting the server ********************"
python3 server.py


