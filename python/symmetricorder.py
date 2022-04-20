n = int(input())
j = 1
while n>0:
	inorder = []
	reverseord = []
	for i in range(n):
		newVal = input()
		if i%2==0: inorder.append(newVal)
		else:      reverseord.append(newVal)
	reverseord.reverse()
	inorder+=reverseord

	print(f"SET {j}")
	for x in inorder:
		print(x)

	j+=1
	n = int(input())
