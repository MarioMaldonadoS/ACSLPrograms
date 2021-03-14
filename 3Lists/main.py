# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    i1 = input()
    i2 = input()
    i3 = input()

    #print(i3)
    l1 = i1.split()
    l2 = i2.split()
    l3 = i3.split()

    sum = 0
    lists = [l1, l2, l3]

    lists = sorted(lists, key=len)

    len1 = len(lists[0])
    len2 = len(lists[1])
    len3 = len(lists[2])
    r = max(len1, len2, len3)

    for i in range(r):
        if i == len1:
            lists.pop(0)

        if i == len2 and i < len3:
            sum += int(l3[i])
            continue

        sum += compare(lists,i)
    print(sum)

def compare(ls,i):
    if len(ls) == 3:
        return max(int(ls[0][i]), int(ls[1][i]), int(ls[2][i]))
    else:
        return max(int(ls[0][i]), int(ls[1][i]))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
