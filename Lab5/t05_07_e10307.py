def is_poss_place(amount, places, x):
    c = 1
    prev_place = places[0]
    for i in places:
        if i - prev_place >= x:
            c += 1
            prev_place = i
    
    return c >= amount

def bin_search(amount, places):
	l = 0
	r = places[-1] - places[0] + 1
	while r - l > 1:
		m = l + (r - l) // 2
		if is_poss_place(amount, places, m):
			l = m
		else: r = m
		
	return l


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    places = list()
    for i in range(m):
        a, b = list(map(int, input().split()))
        for j in range (a, b + 1):
            places.append(j)
    
    d = bin_search(n, places)
    print(d)
