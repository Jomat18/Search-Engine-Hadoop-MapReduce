from porterStemmer import PorterStemmer

porter=PorterStemmer()

def hashmap_pagerank():
	hmap_pr = {}

	f = open('part-00001', 'r')

	for line in f:
		row = line.split('\t')
		hmap_pr[row[0]] = row[1].rstrip('\n')

	return hmap_pr

def hashmap():
	words = {}

	f = open('part-00000', 'r')

	for line in f:
		row = line.split('\t')
		words[row[0]] = [w.split(':')[0] for w in row[1].split(',')]

	return words

inverted_index = hashmap()	
	
def search_query(value):

	words = []

	for word in value:
		words.append(word)
		word =	porter.stem(word, 0, len(word)-1)

	if len(value):		
		result = []
		i = 0
		for word in value:

			if word in inverted_index:
				result.append([inverted_index[word], words[i]])
				i += 1

		return result

	return []			
