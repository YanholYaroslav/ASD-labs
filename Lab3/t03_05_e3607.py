import sys

def find_tall(n, dlg_list, a, b):
    c = 0
    for i in dlg_list:
        if a <= i and i <= b: c += 1
    return c


while True:
    try:
        n = int(input())
        inp = input().split(" ")
        dlg = [int(num) for num in inp]
        a, b = input().split(" ")
        a = int(a); b = int(b)
        print(find_tall(n, dlg, a, b))
    except EOFError:
        sys.exit(0)
