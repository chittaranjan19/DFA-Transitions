def formDFA(name):
	f = open(filename)
	alphabet = f.readline().strip().split() #Read only first line to get the alphabet
	n = len(alphabet)

	ttable = {}
	final = []
	s = 0 #Represents q0 in first iteration, q1 in second and so on, till the blank line is encountered.
	for line in f:
		if(line == '\n') :
			final = list(map(int,f.readline().strip().split())) #List of final states
		else:
			l = line.strip().split()
			for i in range(0,n):
				ttable[(s,alphabet[i])] = int(l[i])
			s+=1
	return [ttable,final]

def checkString(DFA,string):

	state = 0 #As per assumption in problem statement, initial state is q0

	for i in testString :
		#print('q',state,' with input ',i,end=' : ',sep='')
		state = DFA[0][(state,i)]
		#print('q',state,sep='')

	if state in DFA[1]:
		return True
	else :
		return False

filename = input("Enter the file name (with extension): ")
dfa = formDFA(filename)
testString = input("Enter test string : ")
if(checkString(dfa,testString)):
	print("Accepted")
else : 
	print("Rejected")
