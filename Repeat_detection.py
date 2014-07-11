#modified Jun23 Found repeated comments!
#verified on local small set and is ready to upload with the whole folder after commenter extraction

#modified Jun30 count on full data set
#filter out spammers with features and repeated post more then threshold

import os
threshold = 0.1
Commenter = "../CommentUser/"
output = "../Repeated_Count.txt"
output2 = "../Spam_account.txt"

def repeat_detection():
    global threshold, Commenter, output
    for username in os.listdir(Commenter):
        file = os.path.join(Commenter,username)
        with open(file, 'r')as userfile:
            seen = set()
            repeat = 0
            for line in userfile:
                if line in seen:
                    repeat += 1
                else:
                    seen.add(line)

            if repeat >= 1:
            # print "user: " + username
            # print "repeat: " + str(repeat)
                f = open(output, 'a')
                f.write(username+" "+str(repeat)+'\n')

def is_spam(line):
    if str.isalnum(line):
        return True
    spam_kw = {'QQ', 'email', 'http','.com'}
    for kw in spam_kw:
        if str.find(line, kw) > 0:
            return True

def spammer_detection():
    #keep detecting repeat lines, but also track spammers in a file called output2
    #added Jun30 2014
    global threshold, Commenter, output
    for username in os.listdir(Commenter):
        file = os.path.join(Commenter,username)
        with open(file, 'r')as userfile:
            seen = set()
            repeat = 0
            spam = 0
            for line in userfile:
                if line in seen:
                    repeat += 1
                else:
                    seen.add(line)
                if is_spam(line):
                    spam += 1
            rate = float(repeat)/float(len(seen))
            if repeat >= 1:
                f = open(output, 'a')
                f.write(username+" "+str(repeat)+'\n')
            if rate > threshold or spam > 0:
                f1 = open(output2, 'a')
                f1.write(username + " "+ str(repeat)+'\n')

if __name__ == '__main__':
    spammer_detection()