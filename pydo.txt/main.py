# This is a rewritten verison of todo.txt in python. This is supposed to be a basic todo list generator
import os
import datetime
import re
# It can either be called PyDo, The Anti-ToDoList, or To-Don't

# comments are for why, not how. How should be self-evident
print("You are awesome. To use this software, enter a task like this: Badger +Actvity @Area !Now Today is %s" % (datetime.datetime.now()) ) 

start = input("do you wanna write you todo's today? y for yes and n for no. ")


if start == "y":

    time = datetime.datetime.today()
    
    #formatting with time and a newline
    todo = input("\n%s\n" % time)
    
    #got this from SO    
    plusregex = re.findall("[^\w\s]\w+", todo)
    
    print(plusregex)
    
    #prettifies the time
    strtime = str(time)
    superstrtime = "\t" + strtime 

    
    with open("todo.txt", "w") as todowrite:
        
        todowrite.write(todo + superstrtime)
        
        todowrite.write("\n\n%s" % plusregex)
    
        todowrite.close()
        
    userinput1 = input("Do you wanna see and deletes your prevouis todo? Say y for yes and n for no! ")

    if userinput1 == "y":
        
        with open("todo.txt", "r") as f:
            newf = f.readlines()

        #test to see if it is working now I'm gonna add the abilty to slect which one to delet
        delinput = str(input("Enter which text would you like to delete! "))
        
        with open("todo.txt", "w") as f:
            for deltodo in newf:
                if delinput in newf:
                    f.write(deltodo)


# does the same as the first one, but without writing to the file and just allows you to delete it TODO add print todos BEFORE del 
#TODO add abilty to save all todo list into a todo-backup.txt file. 
elif start == "n":
    userinput2 = input("Do you wanna see your rpevouis todo? Say y for yes and n for no! ")

    if userinput2 == "y":
                
        with open("todo.txt", "r") as f:
            newf = f.readlines()
            
        #test to see if it is working now I'm gonna add the abilty to slect which one to delet
        delinput = input("Enter which text would you like to delete! ")
        
        with open("todo.txt", "w") as f:
            for deltodo in newf:
                if delinput in newf:
                    f.write(deltodo)