#Ctaching exceptions
try:
    file = open("a_file.txt")
    d = {"key" : "value", "non existent key" : "new value"}
    print (d["non existent key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Opened file") 
except KeyError as error_message:
    print (f"The key {error_message} does not exist")
else: #do something if there are no exceptions
    content = file.read()
    print (content)
finally: #do something regardles if theres an error or not
    file.close()
    print ("File closed")
    # raise KeyError