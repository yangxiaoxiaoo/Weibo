import numpy as np
from scipy.stats import norm
import os

def pre_CDF_title(input_data1,input_data2, point,input_title):

    Range_low = float(min(input_data1))
    Range_up = float(max(input_data1))
    sorted_data = sorted(input_data1)


    print 'Range_up = '
    print Range_up
    print 'Range_low = '
    print Range_low
    step_len = (Range_up - Range_low)/point
    count = [1]*point
    CDF = list()
    N = len(input_data1)
    print 'N ='
    print N

    for i in range(1, N):
        for j in range(1, point):
            if input_data1[i] <= Range_low + j * step_len:
                count[j] += 1

    for item in count:

        CDF.append(float(item/float(N)))



    Range_low2 = float(min(input_data2))
    Range_up2 = float(max(input_data2))
    sorted_data2 = sorted(input_data2)

    print 'Range_up2 ='
    print Range_up2
    print 'Range_low2 ='
    print Range_low2
    #step_len2 = (Range_up2 - Range_low2)/point
    #TO COMPARE FRIENDS NUMBERS AND OTHER FEATURES, I HAVE TO USE THE SAME SCALE HERE
    step_len2 = step_len

    print 'step_lenth2 = '
    print step_len2

    count2 = [1]*point
    CDF2 = list()
    N2 = len(input_data2)
    print 'N2 ='
    print N2

    for i in range(1, N2):
        for j in range(1, point):
            if input_data2[i] <= Range_low2 + j * step_len2:
                count2[j] += 1

    for item in count2:

        CDF2.append(float(item/float(N2)))
        print 'item ='
        print item
        print float(item/float(N2))

    x = list()
    for count in range(0,len(CDF)):
        x.append(float(count)*step_len)

    fp = open(input_title,'w')

    for i in range(1, len(x), 1):
        print x[i]
        fp.write(str(x[i]) + ' '+ str(CDF[i])+'\n')

#=================================================================
if __name__ == "__main__":
    UserCountList = list()
    CommentFolder = "../CommentUser/"
    for user_name in os.listdir(CommentFolder):
        infile = open(os.path.join(CommentFolder, user_name),'r')
        count = len(infile.readlines())
        UserCountList.append(count)

    pre_CDF_title(UserCountList,UserCountList,2000, "UserCommentCDP_raw")

