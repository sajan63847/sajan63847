question_list= [
	"How many continents are there?",	
	"What is the capital of India?",	
	"NG mei kaun se course padhaya jaata hai?"
]
answer_list= [
	["Four", "Nine", "Seven", "Eight"],
	["Chandigarh", "Bhopal", "Chennai", "Delhi"],
	["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution_list=["Seven","Delhi","Software Engineering"]
solution=["3","4","1"]
wrong_list=["Nine","Chandigarh","Counseling"]
life_line=["5050"]
i=0
l=0
while i<len(question_list):
	print(question_list[i])
	j=0
	while j<len(answer_list[i]):
		print(j+1,answer_list[i][j])
		j=j+1
	s=input("enter your choice =")
	if s=="5050":
		while l<len(life_line):
			print("a",solution_list[i])
			print("b",wrong_list[i])
			s=input("enter your choice =")
			l=l+1
	if s in solution[i]:
		print("congrutulation you give right answer")
	else:
		print("oops you are loose")
		break
	print()
	i=i+1