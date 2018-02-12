count = 1 #count for friend number
nameage = {} #dictionary

while (count<=5):	
	name = input("Enter the name of friend " + str(count) + ": ") #input of name
	age = input("Enter the age of friend " + str(count) + ": ") #input of age
	nameage[name] = age #add to dictionary
	count = count + 1 #changing the count

print("The contents of the database is: " + str(nameage)) #display the dictionary
