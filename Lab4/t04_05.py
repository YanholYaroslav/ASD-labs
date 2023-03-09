def func(x):
	return x*x*x + 4*x*x + x - 6
	
def bin_search(l, r, c):
	while True:
		m = l + (r - l) / 2
		if func(m) > c:
			r = m
		else: l = m
		if abs(l - r) < 1e-9: break
		
	return r
	
C = 0
print(bin_search(0, 2, C))