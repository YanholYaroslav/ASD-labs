from math import sin

def func(x):
	return sin(x) - x/3
	
def bin_search(l, r, c):
	while True:
		m = l + (r - l) / 2
		if func(m) < c:
			r = m
		else: l = m
		if abs(l - r) < 1e-6: break
		
	return r
	
C = 0
print(bin_search(1.6, 3.0, C))