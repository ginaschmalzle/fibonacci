#!/Users/ginaschmalzle/Documents/hackerschool/crackcode/d3plugin/v_env/bin/python
import matplotlib.pyplot as plt
import numpy as np
import mpld3
from mpld3 import plugins
import time

fib_r=[]
tm=[]
a=[]
fib_it=[]
tmi=[]
ai=[]
memo = {}
def get_fibo_rec(n):
	if (n == 0):
		return 0
	elif (n == 1):
		return 1
	elif (n > 1):
		return (get_fibo_rec(n-1) + get_fibo_rec(n-2))
	else:	
		return -1 	


def get_fibo_mem(n):
        if (n == 0):
                return 0
        elif (n == 1):
                return 1
        elif (n > 1):
		if n not in memo:
			memo[n] = (get_fibo_mem(n-1) + get_fibo_mem(n-2))
                return memo[n]
        else:
                return -1

def get_fibo_it(n):
        if (n == 0):
                return 0
        elif (n == 1):
                return 1
        elif (n >1 ):
		fn = 0
                fn1 = 1
                fn2 = 2
                for i in range(3, n):
                        fn = fn1+fn2
                        fn1 = fn2
                        fn2 = fn
                return fn
	else: 
		return -1

def plotit(a,rec,tm,color):
	plt.subplot(2,1,1)
	plt.plot (tm,a,color, linewidth=10)
	plt.ylabel('n')
	plt.subplot(2,1,2)
        plt.plot (tm,rec,color, linewidth=10)
        plt.xlabel('Time(seconds)')
	plt.ylabel('Fibonacci Value',labelpad=25)


def run_range(begin,end):
	for n in range (begin,end):
		start_time = time.time()   #Start the timer!
		answer = get_fibo_mem(n)   #Run the Recursive Case that has been memoized
		diff_time = time.time() - start_time  #Stop timer and Calculate the difference 
		fib_r.append(answer)
		tm.append(diff_time)
		a.append(n)
	plotit(a,fib_r,tm,'r')
	for n in range (begin,end):
                start_time = time.time()  #Start the timer!
                answer =  get_fibo_it(n)   # Run the Iterative Case
		diff_time = time.time() - start_time  # Stop timer and Calculate the difference
                fib_it.append(answer)
                tmi.append(diff_time)
                ai.append(n)
	plotit(ai,fib_it,tmi, 'b')

run_range(0,200)
mpld3.show()
