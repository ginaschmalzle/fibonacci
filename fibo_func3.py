#!/usr/bin/python
import time
start_time = time.time()
#find fibonocci number of the 10th element
start={'Number': 30, 'Fn0':0, 'Fn1':1,'Fn2':1} # Fn(0), Fn(1), Fn(2)
def get_fibo(start):
	if (start['Number'] == 0):
		return start['Fn0']
	elif (start['Number'] == 1):
		return start['Fn1']
	else:
		fn1 = start['Fn0']+start['Fn1']
		fn2 = start['Fn2']+start['Fn2']
		for i in range(3, start['Number']):
			fn = reduce(lambda a,x: a+x, [fn1,fn2])
			fn1 = fn2
			fn2 = fn
		return fn  
	
print  get_fibo(start)
print time.time() - start_time, "seconds"
