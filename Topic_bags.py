#Jul10, after C_LDA_allin1,
#format each user as a vector, 1 means he has words in this topic's top 10 feature most words
#later: cluster the user's topic to form a topic network
import os
from gensim import corpora, models, similarities

infiles = "../CommentUserTokenized/"
outfile = "../CommentUserTopic.txt"
LDA_topic_num = 20


def format_vector():
    topic_list = list()
    lda = models.LdaModel.load('../C_Weibo_corpus_LDA.lda')
    for tuple_item in lda.show_topics(LDA_topic_num,topn = 10, formatted=False):
        this_topic = set()
        for words in tuple_item:
            print(words[1])
            this_topic.add(words[1])
        print tuple_item
        topic_list.append(this_topic)

    for user_name in os.listdir(infiles):
        user_topic = [0]*LDA_topic_num
        file_dir = os.path.join(infiles, user_name)
        user_file = open(file_dir, 'r')
        for line in user_file:
            for word in line.split(' '):
                for topic_index in range(0,len(topic_list)):
                    if word in topic_list[topic_index]:
                        user_topic[topic_index] = 1
        pfout = open(outfile, 'a')
        pfout.write(str(user_topic) + ' '+ user_name.split('_')[0]+'\n')


if __name__ == "__main__":
    format_vector()
