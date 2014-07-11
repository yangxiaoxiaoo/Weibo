#preprocessing for comments
#Big Users(more then 1k ~3 comments)only

import logging, gensim, bz2
import os
from gensim import corpora, models, similarities

def C_LDA_pre(nobelow, noabove):
    #load dictionary
    id2word = gensim.corpora.Dictionary.load("../C_temp_corpus_dict")
    id2word.filter_extremes(no_below=nobelow, no_above=noabove)
    #Now the same word have a different word id, so the new dictionary is saved
    id2word.save('../C_temp_corpus_dict')
    print(id2word)

    documents_folder = "../CommentUserTokenized/"
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
       # print doc_vector

    corpus = [id2word.doc2bow(doc_text) for doc_text in cop_wlist]
    corpora.MmCorpus.serialize('../C_Weibo_corpus.mm',corpus)
    print "------------------------------corpus--------------------------------------"
    print(corpus)

if __name__ == '__main__':
    C_LDA_pre(10,0.05)

