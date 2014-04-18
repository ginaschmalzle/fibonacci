#!/usr/bin/python

import time
import matplotlib.pyplot as plt

rec=[]
tm=[]
a=[]
reci=[]
tmi=[]
ai=[]
def get_fibo_rec(start):
	if (start['Number'] == 0):
		return 0
	elif (start['Number'] == 1):
		return 1
	elif (start['Number'] > 1):
		return (get_fibo_rec({'Number': start['Number']-1}) + get_fibo_rec({'Number': start['Number']-2}))
	else:	
		return -1 	

def get_fibo_it(start):
        if (start['Number'] == 0):
                return 0
        elif (start['Number'] == 1):
                return 1
        elif (start['Number'] >1 ):
		fn = 0
                fn1 = 1
                fn2 = 2
                for i in range(3, start['Number']):
                        fn = reduce(lambda a,x: a+x, [fn1,fn2])
                        fn1 = fn2
                        fn2 = fn
                return fn
	else: 
		return -1

def plotit(a,rec,tm,color):
	plt.subplot(2,1,1)
	plt.plot (tm,a,color, linewidth=10)
	plt.ylabel('Sequence Number')
	plt.subplot(2,1,2)
        plt.plot (tm,rec,color, linewidth=10)
        plt.xlabel('Time(seconds)')
	plt.ylabel('Fibonacci Value')

def run_range(begin,end):
	for n in range (begin,end):
		#start={'Number': n} 
		start_time = time.time()
		#find fibonocci number of the 10th element
		#print  get_fibo_rec(start),  time.time() - start_time, "seconds"
		rec.append(n)
		tm.append([time.time() - start_time])
		a.append([n])
	print "Done Recursive"	
	plotit(a,rec,tm,'r')
	for n in range (begin,end):
		start={'Number': n} 
                start_time = time.time()
                #find fibonocci number of the 10th element
                print  get_fibo_it(start),  time.time() - start_time, "seconds"
                reci.append([get_fibo_it(start)])
                tmi.append([time.time() - start_time])
                ai.append([n])
	print "Done Iterative"	
	plotit(ai,reci,tmi, 'b')

run_range(0,12)
plt.show()
