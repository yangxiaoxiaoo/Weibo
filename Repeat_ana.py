def threshold_stat(above):
    input = "../Repeated_Count.txt"
    fp = open(input, 'r')
    linecount = 0
    abovecount = 0
    for line in fp:
        linecount += 1
        username = line.split(' ')[0]
        repeat = line.split(' ')[1]
        if int(repeat) > above:
            abovecount += 1
    rate = float(abovecount) / float(linecount)
    return rate

output = "../Ana_Repeated_Count.txt"
for threshold in range(0,200,10):
    fp2 = open(output, 'a')
    fp2.write("Threshold_n: " + str(threshold) + " The_rate_of_above_n_times_repeat:: " + str(threshold_stat(threshold)) + "\n" )