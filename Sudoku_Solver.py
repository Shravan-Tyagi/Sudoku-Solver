#Made By Shravan




#Given Sudoku To Solve:

given = {
         1:[[[5],[3],[]],[[6],[],[]],[[],[9],[8]]], 2:[[[],[7],[]],[[1],[9],[5]],[[],[],[]]], 3:[[[],[],[]],[[],[],[]],[[],[6],[]]],
         4:[[[8],[],[]],[[4],[],[]],[[7],[],[]]], 5:[[[],[6],[]],[[8],[],[3]],[[],[2],[]]], 6:[[[],[],[3]],[[],[],[1]],[[],[],[6]]],
         7:[[[],[6],[]],[[],[],[]],[[],[],[]]], 8:[[[],[],[]],[[4],[1],[9]],[[],[8],[]]], 9:[[[2],[8],[]],[[],[],[5]],[[],[7],[9]]]
         }


#Boxes initiated:

box1 = {"R1":[],"R2":[],"R3":[],"C1":[],"C2":[],"C3":[]}
box2 = {"R1":[],"R2":[],"R3":[],"C1":[],"C2":[],"C3":[]}
box3 = {"R1":[],"R2":[],"R3":[],"C1":[],"C2":[],"C3":[]}
box4 = {"R1":[],"R2":[],"R3":[],"C1":[],"C2":[],"C3":[]}
box5 = {"R1":[],"R2":[],"R3":[],"C1":[],"C2":[],"C3":[]}
box6 = {"R1":[],"R2":[],"R3":[],"C1":[],"C2":[],"C3":[]}
box7 = {"R1":[],"R2":[],"R3":[],"C1":[],"C2":[],"C3":[]}
box8 = {"R1":[],"R2":[],"R3":[],"C1":[],"C2":[],"C3":[]}
box9 = {"R1":[],"R2":[],"R3":[],"C1":[],"C2":[],"C3":[]}


#Numbers Distribution To Boxes:

