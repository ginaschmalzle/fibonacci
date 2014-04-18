#!/usr/bin/python

import time
start_time = time.time()

#find fibonocci number of the 10th element
start={'Number': 30} # Fn(0), Fn(1), Fn(2)
def get_fibo(start):
	if (start['Number'] == 0):
		return 0
	elif (start['Number'] == 1):
		return 1
	elif (start['Number'] > 1):
		return (get_fibo({'Number': start['Number']-1}) + get_fibo({'Number': start['Number']-2}))
	else:	
		return -1 	
print  get_fibo(start)
print time.time() - start_time, "seconds"
