#!/usr/bin/env python3

file_name = input("Enter a file name or path to read: ")
f = open(file_name, 'r')
i = 1
line = f.readline()
while line:
	line = f.readline()
	print(line, end="")
	if i%1000 == 0:
		op = input("Read more? [n]:")
		if op == 'n':
			print("Exiting.")
			break
	i=i+1