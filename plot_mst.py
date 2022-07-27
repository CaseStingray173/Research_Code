from mst_routine import euc_dist_mat
from mst_instance import mst_instance
from Graph import draw_mst
import numpy as np
import ast
import matplotlib.pyplot as plt


folder = "D:/UD/RESEARCH/CODE/Test/"


def test_mst():
    # READING THE FILE
    with open("DEEP-Steiner.txt") as f1:
        temp_1 = f1.readlines()
    # REMOVING ALL THE NEW LINE CHARACTERS
    l_1 = [x[:-1] for x in temp_1]

    # READING THE FILE
    with open("MST.txt") as f2:
        temp_2 = f2.readlines()
    # REMOVING ALL THE NEW LINE CHARACTERS
    l_2 = [x[:-1] for x in temp_2]

    # READING THE FILE
    with open("STM.txt") as f3:
        temp_3 = f3.readlines()
    # REMOVING ALL THE NEW LINE CHARACTERS
    l_3 = [x[:-1] for x in temp_3]

    # USED TO NAME THE PDF FILES
    counter = 1

    for _ in range(0, 5):
        # CONVERTING FROM STRING TO LIST
        line_1 = ast.literal_eval(l_1[_])
        line_2 = ast.literal_eval(l_2[_])
        line_3 = ast.literal_eval(l_3[_])

        # CONVERTING THE LIST TO NP ARRAY
        DST = np.array(line_1)
        MST = np.array(line_2)
        STM = np.array(line_3)

        # GETTING THE MIN_WEIGHT FOR EACH ENTRY AND RATIO
        min_w_1 = mst_instance(DST)
        # min_w_2 = mst_instance(MST)
        min_w_3 = mst_instance(STM)

        ratio = min_w_1 / min_w_3

        # GETTING THE DISTANCE MATRIX
        X = euc_dist_mat(DST)
        X1 = euc_dist_mat(MST)
        X2 = euc_dist_mat(STM)

        # GETTING THE EDGE LIST
        edge_list = draw_mst(X)
        edge_list_1 = draw_mst(X1)
        edge_list_2 = draw_mst(X2)

        # PLOTTING THE COORDINATES FROM THE NP ARRAY WE HAVE
        plt.scatter(DST[:, 0], DST[:, 1], label="DST", c='r')
        plt.scatter(MST[:, 0], MST[:, 1], label="MST", c='b')
        plt.scatter(STM[:, 0], STM[:, 1], label="STM", c='g')

        plt.legend(bbox_to_anchor=(0.77, 1.13), ncol=3)
        plt.xlabel("X")
        plt.ylabel("Y")

        # JOINING THE COORDINATES WITH LINES USING THE EDGE LIST
        for edge in edge_list:
            i, j = edge
            plt.plot([DST[i, 0], DST[j, 0]], [DST[i, 1], DST[j, 1]], c='r')
        for edge in edge_list_1:
            i, j = edge
            plt.plot([MST[i, 0], MST[j, 0]], [MST[i, 1], MST[j, 1]], c='b')
        for edge in edge_list_2:
            i, j = edge
            plt.plot([STM[i, 0], STM[j, 0]], [STM[i, 1], STM[j, 1]], c='g')

        plt.savefig(folder + str(counter) + "_" + str(round(ratio, 3)) + ".pdf",
                    bbox_inches="tight")
        plt.clf()
        counter += 1

    print("All the graphs have been saved as pdf")

# FROM PREVIOUS VERSION OF THE CODE
    # SEL = np.array(arr)
    # ORI = np.array(arr1)

    # Prints the weight of mst
    # min_w = mst_instance(SEL)
    # print("The minimum weight of the MST: ", min_w)
    # # Prints the weight of mst
    # min_w_1 = mst_instance(ORI)
    # print("The minimum weight of the MST: ", min_w_1)

    # Using the mst_routine.py to get the Euclidean distance matrix

#     for _ in range(1, 3):
#         P = rand_coords()
#         P1 = rand_coords()
#
#         X = euc_dist_mat(P)
#         X1 = euc_dist_mat(P1)
#
#         edge_list = draw_mst(X)
#         edge_list_1 = draw_mst(X1)
#
#         plt.scatter(P[:, 0], P[:, 1], label="P", c='k')
#         plt.scatter(P1[:, 0], P1[:, 1], label="P1", c='b')
#         plt.legend(bbox_to_anchor=(0.65, 1.13), ncol=2)
#
#         plt.xlabel("X")
#         plt.ylabel("Y")
#
#         for edge in edge_list:
#             i, j = edge
#             plt.plot([P[i, 0], P[j, 0]], [P[i, 1], P[j, 1]], c='k')
#
#         for edge in edge_list_1:
#             i, j = edge
#             plt.plot([P1[i, 0], P1[j, 0]], [P1[i, 1], P1[j, 1]], c='b')
#         print(str(_))
#         plt.savefig("D:/UD/RESEARCH/CODE/Graphs/MST_Graph_" + str(_) + ".pdf", bbox_inches="tight")
#         plt.clf()
#     # plt.show()
#
# PREVIOUS VERSION OF THE CODE ENDS HERE


if __name__ == "__main__":
    test_mst()
