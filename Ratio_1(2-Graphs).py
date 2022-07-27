import ast
import os
import numpy as np
from mst_instance import mst_instance

folder = "D:/UD/RESEARCH/CODE/Graphs/"

# READING THE FILE
with open("selecte_a.txt") as f1:
    temp_1 = f1.readlines()
# REMOVING ALL THE NEW LINE CHARACTERS
l_1 = [x[:-1] for x in temp_1]

# READING THE FILE
with open("origin_a.txt") as f2:
    temp_2 = f2.readlines()
# REMOVING ALL THE NEW LINE CHARACTERS
l_2 = [x[:-1] for x in temp_2]

ratio_list = []
for _ in range(20001, 30001):
    # CONVERTING FROM STRING TO LIST
    line_1 = ast.literal_eval(l_1[_])
    line_2 = ast.literal_eval(l_2[_])

    # CONVERTING THE LIST TO NP ARRAY
    SEL = np.array(line_1)
    ORI = np.array(line_2)

    # GETTING THE MIN_WEIGHT FOR EACH ENTRY AND RATIO
    min_w_1 = mst_instance(SEL)
    min_w_2 = mst_instance(ORI)
    ratio = min_w_1 / min_w_2
    ratio_list.append(round(ratio, 3))
print("Stored all the ratios in a list")

print(ratio_list)

# THIS IS USED TO RENAME THE FILE USING THE RATIO
# count = 1
# index = 0
# for file in os.listdir(folder):
#     src = folder + file
#     dst = folder + "Graph_" + str(count) + "_ratio_" + str(ratio_list[index]) + ".pdf"
#     os.rename(src, dst)
#     count += 1
#     index += 1
# print("Finished renaming all the files")
#
# result = os.listdir(folder)
# print(result)


# with open("selecte_a.txt") as f1:
#     lines = f1.readlines()
# l_1 = [x[:-1] for x in lines]
#
# counter = 0
# for i in range(20001,30001):
#     counter += 1
# print(counter)
