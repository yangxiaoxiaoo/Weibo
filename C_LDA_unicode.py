#debug for the unicode problem
#no side effect for now
import logging, gensim, bz2
import os
from gensim import corpora, models, similarities

def C_LDA_output():
    logging.basicConfig(filename='../C_LDA_20_topics', filemode='a', format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)
    #load the corpus iterator mm
    #corpus_this = gensim.corpora.MmCorpus('../C_Weibo_corpus.mm')
    #tfidf = models.TfidfModel(corpus_this)

    lda = models.LdaModel.load('../C_Weibo_corpus_LDA.lda')
    lda.print_topics(100)

if __name__ == '__main__':
    C_LDA_output()

