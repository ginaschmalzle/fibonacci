#!/usr/bin/python

#find fibonocci number of the 10th element
start=[0,1,1] # Fn(0), Fn(1), Fn(2)
n =  10
def get_fibo(n, start):
	i = 3
	fn1=start[1]
	fn2=start[2]
	while ( i <= n):
		fn = fn1 + fn2 
		fn1 = fn2
		fn2 = fn
		i = i+1
	return fn  
	
print  get_fibo(n, start)
