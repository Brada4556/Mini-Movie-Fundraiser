#functions go here


#Main code
want_instructions = input("Do you want to view instructions? ")
print(want_instructions)

if want_instructions == "yes":
    print("Instructions go here")
elif want_instructions == "no":
    pass
else:
    print("please answer yes/no")