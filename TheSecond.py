
## The second question of the second projct of TLA
## Thanks to DR.Rahmani
## Thanks to TA(s) team
## input is from a txt file
##output write in console
##Function base
##@auther AmirReza Zand 96522159
## Ali Lesani 95521405;

def process_input(File):
    input_list = []
    for line in File:
        line = line.split("\n")
        input_list.append(line)

    for i in range(len(input_list)):
        if input_list[i][-1] == '':
            del input_list[i][-1]
    return input_list

def find_first_last(List):
    last_first = []
    first = List[4][0]
    first = first.split(',')
    for i in range(len(first)):
        if first[i][0] == "-":
            last_first.append(first[i][2:])
            break
    last = List[-1][0]
    last = last.split(',')
    for i in range(len(last)):
        if last[i][0] == "*":
            last_first.append(last[i][1:])
            break

    return last_first

def peek_stack(stack):
    if stack:
        return stack[-1]

def main():
    input_file = input("Please Enter The File Dir \n")
    input_file = open(input_file , 'r')
    proceture = process_input(input_file)
    found = find_first_last(proceture)
    Start = found[0]

    last = found[1]

    Grammar = []
    for i in range(4,len(proceture)):
        Grammar.append(proceture[i])

    final_grammar = []
    for i in range(len(Grammar)):
        final_grammar.append(Grammar[i][0])

    Grammar = [s.replace('->', '') for s in final_grammar]
    Grammar = [s.replace('*', '') for s in Grammar]
    Grammar = [s.replace('_', '') for s in Grammar]
    independent_var = Grammar[-1]
    independent_var = independent_var.split(",")
    independent_var = "(" + independent_var[0] + independent_var[2] + independent_var[4] + ")"


    Stack = ["$"]
    input_str = input("Please Enter A STR \n")

    reporter_stack = []
    length  = len(Grammar)
    for i in range(len(input_str)):
        for j in range(len(Grammar)):
            current_grammar = Grammar[j].split(",")
            peek = peek_stack(Stack)


            if(input_str[i] == current_grammar[1] and peek == current_grammar[2] and Start == current_grammar[0]):
                Start = current_grammar[4]
                Stack.pop()
                for k in range(len(current_grammar[3])-1,-1,-1):

                    Stack.append(current_grammar[3][k])
                    reporter_stack.append(current_grammar[3][k])

                break


    final_dir = Grammar.pop()
    final_dir = final_dir.split(",")
    aux_str = ""



    for i in range(len(Stack)):
        aux_str = aux_str.join(Stack[i])

    if(aux_str == final_dir[2]):
        print("Output")
        print("True")
        final_list_of_TLA = show_dir(Start , reporter_stack, independent_var, input_str)

        for j in range(len(final_list_of_TLA)-1):
            print(final_list_of_TLA[j] , end = " => ")
        print(final_list_of_TLA[len(final_list_of_TLA)-1])

    else:
        print("Output")
        print("False")


def show_dir(Start , reporter_stack , independent_var , input_str):
    Stack =[independent_var]
    for i in range(1,len(input_str)):
        Stack.append(str(input_str[0:i] + "(" + Start + reporter_stack[i] + Start +  ")" + independent_var))
    Stack.append(input_str + independent_var)
    Stack.append(input_str)
    return Stack

if __name__ == "__main__":
    main()