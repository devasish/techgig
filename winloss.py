
def main():
    t = int(input())
    op_list = []
    for i in range(t):
        v_list = []
        p_list = []

        n = int(input())
        v_inp = input()
        p_inp = input()

        v_list = v_inp.split()
        p_list = p_inp.split()

        v_list = [int(x) for x in v_list]
        p_list = [int(x) for x in p_list]

        v_list.sort()
        p_list.sort()

        is_win = True

        for k in range(n):
            if p_list[k] <= v_list[k]:
                is_win = False
                break

        op = 'WIN' if is_win else 'LOSE'
        op_list.append(op)

    for i in range(t):
        print(op_list[i])




main()
