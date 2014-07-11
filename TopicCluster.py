from cluster import KMeansClustering
data = "../CommentUserTopic.txt"
cluster_in = list()
fin = open(data, 'r')
for line in fin:
    str = (line.split(']')[0] + ']')
    vec = eval(str)
    #print vec[0]
    cluster_in.append(vec)
    cl = KMeansClustering(cluster_in)
    clusters = cl.getclusters(2)
