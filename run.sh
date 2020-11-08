#!/bin/bash

javac -classpath $(hadoop classpath) -d . WordCount.java
jar cf wc.jar WordCount*.class

# Ejecutar el jar en hadoop
hadoop jar wc.jar WordCount /user/joma/input /user/joma/output

echo $WORDS