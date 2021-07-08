import os
import string
import numpy
from os import listdir
from os.path import isfile, join


#paths of answer files and the predicted files
paths = ['/home/sakib/Desktop/Research/IMS/SE2/', '/home/sakib/Desktop/Research/IMS/SE3/', '/home/sakib/Desktop/Research/IMS/SE7/', '/home/sakib/Desktop/Research/IMS/SE13/', '/home/sakib/Desktop/Research/IMS/SE15/'] 

answer_files = ['/home/sakib/Desktop/Research/IMS/Evaluation/answer_SE2.txt', '/home/sakib/Desktop/Research/IMS/Evaluation/answer_SE3.txt', '/home/sakib/Desktop/Research/IMS/Evaluation/answer_SE7.txt', '/home/sakib/Desktop/Research/IMS/Evaluation/answer_SE13.txt', '/home/sakib/Desktop/Research/IMS/Evaluation/answer_SE15.txt']
pred_files = ['/home/sakib/Desktop/Research/IMS/Evaluation/pred_SE2.txt', '/home/sakib/Desktop/Research/IMS/Evaluation/pred_SE3.txt', '/home/sakib/Desktop/Research/IMS/Evaluation/pred_SE7.txt', '/home/sakib/Desktop/Research/IMS/Evaluation/pred_SE13.txt', '/home/sakib/Desktop/Research/IMS/Evaluation/pred_SE15.txt']
#onlyfiles = [f for f in listdir(paths[0]) if isfile(join(paths[0], f))]

#o = paths[0]+onlyfiles[10]


#concatenating the predicted files to the specific answer files
#for i in range(len(paths)):
#	filepaths = [f for f in listdir(paths[i]) if isfile(join(paths[i], f))]
#	
#	for j in range(len(filepaths)):
#		cfile = paths[i]+filepaths[j]
#		x = open(cfile, "r")
#		a = open(answer_files[i], "a+")
#		a.write(x.read())
#		a.close()
#		x.close()

#removing the first column of the answer files

#for k in range(len(answer_files)):
#	x = open(answer_files[k], "r")
#	lines = x.readlines()
#	x.close()
#
#	for line in lines:
#		x = open(pred_files[k], "a+")
#		x.write(line.split(" ")[1]+" "+line.split(" ")[2])
#		x.close()


#sorting the prediction files based on the first columns

#for k in range(len(pred_files)):
#	f = open(pred_files[k], "r")
#	lines = f.readlines()
#	f.close()
#
#	f = open(pred_files[k], "w")
#
#	for line in sorted(lines, key=lambda line: line.split()[0]):
#		f.write(line)
#
#	f.close()


#creating the all dataset outputs

all = open("pred_ALL.txt", "w+")

for k in range(len(answer_files)):

	f = open(answer_files[k],"r")
	lines = f.readlines()
	modified_lines = []
	for i in lines:
		line = i.split()[0]+"."+i.split()[1]+" "+i.split()[2]+"\n"
		modified_lines.append(line)

	for line in sorted(modified_lines, key=lambda line:line.split()[0]):
		all.write(line)
	f.close()

all.close()



















