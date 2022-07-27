from mst_routine import euc_dist_mat
from mst_instance import mst_instance
from Graph import draw_mst
import numpy as np
import ast
import matplotlib.pyplot as plt


def test_mst():
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

    # COUNTER IS USED TO NAME THE PDF FILES
    counter = 1

    # GETS THE LAST 10000 ENTRIES
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

        # GETTING THE DISTANCE MATRIX
        X = euc_dist_mat(SEL)
        X1 = euc_dist_mat(ORI)

        # GETTING THE EDGE LIST
        edge_list = draw_mst(X)
        edge_list_1 = draw_mst(X1)

        # PLOTTING THE COORDINATES FROM THE NP ARRAY WE HAVE
        plt.scatter(SEL[:, 0], SEL[:, 1], label="SEL", c='r')
        plt.scatter(ORI[:, 0], ORI[:, 1], label="ORI", c='b')

        plt.legend(bbox_to_anchor=(0.65, 1.13), ncol=2)
        plt.xlabel("X")
        plt.ylabel("Y")

        # JOINING THE COORDINATES WITH LINES USING THE EDGE LIST
        for edge in edge_list:
            i, j = edge
            plt.plot([SEL[i, 0], SEL[j, 0]], [SEL[i, 1], SEL[j, 1]], c='r')
        for edge in edge_list_1:
            i, j = edge
            plt.plot([ORI[i, 0], ORI[j, 0]], [ORI[i, 1], ORI[j, 1]], c='b')

        plt.savefig("D:/UD/RESEARCH/CODE/Graphs/Graph_" + str(counter) + "_ratio_" + str(ratio) + ".pdf",
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
