#Jul5:try shrinking data size by filtering out less then 2 comments
import hashlib
import os

Commenter = "../CommentUser/"
output = "../BigCommenterHashed/"
#output_threshold = 0.01
user_set_map = {}
users = set()

def map_filter_init():
    global user_set_map,users
    for username in os.listdir(Commenter):
        users.add(username)
        file = os.path.join(Commenter, username)
        with open(file,'r')as userfile:
            hashed_comment = set()
            repeat = 0
            for line in userfile:
                hash_ogj = hashlib.md5(line)
                hashed_comment.add(hash_ogj.hexdigest())
            #filter out less then 2 comment cases
            if len(hashed_comment) > 2:
                user_set_map[username] = hashed_comment
                output_file  = os.path.join(output,username)
                output_fp = open(output_file, 'w')
                for elem in hashed_comment:
                    output_fp.write(str(elem) + '\n')

if __name__ == "__main__":
    map_filter_init()