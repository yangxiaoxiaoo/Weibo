import logging, gensim, bz2
import os
from gensim import corpora, models, similarities

#load dictionary
dictionary = gensim.corpora.Dictionary.load("../temp_corpus_dict_10_05")
#load the corpus iterator mm
corpus_this = gensim.corpora.MmCorpus('../Weibo_corpus.mm')
#print (corpus_this)
#LDA model transformation
lda = models.LdaModel(corpus= corpus_this,num_topics = 100,id2word=dictionary,update_every=1)
lda.print_topics(100)
lda.save('../Weibo_corpus_LDA.lda')