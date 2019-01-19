#! /usr/bin/python3
import sys
import worker_funcs

# ensures there is a source argument
if len(sys.argv) != 2:
	print(f"usage: {sys.argv[0]} <src.dsl>")
	sys.exit(1)
	
print("A DSL for the Web.")

with open(sys.argv[1], "r") as source:
	for line in source:
		line = line.strip()
		if (not line) or (line[0] == "#"): #allows comments
			continue 
		parts = line.split()
		func = parts[0]
		args = parts[1:]
		for index, arg in enumerate(args):
			args[index] = arg.replace('"', '')
		print(args)
		getattr(worker_funcs, func)(args)

input("Press enter to exit.")
