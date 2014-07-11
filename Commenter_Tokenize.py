#May12 Tokenize Commenters bigger then 1k
#Jun23 Tokenize all renewed Commenters
#keep previous segmentation on celebrity users for future usage
import os
from smallseg import SEG
seg = SEG()

all_user_folder = "../CommentUser/"
for user_name in os.listdir(all_user_folder):
    user_file = os.path.join(all_user_folder, user_name)
    user_all_text = user_name + '_text'
    user_tokenized_text = user_name + '_tokenized'
    with open(user_file,'r') as user_text_corpus:
        for line in user_text_corpus:
            #  print line
            #every line of tweets has a list of words wlist
            wlist = seg.cut(line)
            wlist.reverse()
            #  print wlist
            tmp = " ".join(wlist)
            fout = open(os.path.join("../CommentUserTokenized", user_tokenized_text),'a')
            fout.write(tmp.encode('utf-8'))