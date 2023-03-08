def bin_search(arr, n, el):
    l = 0
    r = n - 1
    while l <= r:
        m = l + (r - l) // 2
        if el > arr[m]:
            l = m + 1
        elif el < arr[m]:
            r = m - 1
        else: return "YES"
    return "NO"


n = int(input())
col = list(map(int, input().split(" ")))
m = int(input())
inp = input().split(" ")

for i in range(m):
    try:
        mes = bin_search(col, n, int(inp[i]))
        print(mes)
    except:
        print("NO")