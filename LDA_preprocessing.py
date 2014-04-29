import logging, gensim, bz2
import os
from gensim import corpora, models, similarities

#load dictionary
id2word = gensim.corpora.Dictionary.load("../temp_corpus_dict")

documents_folder = "../UserTokenized/"
#corpus
cop_wlist = []
for user_doc in os.listdir(documents_folder):
    #documents
    doc_wlist = []
    user_name = user_doc.split('_')[0]
    file_dir = os.path.join(documents_folder, user_doc)
    user_file = open(file_dir, 'r')
    for line in user_file:
        for word in line.split(' '):
            doc_wlist.append(word)
    cop_wlist.append(doc_wlist)
    doc_vector = id2word.doc2bow(doc_wlist)
    print doc_vector

corpus = [id2word.doc2bow(doc_text) for doc_text in cop_wlist]
corpora.MmCorpus.serialize('../Weibo_corpus.mm',corpus)
print "------------------------------corpus--------------------------------------"
print(corpus)
