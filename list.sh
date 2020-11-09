counter=0; 

for file in *; do 
	[[ -f $file ]] && mv -i "$file" $((counter+1)).txt && ((counter++)); 
done