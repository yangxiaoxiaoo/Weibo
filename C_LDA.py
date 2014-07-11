#Commenter LDA
#including logging, and since we don't need bag of words analysis, all printed information in logging file
#end of LDA in commenters

import logging, gensim, bz2
import os
from gensim import corpora, models, similarities

def C_LDA(topic_num):
    logging.basicConfig(filename='../C_LDA_topics', filemode='a', format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)
    #load dictionary
    dictionary = gensim.corpora.Dictionary.load("../C_temp_corpus_dict")
    #load the corpus iterator mm
    corpus_this = gensim.corpora.MmCorpus('../C_Weibo_corpus.mm')
    tfidf = models.TfidfModel(corpus_this)
    #print (corpus_this)
    #LDA model transformation
    lda = models.LdaModel(corpus= corpus_this,num_topics = topic_num,id2word=dictionary,update_every=1)
    lda.print_topics(topic_num)
    lda.save('../C_Weibo_corpus_LDA.lda')

if __name__ == '__main__':
    C_LDA(100)