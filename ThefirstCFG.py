
## The first question of the second projct of TLA
## Thanks to DR.Rahmani
## Thanks to TA(s) team
## input is from a txt file
##output write in console
## Function base
##@auther AmirReza Zand 96522159;
## Ali Lesani 95521405;

def process_input(File):
    input_list = []
    for line in File:
        line = line.split("\n")
        input_list.append(line)

    for i in range(len(input_list)):
        if input_list[i][-1] == '':
            del input_list[i][-1]

    List = []
    for i in range(len(input_list)):
        List.append(input_list[i][0])

    List = [s.replace('->', '') for s in List]
    List = [s.replace('*', '') for s in List]
    List = [s.replace('_', '') for s in List]

    return List

def main_process(List):
    number = int(List[0])
    alphabet = List[1]
    alphabet = alphabet.split(",")
    transition = []
    non_transiton = []
    for i in range(4,len(List)):
        local_var = List[i].split(",")
        if local_var[3] != "" :
            transition.append(List[i])
        else:
            non_transiton.append(List[i])

    List_of_CFG = []
    for l in range(number):
        if l == 0:
            for i in range(len(transition)):
                local_var = transition[i].split(",")
                local_str = ""
                local_str = local_str + str(local_var[0])
                local_str = local_str + str(local_var[2])
                local_str = local_str + str(local_var[4])
                List_of_CFG.append(local_str)
                for j in range(number-1):
                    local_str = ""
                    local_str = local_str.join(local_var[1])
                    List_of_CFG.append(local_str)
                    for m in range(0,number):

                        local_str = ""
                        if len(local_var[3])>1:
                            local_str = local_str.join(str("("+local_var[0]+str(local_var[3][0])+"q"+str(m)+")"+"("+"q"+str(m)+str(local_var[3][1])+local_var[4]+")"))
                        else:
                            local_str = local_str.join(str("(" + local_var[0] + str(local_var[3][0]) + "q" + str(m) + ")"))
                        List_of_CFG.append(local_str)
        else:
            for i in range(len(transition)):
                local_var = transition[i].split(",")
                local_str = ""
                local_str = local_str + str(local_var[0])
                local_str = local_str + str(local_var[2])
                local_str = local_str + "qf"
                List_of_CFG.append(local_str)
                for j in range(number - 1):
                    local_str = ""
                    local_str = local_str.join(local_var[1])
                    List_of_CFG.append(local_str)
                    for m in range(0, number):
                        local_str = ""
                        if len(local_var[3]>1):
                            local_str = local_str.join(str(
                                "(" + local_var[0] + str(local_var[3][0]) + "q" + str(m) + ")" + "(" + "q" + str(m) + str(
                                    local_var[3][1]) + "qf" + ")"))
                        else:
                            local_str = local_str.join(str(
                                "(" + local_var[0] + str(local_var[3][0]) + "q" + str(m) + ")"))

                        List_of_CFG.append(local_str)


    others = Other_transition(non_transiton)
    for i in range(len(others)):

        List_of_CFG.append(others[i])
    return List_of_CFG

def Other_transition(lst):
    CFG = []
    for i in range(len(lst)):
        string = ""
        Var = lst[i].split(",")
        string = string + str(Var[0])
        string = string + str(Var[2])
        string = string + str(Var[4])
        string = string + " -> "
        if Var[1] != "":
            string = string + str(Var[1])
        else:
            string = string + "_"

        CFG.append(string)
    return CFG





def main():
    input_file = input("Please Enter The File Dir \n")
    input_file = open(input_file , 'r')
    proceture = process_input(input_file)
    Main_list = main_process(proceture)

    for i in range(4*int(proceture[0])):
        print(Main_list[0] + " -> " + Main_list [1] + Main_list[2] + " | " + Main_list[1] + Main_list[3])
        for j in range(2*int(proceture[0])):
            del Main_list[0]

    for i in range(len(Main_list)):
        print(Main_list[i])





if __name__ == "__main__":
    main()