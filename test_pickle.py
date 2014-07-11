# -*- coding: utf-8 -*-
import pickle
import time

def dump_pickle():
    user={}
    user['id']=1
    user['name'] = '列化'
    print user
    with open('../Test_pickle_file','wb') as f:
        pickle.dump(user, f)
        print "written "

def load_pickle():
    with open('../Test_pickle_file','rb') as f:
        user = pickle.load(f)
        print user
        print user['name']
        print user['name'].decode('utf-8')

dump_pickle()
time.sleep(1)
load_pickle()
print '\xe4\xbb\x80\xe4\xb9\x88\xe6\x97\xb6\xe5\x80\x99\xe9\x83\xbd\xe7\xbe\x8e\xe4\xb8\xbd\xe5\xa4\xa7\xe6\x96\xb9[\xe5\x8f\xaf\xe7\x88\xb1]'