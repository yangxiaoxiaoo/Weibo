import CDF_UserText

UserCountList = list()
Count = open("../Repeated_Count.txt",'r')
for line in Count:
    username = line.split(' ')[0]
    repeat = line.split(' ')[1]
    if repeat > 0.5:
        UserCountList.append(repeat)

CDF_UserText.pre_CDF_title(UserCountList,UserCountList,500, "UserCount_raw")