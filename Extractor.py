import os
import re

# READS THE FOLDER CONTAINING .PS FILES
folder = "D:/UD/RESEARCH/CODE/testres/"

# THIS IS TO SEE HOW MANY FILES THERE ARE IN THAT FOLDER
# size_of_folder = len(os.listdir(folder))

count = 1
for file in os.listdir(folder):
    # READS THE FILE SEQUENTIALLY THAT IS: ST1.PS, ST2.PS, ...
    with open(os.path.join(folder + "st" + str(count) + ".ps")) as f:
        print("Reading file: ", folder + "st" + str(count) + ".ps")
        temp_1 = f.readlines()
    # REMOVING ALL THE NEW LINE CHARACTERS
    l_1 = [x[:-1] for x in temp_1]
    count += 1

    # THIS LIST STORES THE LINES AFTER USING REGEX SEARCH
    new_li = []
    for i in range(len(l_1)):
        # USING REGEX TO GET ALL THE COORDINATES
        r = re.compile(".*(DT|@C)")
        new_li = list(filter(r.match, l_1))

    # THIS PRINTS THE ELEMENTS OF "new_li" THAT CONTAINS THE LINES AFTER PERFORMING REGEX SEARCH
    # for x in new_li:
    #     print(x)
    # SAMPLE OUTPUT OF ABOVE CODE:
    #     / DT {
    #     .8883551955223082  .0374859571456909  DT
    #     .2754923105239867  .6448852419853210  DT
    #     % @ C  .7038321580257279  .0971825861751558
    #     % @ C  .3383475051243485  .5711681220792270

    # THIS LIST STORES ALL THE LINES AFTER REMOVING THE TAB "\t" ELEMENT.
    _ = []
    for j in range(len(new_li)):
        # REMOVING TAB
        li = list(new_li[j].split("\t"))
        if len(li) != 1:
            _.append([float(li[1]), float(li[2])])

    # THIS PRINTS THE FINAL RESULT LIST AFTER REMOVING ALL THE TAB ELEMENTS. WHICH CONTAINS ALL THE COORDINATES REQUIRED
    # FOR MST
    # for y in _:
    #     print(y)
    # SAMPLE OUTPUT OF ABOVE CODE:
    #     [0.8883551955223082, 0.0374859571456909]
    #     [0.2754923105239867, 0.644885241985321]
    #     [0.2120095491409301, 0.2086731791496276]

    with open("STM.txt", 'a') as f:
        f.write(str(_) + "\n")
print("Process Finished!!")
