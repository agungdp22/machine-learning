#!/usr/bin/env python

from machineLearning import LVQ
import numpy as np

data = np.loadtxt("data.txt", usecols=[0,1,2,3,4])

lvq = LVQ(data)
lvq.learning()
lvq.printBobot()

tes = []
print "Masukkan data tes:"
for i in range(4):
	inp = int(input())
	tes.append(inp)

lvq.prediksi(tes)