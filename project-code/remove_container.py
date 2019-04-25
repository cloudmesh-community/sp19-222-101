import os


file = open("dockerContainers.txt", "r")
lines = file.read().split('\n')
line = lines[1].split(' ')

name = line[len(line)-1]
command = "docker rm " + name
os.system(command)