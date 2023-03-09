from math import sqrt

def func(x):
	return x*x + sqrt(x)
	
def bin_search(l,r, c):
	while True:
		m = l + (r - l) / 2
		if func(m) > c:
			r = m
		else: l = m
		if abs(l - r) < 1e-6: break
		
	return r
	
C = float(input())
print(bin_search(1.0, 1e10, C))