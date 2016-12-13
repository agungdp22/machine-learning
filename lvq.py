#!/usr/bin/env python

import numpy as np

data = np.loadtxt("data.txt", usecols=[0,1,2,3,4])
# print len(data)
datates = data[:,0:4]
# print datates
w1 = datates[0]
w2 = datates[1]
# print len(w1)
epochs = 10
alpha = 0.05
for i in range(epochs):
	for j in range(2,len(data)):
		# print "data ke-",j-1,datates[j]
		sum1 = 0
		sum2 = 0
		for k in range(len(w1)):
			sum1 = sum1+(datates[j][k]-w1[k])**2
			sum2 = sum2+(datates[j][k]-w2[k])**2
		sum1 = np.sqrt(sum1)
		sum2 = np.sqrt(sum2)
		for k in range(len(w1)):
			if sum1<=sum2:
				w1[k] = w1[k]+alpha*(datates[j][k]-w1[k])
			else:
				w2[k] = w2[k]+alpha*(datates[j][k]-w2[k])
	alpha = 0.1*alpha
print "Training selesai..."
print w1
print w2

while True:
	bobot1 = 0
	bobot2 = 0
	for i in range(len(w1)):
		print "data ke-",i,": ",
		ii = int(input())
		bobot1 = bobot1+(ii-w1[i])**2
		bobot2 = bobot2+(ii-w2[i])**2
	bobot1 = np.sqrt(bobot1)
	bobot2 = np.sqrt(bobot2)

	if bobot1<bobot2:
		print "masuk ke kelas 1"
	else:
		print "masuk ke kelas 2"
