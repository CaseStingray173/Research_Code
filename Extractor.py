from mst_instance import mst_instance
from mst_routine import euc_dist_mat
from Graph import draw_mst
import numpy as np
import matplotlib.pyplot as plt
import os
import re

folder = "D:/UD/RESEARCH/CODE/testres/"
size_of_folder = len(os.listdir(folder))

count = 1
for file in os.listdir(folder):
    with open (os.path.join(folder+"st"+str(count)+".ps")) as f:
        print("Reading file: ", folder+"st"+str(count)+".ps")
        temp_1 = f.readlines()
    # REMOVING ALL THE NEW LINE CHARACTERS
    l_1 = [x[:-1] for x in temp_1]

    count += 1

    new_li = []
    for i in range(len(l_1)):
        r = re.compile(".*(DT|@C)")
        new_li = list(filter(r.match, l_1))

    _ = []
    for j in range(len(new_li)):
        li = list(new_li[j].split("\t"))
        if len(li) != 1:
            _.append([float(li[1]), float(li[2])])
    #print(_)
    with open("test.txt", 'a') as f:
        f.write(str(_)+"\n")
print("Process Finished!!")


# with open(folder+"st1.ps") as f1:
#     temp_1 = f1.readlines()
# # REMOVING ALL THE NEW LINE CHARACTERS
# l_1 = [x[:-1] for x in temp_1]

# __ = np.array(_)
#
# length = mst_instance(__)
# print(length)

# X = euc_dist_mat(__)
#
# # GETTING THE EDGE LIST
# edge_list = draw_mst(X)
#
# # PLOTTING THE COORDINATES FROM THE NP ARRAY WE HAVE
# plt.scatter(__[:, 0], __[:, 1], label="SEL", c='r')
#
# plt.legend(bbox_to_anchor=(0.65, 1.13), ncol=2)
# plt.xlabel("X")
# plt.ylabel("Y")
#
# # JOINING THE COORDINATES WITH LINES USING THE EDGE LIST
# for edge in edge_list:
#     i, j = edge
#     plt.plot([__[i, 0], __[j, 0]], [__[i, 1], __[j, 1]], c='r')
#
# plt.show()

