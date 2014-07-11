import gensim
import os
#Jul 7 old lda new commenter

Commenter = "../CommentUser/"
lda = gensim.models.LdaModel.load('../C_Weibo_corpus_LDA.lda')

lda = gensim.models.LdaModel(chunksize=1)
documents_folder = "../CommentUserTokenized/"
id2word = gensim.corpora.Dictionary.load("../C_temp_corpus_dict")
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
    lda.inference(doc_vector, False)