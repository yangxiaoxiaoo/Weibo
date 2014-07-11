# -*- coding: utf-8 -*-
#! /usr/bin/env python

#Previous experiments are done on celebrity users;
#Now generalize it to all commentors and save the result in folder Commentors_Tokenized
from gensim import corpora, models, similarities
import os
import sys
import fnmatch
import pdb
import pickle
import codecs
import time
import unicodedata
all_user_folder = "../timelines/"

def Extract_Comment_to_folder():
    for user_name in os.listdir(all_user_folder):
        user_folder = os.path.join(all_user_folder, user_name)
        if os.path.isdir(user_folder):
            user_all_text = user_name + '_text'
            try:
                os.remove(os.path.join(user_folder, user_all_text))
            except OSError:
                pass
            with open(os.path.join(user_folder, user_all_text),'a') as result:
                for crawling_date in os.listdir(user_folder):

                    date_folder = os.path.join(user_folder,crawling_date)
                    if os.path.isdir(date_folder):
                        #print 'reach date folder'
                        for text_file_names in os.listdir(date_folder):
                            #print 'find text file'
                            with open(os.path.join(date_folder,text_file_names), 'r')as data:
                                while True:
                                    try: mydict = pickle.load(data)
                                    except UnicodeDecodeError:
                                        print "Unicode!"
                                      #  time.sleep(1)
                                        continue
                                    except EOFError:
                                     #   print "EOFE"
                                     #   time.sleep(1)
                                        break
                                    except IndexError:
                                        print "index"
                                     #   time.sleep(1)
                                        break
                                   # print mydict

                                    #############Comments:
                                    index = 0
                                    while True:
                                        try:
                                            if mydict.get(index) != None:
                                                content = mydict[index]['content'].encode('iso-8859-1')
                                                #spent a week on this stupid encode...
                                                uid = mydict[index]['uid'].encode('iso-8859-1').encode('utf-8')[1:]
                                                timestamp = mydict[index]['timestamp'].encode('iso-8859-1').encode('utf-8')
                                                index += 1
                                            else:
                                                break

                                          #  print content

                                          #  print uid
                                          #  print timestamp

                                            user_fout = open(os.path.join("../CommentUser/",uid),'a')
                                            user_fout.write(content +'\n')
                                        except Exception as getindexErr:
                                            #print "index_err---------------------------------"
                                            #time.sleep(1)
                                            pass

def Extract_Tweets_to_folder():
    for user_name in os.listdir(all_user_folder):
        user_folder = os.path.join(all_user_folder, user_name)
        if os.path.isdir(user_folder):
            user_all_text = user_name + '_text'
            try:
                os.remove(os.path.join(user_folder, user_all_text))
            except OSError:
                pass
            with open(os.path.join(user_folder, user_all_text),'a') as result:
                for crawling_date in os.listdir(user_folder):

                    date_folder = os.path.join(user_folder,crawling_date)
                    if os.path.isdir(date_folder):
                        #print 'reach date folder'
                        for text_file_names in os.listdir(date_folder):
                            #print 'find text file'
                            with open(os.path.join(date_folder,text_file_names), 'r')as data:
                                if True:
                                    try: mydict = pickle.load(data)
                                    except UnicodeDecodeError:
                                        print "Unicode!"
                                       # time.sleep(1)
                                        continue
                                    except EOFError:
                                      #  print "EOFE"
                                       # time.sleep(1)
                                        break
                                    except IndexError:
                                        print "index"
                                      #  time.sleep(1)
                                        break


                                    #############Tweets:
                                    #############format {'retweet': False, 'timestamp': u'2012-10-28-15-29-18', 'tweet': {'content': u'\xe8\x83\xbd\xe4\xb8...
                                   # print mydict

                                    if True:
                                        try:
                                            if True:
                                                retweet = mydict['retweet']
                                                content = mydict['tweet']['content'].encode('iso-8859-1')
                                                uid = mydict['uid'].encode('iso-8859-1').encode('utf-8')[1:]
                                                timestamp = mydict['timestamp'].encode('iso-8859-1').encode('utf-8')

                                           # print content
                                           # print retweet
                                           # print uid
                                           # print timestamp

                                            user_fout = open(os.path.join("../TweetUser/",uid),'a')
                                            user_fout.write(content +'\n')

                                        except Exception as NotATweet:
                                            #print "index_err---------------------------------"
                                            #time.sleep(1)
                                            break
Extract_Comment_to_folder()
print "Comment Finished================"
Extract_Tweets_to_folder()







                                #    t_content = mydict['tweet']['content'].encode('utf-8')
                                  #  print '======tweet======='
                                  #  print t_content

                                  #  except Exception, err:
                                  #      print "no content"