for i in given:
    if i==1:
        for j in range(len(given[i])):
            if j==0:
                box1["R1"] = given[i][j]
                box1["C1"].append(given[i][j][0])
                box1["C2"].append(given[i][j][1])
                box1["C3"].append(given[i][j][2])
            if j==1:
                box1["R2"] = given[i][j]
                box1["C1"].append(given[i][j][0])
                box1["C2"].append(given[i][j][1])
                box1["C3"].append(given[i][j][2])
            if j==2:
                box1["R3"] = given[i][j]
                box1["C1"].append(given[i][j][0])
                box1["C2"].append(given[i][j][1])
                box1["C3"].append(given[i][j][2])

    if i==2:
        for j in range(len(given[i])):
            if j==0:
                box2["R1"] = given[i][j]
                box2["C1"].append(given[i][j][0])
                box2["C2"].append(given[i][j][1])
                box2["C3"].append(given[i][j][2])
            if j==1:
                box2["R2"] = given[i][j]
                box2["C1"].append(given[i][j][0])
                box2["C2"].append(given[i][j][1])
                box2["C3"].append(given[i][j][2])
            if j==2:
                box2["R3"] = given[i][j]
                box2["C1"].append(given[i][j][0])
                box2["C2"].append(given[i][j][1])
                box2["C3"].append(given[i][j][2])

    if i==3:
        for j in range(len(given[i])):
            if j==0:
                box3["R1"] = given[i][j]
                box3["C1"].append(given[i][j][0])
                box3["C2"].append(given[i][j][1])
                box3["C3"].append(given[i][j][2])
            if j==1:
                box3["R2"] = given[i][j]
                box3["C1"].append(given[i][j][0])
                box3["C2"].append(given[i][j][1])
                box3["C3"].append(given[i][j][2])
            if j==2:
                box3["R3"] = given[i][j]
                box3["C1"].append(given[i][j][0])
                box3["C2"].append(given[i][j][1])
                box3["C3"].append(given[i][j][2])

    if i == 4:
        for j in range(len(given[i])):
            if j == 0:
                box4["R1"] = given[i][j]
                box4["C1"].append(given[i][j][0])
                box4["C2"].append(given[i][j][1])
                box4["C3"].append(given[i][j][2])
            if j == 1:
                box4["R2"] = given[i][j]
                box4["C1"].append(given[i][j][0])
                box4["C2"].append(given[i][j][1])
                box4["C3"].append(given[i][j][2])
            if j == 2:
                box4["R3"] = given[i][j]
                box4["C1"].append(given[i][j][0])
                box4["C2"].append(given[i][j][1])
                box4["C3"].append(given[i][j][2])

    if i == 5:
        for j in range(len(given[i])):
            if j == 0:
                box5["R1"] = given[i][j]
                box5["C1"].append(given[i][j][0])
                box5["C2"].append(given[i][j][1])
                box5["C3"].append(given[i][j][2])
            if j == 1:
                box5["R2"] = given[i][j]
                box5["C1"].append(given[i][j][0])
                box5["C2"].append(given[i][j][1])
                box5["C3"].append(given[i][j][2])
            if j == 2:
                box5["R3"] = given[i][j]
                box5["C1"].append(given[i][j][0])
                box5["C2"].append(given[i][j][1])
                box5["C3"].append(given[i][j][2])

    if i == 6:
        for j in range(len(given[i])):
            if j == 0:
                box6["R1"] = given[i][j]
                box6["C1"].append(given[i][j][0])
                box6["C2"].append(given[i][j][1])
                box6["C3"].append(given[i][j][2])
            if j == 1:
                box6["R2"] = given[i][j]
                box6["C1"].append(given[i][j][0])
                box6["C2"].append(given[i][j][1])
                box6["C3"].append(given[i][j][2])
            if j == 2:
                box6["R3"] = given[i][j]
                box6["C1"].append(given[i][j][0])
                box6["C2"].append(given[i][j][1])
                box6["C3"].append(given[i][j][2])

    if i == 7:
        for j in range(len(given[i])):
            if j == 0:
                box7["R1"] = given[i][j]
                box7["C1"].append(given[i][j][0])
                box7["C2"].append(given[i][j][1])
                box7["C3"].append(given[i][j][2])
            if j == 1:
                box7["R2"] = given[i][j]
                box7["C1"].append(given[i][j][0])
                box7["C2"].append(given[i][j][1])
                box7["C3"].append(given[i][j][2])
            if j == 2:
                box7["R3"] = given[i][j]
                box7["C1"].append(given[i][j][0])
                box7["C2"].append(given[i][j][1])
                box7["C3"].append(given[i][j][2])

    if i == 8:
        for j in range(len(given[i])):
            if j == 0:
                box8["R1"] = given[i][j]
                box8["C1"].append(given[i][j][0])
                box8["C2"].append(given[i][j][1])
                box8["C3"].append(given[i][j][2])
            if j == 1:
                box8["R2"] = given[i][j]
                box8["C1"].append(given[i][j][0])
                box8["C2"].append(given[i][j][1])
                box8["C3"].append(given[i][j][2])
            if j == 2:
                box8["R3"] = given[i][j]
                box8["C1"].append(given[i][j][0])
                box8["C2"].append(given[i][j][1])
                box8["C3"].append(given[i][j][2])

    if i == 9:
        for j in range(len(given[i])):
            if j == 0:
                box9["R1"] = given[i][j]
                box9["C1"].append(given[i][j][0])
                box9["C2"].append(given[i][j][1])
                box9["C3"].append(given[i][j][2])
            if j == 1:
                box9["R2"] = given[i][j]
                box9["C1"].append(given[i][j][0])
                box9["C2"].append(given[i][j][1])
                box9["C3"].append(given[i][j][2])
            if j == 2:
                box9["R3"] = given[i][j]
                box9["C1"].append(given[i][j][0])
                box9["C2"].append(given[i][j][1])
                box9["C3"].append(given[i][j][2])



#box1 = {"R1":[],"R2":[],"R3":[],"C1":[],"C2":[],"C3":[]}
#box1 = {'R1': [[], [5], [8]], 'R2': [[], [2], []], 'R3': [[], [], [9]], 'C1': [[], [], []], 'C2': [[5], [2], []], 'C3': [[8], [], [9]]}



matrix = [box1,box2,box3,box4,box5,box6,box7,box8,box9]
not_full = True
iter_no = 0
unsolved = str(matrix)
print(unsolved)

