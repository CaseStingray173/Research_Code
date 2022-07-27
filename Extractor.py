import os
import re

folder = "D:/UD/RESEARCH/CODE/testres/"
size_of_folder = len(os.listdir(folder))

count = 1
for file in os.listdir(folder):
    with open(os.path.join(folder + "st" + str(count) + ".ps")) as f:
        print("Reading file: ", folder + "st" + str(count) + ".ps")
        temp_1 = f.readlines()
    # REMOVING ALL THE NEW LINE CHARACTERS
    l_1 = [x[:-1] for x in temp_1]
    count += 1

    new_li = []
    for i in range(len(l_1)):
        # USING REGEX TO GET ALL THE COORDINATES
        r = re.compile(".*(DT|@C)")
        new_li = list(filter(r.match, l_1))

    _ = []
    for j in range(len(new_li)):
        # REMOVING TAB
        li = list(new_li[j].split("\t"))
        if len(li) != 1:
            _.append([float(li[1]), float(li[2])])
    # print(_)
    with open("test.txt", 'a') as f:
        f.write(str(_) + "\n")
print("Process Finished!!")
