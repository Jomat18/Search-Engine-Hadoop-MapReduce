#!/bin/bash

counter=1; 

for file in *; do 
	[[ -f $file ]] && mv -i "$file" $((counter))_"$file" && ((counter++)); 
done