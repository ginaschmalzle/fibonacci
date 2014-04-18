#!/usr/bin/python

#find fibonocci number of the 10th element
n =  10
i = 3

fn1 = 0
fn2 = 1
fn = fn1 +fn2

fn1 = fn2
fn2 = fn

while ( i <= n):
	fn = fn1 + fn2 
	fn1 = fn2
	fn2 = fn
	i = i+1
	print fn   
	
	
