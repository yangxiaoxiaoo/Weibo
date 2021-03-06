import os
from gensim import corpora, models, similarities

documents_folder = "../UserTokenized_2/"
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
dictionary = corpora.Dictionary(cop_wlist)
dictionary.save('../temp_corpus_dict')
print(dictionary)
