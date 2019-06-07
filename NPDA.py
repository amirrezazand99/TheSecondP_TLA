# The second project theory DR.Rahmani
# Thanks to TA(s) team

def change_to_CFG(file):
    my_file = open(file,'r')#.read().replace('\n',"+")
    input_list = []
    for line in my_file:
        line = line.split("\n")
        input_list.append(line)

    for i in range(len(input_list)):
        if input_list[i][-1] == '':
            del input_list[i][-1]
    Stack_start = input_list[3][0]
    var = input_list[1][0]
    var = var.split(',')
    input_stack = input_list[2][0]
    input_stack = input_stack.split(',')
    print(input_stack)
    print(input_list)
    print(var)
    print(Stack_start)

def main():
    input_file = input("Enter your file dir :\n")
    change_to_CFG(input_file)


if __name__ == "__main__":
    main()