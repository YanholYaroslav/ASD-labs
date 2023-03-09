def is_poss_place(amount, places, x):
    c = 1
    prev_place = places[0]
    for i in places:
        if i - prev_place >= x:
            c += 1
            prev_place = i
    return c >= amount


def bin_search(amount, places):
    left, right = 0, places[-1] - places[0] + 1
    while right - left > 1:
        mid = (left + right) // 2
        if is_poss_place(amount, places, mid):
            left = mid
        else:
            right = mid
    return left


if __name__ == "__main__":
    n, m = map(int, input().split())
    places = []
    for i in range(m):
        a, b = map(int, input().split())
        places.append(a)
        places.append(b)
    places.sort()
    res = bin_search(n, places)
    print(res)
