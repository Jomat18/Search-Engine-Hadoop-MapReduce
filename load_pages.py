

def hashmap():
	words = {}

	f = open('part-00000', 'r')

	for line in f:
		row = line.split('\t')
		words[row[0]] = [w.split(':')[0] for w in row[1].split(',')]

	return words
	
def search_query(value, words):

	if value:		
		query = value.split()

		print (query)
		for word in query:

			if word in words:
				return words[word]
			else: 
				return []

	return []			
