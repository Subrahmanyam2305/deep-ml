import numpy as np
from collections import Counter
import math

def compute_tf_idf(corpus, query):
	"""
	Compute TF-IDF scores for a query against a corpus of documents.
    
	:param corpus: List of documents, where each document is a list of words
	:param query: List of words in the query
	:return: List of lists containing TF-IDF scores for the query words in each document
	"""
	tfidf_scores, result, idf_counter = [], [], Counter()
	for document in corpus:
		unique_terms_in_doc = set(document)
		for term in unique_terms_in_doc:
			idf_counter[term] += 1

	idf_val_dict = {}
	for term in idf_counter:
		idf_val_dict[term] = math.log((len(corpus)+1) / (idf_counter[term] + 1)) + 1
	
	for document in corpus:
		tfidf_list = []
		doc_len = len(document)
		for term in query:
			tf_val = document.count(term) / doc_len if doc_len > 0 else 0
			idf_val = idf_val_dict.get(term, 0)
			tfidf_list.append(round(tf_val*idf_val, 5))
		result.append(tfidf_list)

	return result

			
