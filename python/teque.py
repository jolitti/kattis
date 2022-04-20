from collections import deque

q1 = deque()
q2 = deque()

def areQueuesLevel():
	return 0<=len(q1)-len(q2)<=1

def levelQueues():
	while not areQueuesLevel():
		if len(q1)>len(q2):
			q2.appendleft(q1.pop())
		else:
			q1.append(q2.popleft())

def getInQueue(index):
	if index<len(q1):
		return q1[index]
	else:
		return q2[index-len(q1)]

n = int(input())

for i in range(n):
	command, arg = input().split()
	arg = int(arg)

	if command=="get":
		print(getInQueue(arg))
	elif command=="push_back":
		q2.append(arg)
		levelQueues()
	elif command=="push_front":
		q1.appendleft(arg)
		levelQueues()
	else:
		q1.append(arg)
		levelQueues()
