# -*- coding: utf-8 -*-

"""Main module."""
import random
import math
import matplotlib.pyplot as plt
import argparse
#constant define
Kb = 1#constant
m = 10#mass
wall_size = 5.0

#command line input
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--initial_position", help="initial position")
parser.add_argument("-v", "--initial_velosity", help="initial velosity")
parser.add_argument("-T", "--temperature", help="temperature")
parser.add_argument("-e", "--damping_coefficient", help="damping coefficient")
parser.add_argument("-d", "--time_step", help="time step")
parser.add_argument("-a", "--total_time", help="total time")
args = parser.parse_args()
ini_position = float(args.initial_position)
vel = float(args.initial_velosity)
T = float(args.temperature)
e = float(args.damping_coefficient)
del_t = float(args.time_step)
total_t = float(args.total_time)

#Langevin Equation and Euler Intergration
sigma = math.sqrt(2*T*e*Kb)
epsilon = []
nt = int(total_t/del_t)

#function move
def move():
	'''This function represents a complete movement of a particle, start from position 0 and velosity 0, stop by 
	it hits either wall. There is Euler Intergration inside this function'''
	v = [vel]
	x = [ini_position]
	for i in range(1,nt):
		epsilon.append(random.gauss(0,sigma))#epsilon changes in each movement
		v.append(v[-1] + (epsilon[-1] - e*v[-1])*del_t/m)
		x.append(x[-1] + v[-1]*del_t) #v[-1]here is not the same as v[-1] above
		if x[-1] >= wall_size:
			x[-1] = wall_size
			break
		if x[-1] <= 0:
			x[-1] = 0.0
			break
	t = int(len(x)*del_t)
	return v,x,t

#run function would call move() for 100 nice runs and return an array which make the histogram
def run():
	'''This function is used for the histogram, it will call move() function many times until get 
	enough data for the histogram'''
	v = []
	x = []
	his_t = []
	while len(his_t) < 100:
		[v,x,t] = move()
		if x[1] != 0.0 and x[-1] ==wall_size:
			his_t.append(t)
	return his_t,x

def PlotAndOutput():
	''' This function aims at do the final Output and plot things'''
	[t0,x0] = run()
	plt.figure(1)
	plt.hist(t0)
	plt.title('Histogram')
	plt.xlabel('time')
	plt.ylabel('frequency')
	plt.savefig('histogram.png')
	while 1:
		[v,x1,t1] = move()
		if x1[1] != 0.0 and x1[-1] == wall_size:
			print("final position: ")
			print(x1[-2])
			print("final velocity: ")
			print(v[-2])
			print("Please view the output file and png in my directory")
			plt.figure(2)
			plt.plot(x1)
			plt.title('Trajectory')
			plt.xlabel('time')
			plt.ylabel('position')
			plt.savefig('trajectory.png')
			fo = open("OutPut.txt", "w")
			fo.write("index , time , position , velocity\n")
			for i in range(len(x1)):
				time = i*del_t
				line = str(i) +' , '+str(time)+' , '+str(x1[i])+' , '+str(v[i])+'\n'
				fo.write(line)
			break
PlotAndOutput()
