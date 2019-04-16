def main():
    t = int(input())


    for ti in range(t):
        n = int(input())
        tickets_str = input()
        # print(tickets_str)
        tickets = tickets_str.split()
        tickets = [int(x) for x in tickets]


        hasPostive = False
        maxNeg = tickets[0]
        for j in range(n):
            if  tickets[j] > 0 :
                hasPostive = True
                break
            else:
                if maxNeg < tickets[j]: maxNeg = tickets[j]


        if not hasPostive:
            print(maxNeg)
            return

        arr = []
        for k in range(n):
            if k is 0:
                if tickets[k] > 0:
                    arr.append([tickets[k], [tickets[k]]])
                else:
                    arr.append([0, []])
            elif k is 1:
                if tickets[k] > 0:
                    arr.append([tickets[k], [tickets[k]]])
                else:
                    arr.append([0, []])
            elif k is 2:
                if tickets[k] > 0:
                    tmp = [
                        tickets[k] + arr[k - 2][0],
                        arr[k - 2][1][:]
                    ]
                    tmp[1].append(tickets[k])

                    arr.append(tmp)
                else:
                    if arr[k-1][0] > arr[k-2][0]:
                        arr.append(arr[k - 1][:])
                    else:
                        arr.append(arr[k - 2][:])
            else:
                if tickets[k] > 0:
                    m1 = tickets[k] + arr[k - 2][0]
                    m2 = tickets[k] + arr[k - 3][0]

                    if m1 > m2:
                        tmp = [
                            tickets[k] + arr[k - 2][0],
                            arr[k - 2][1][:]
                        ]
                    else:
                        tmp = [
                            tickets[k] + arr[k - 3][0],
                            arr[k - 3][1][:]
                        ]

                    tmp[1].append(tickets[k])
                    arr.append(tmp)
                else:
                    if arr[k-1][0] > arr[k-2][0]:
                        arr.append(arr[k-1][:])
                    else:
                        arr.append(arr[k - 2][:])


        maxItem = arr[0]
        for item in arr:
            if item[0] > maxItem[0]:
                maxItem = item

        # print(maxItem)
        maxItem[1].reverse()
        op = "".join([str(x) for x in maxItem[1]])
        print(op)


main()
