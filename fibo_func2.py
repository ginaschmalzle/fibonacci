#!/usr/bin/python

#find fibonocci number of the 10th element
start={'Number': 10, 'Fn0':0, 'Fn1':1,'Fn2':1} # Fn(0), Fn(1), Fn(2)
def get_fibo(start):
	fn1 = start['Fn0']+start['Fn1']
	fn2 = start['Fn2']+start['Fn2']
	for i in range(3, start['Number']):
		fn = fn1 + fn2 
		fn1 = fn2
		fn2 = fn
		i = i+1
	return fn  
	
print  get_fibo(start)
