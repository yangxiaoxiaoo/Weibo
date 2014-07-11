import hashlib
import os
Commenter = "../CommentUser/"
output = "../Repeated_Count_interuser.txt"
output_threshold = 0.01

user_set_map = {}
users = set()


def jaccard(uid_1, uid_2):
    uid_union = uid_1.union(uid_2)
    uid_intersect = uid_1.intersection(uid_2)
    jaccard_index = float(len(uid_intersect)) / float(len(uid_union))
    return jaccard_index

def map_init():
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
            user_set_map[username] = hashed_comment

def comp_hash():
    global user_set_map,users
    probe_1layer = 0
    for user1 in users:
        probe_1layer +=1
        if probe_1layer % 100 == 0:
            print "reach 1st layer loop user----"
            print probe_1layer
        for user2 in users:
            index = jaccard(user_set_map[user1],user_set_map[user2])
            print(index)
            f = open(output, 'a')
            if index > output_threshold:
                f.write(user1 +' '+  user2 + " "+ str(index)+'\n')

if __name__ == "__main__":
    map = map_init()
    comp_hash()