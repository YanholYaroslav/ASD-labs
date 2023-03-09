def func(x):
	return x*x*x + x + 1
	
def bin_min_search(l, r, c):
	while True:
		m = l + (r - l) / 2
		if func(m) > c:
			r = m
		else: l = m
		if abs(l - r) < 1e-6: break
		
	return r
	
C = 5
print(bin_min_search(0, 10, C))