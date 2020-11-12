
from porterStemmer import PorterStemmer
from os import listdir
from re import findall
from stopwords import stopwords

porter=PorterStemmer()

#stopwords = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

files = listdir('corpus/')

for file in files: 

	f = open('corpus/'+file, 'r',encoding = "ISO-8859-1")

	lines = ""

	for line in f:

		if len(line.strip())!=0:

			line = " ".join(findall("[a-zA-Z]+", line))

			line = line.lower().split()

			words = [word for word in line if word not in stopwords]

			words=[ porter.stem(word, 0, len(word)-1) for word in words]

			if len(words):
				lines = lines + " ".join(words) + '\n'

	f.close()

	lines = lines[:-1]

	with open('corpus/'+file, 'w') as f:
		f.writelines(lines)

	f.close()	