while iter_no<300:
    #global unsolved
    iter_no += 1
    unsolved = str(matrix)

    for i in matrix:
        init = []
        not_init = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        #Checking the box:
        for k in i["R1"]:
            if k != []:
                init.append(k[0])
                not_init.remove(k[0])
        for k in i["R2"]:
            if k != []:
                init.append(k[0])
                not_init.remove(k[0])
        for k in i["R3"]:
            if k != []:
                init.append(k[0])
                not_init.remove(k[0])

        search_row = []
        search_column = []
        if i == box1:
            search_row = [box2,box3]
            search_column = [box4,box7]
        if i == box2:
            search_row = [box1,box3]
            search_column = [box5, box8]
        if i == box3:
            search_row = [box1,box2]
            search_column = [box6, box9]
        if i == box4:
            search_row = [box5,box6]
            search_column = [box1, box7]
        if i == box5:
            search_row = [box4,box6]
            search_column = [box2, box8]
        if i == box6:
            search_row = [box4,box5]
            search_column = [box3, box9]
        if i == box7:
            search_row = [box8,box9]
            search_column = [box1, box4]
        if i == box8:
            search_row = [box7,box9]
            search_column = [box2, box5]
        if i == box9:
            search_row = [box7,box8]
            search_column = [box3, box6]


        #Checking Rows:

        check_list = [i["R1"][0], i["R1"][1], i["R1"][2], i["R2"][0], i["R2"][1], i["R2"][2], i["R3"][0], i["R3"][1],
                      i["R3"][2]]

        for j in range(len(check_list)):
            if check_list[j] == []:
                if j == 0:
                    single_init = list(init)
                    single_not_init = list(not_init)
                    for k in search_row:
                        for x in k["R1"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    for k in search_column:
                        for x in k["C1"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    if len(single_not_init) == 1:
                        i["R1"][0] = single_not_init

                if j == 1:
                    single_init = list(init)
                    single_not_init = list(not_init)
                    for k in search_row:
                        for x in k["R1"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    for k in search_column:
                        for x in k["C2"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    if len(single_not_init) == 1:
                        i["R1"][1] = single_not_init

                if j == 2:
                    single_init = list(init)
                    single_not_init = list(not_init)
                    for k in search_row:
                        for x in k["R1"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    for k in search_column:
                        for x in k["C3"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    if len(single_not_init) == 1:
                        i["R1"][2] = single_not_init

                if j == 3:
                    single_init = list(init)
                    single_not_init = list(not_init)
                    for k in search_row:
                        for x in k["R2"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    for k in search_column:
                        for x in k["C1"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    if len(single_not_init) == 1:
                        i["R2"][0] = single_not_init

                if j == 4:
                    single_init = list(init)
                    single_not_init = list(not_init)
                    for k in search_row:
                        for x in k["R2"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    for k in search_column:
                        for x in k["C2"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    if len(single_not_init) == 1:
                        i["R2"][1] = single_not_init

                if j == 5:
                    single_init = list(init)
                    single_not_init = list(not_init)
                    for k in search_row:
                        for x in k["R2"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    for k in search_column:
                        for x in k["C3"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    if len(single_not_init) == 1:
                        i["R2"][2] = single_not_init

                if j == 6:
                    single_init = list(init)
                    single_not_init = list(not_init)
                    for k in search_row:
                        for x in k["R3"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    for k in search_column:
                        for x in k["C1"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    if len(single_not_init) == 1:
                        i["R3"][0] = single_not_init

                if j == 7:
                    single_init = list(init)
                    single_not_init = list(not_init)
                    for k in search_row:
                        for x in k["R3"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    for k in search_column:
                        for x in k["C2"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    if len(single_not_init) == 1:
                        i["R3"][1] = single_not_init

                if j == 8:
                    single_init = list(init)
                    single_not_init = list(not_init)
                    for k in search_row:
                        for x in k["R3"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    for k in search_column:
                        for x in k["C3"]:
                            if x != []:
                                if x[0] not in single_init:
                                    single_init.append(x[0])
                                    single_not_init.remove(x[0])
                    if len(single_not_init) == 1:
                        i["R3"][2] = single_not_init

        not_full = False
        for j in matrix:
            for k in j:
                for x in j[k]:
                    if not x:
                        not_full = True

print()
print(iter_no)
print("\n\n")
#print(matrix)
solved = str(matrix)
print(unsolved)
print(solved)

if solved == unsolved:
    print("No Change")

"""
box1 = {"R1":[0,0,0],"R2":[0,0,0],"R3":[0,0,0],"C1":[0,0,0],"C2":[0,0,0],"C3":[0,0,0]}
box2 = []
box3 = []
box4 = []
box5 = []
box6 = []
box7 = []
box8 = []
box9 = []
matrix = [[box1,box2,box3],[box4,box5,box6],[box7,box8,box9]]

box1["R1"][1] = 2
print(box1["R1"])

def show():
    print(matrix)


#show()

"""