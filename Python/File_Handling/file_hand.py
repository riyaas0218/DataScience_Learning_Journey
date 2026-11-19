# file=open('demo.txt','w')
# file.write("this is my first file \n")
# file.write("Never give up you can do\n")
# file.close()

# file=open('demo.txt','r')
# content=file.read()
# print("the file contents are \n",content)
# file.close


# file=open('demo.txt','a')
# file.write("Adding new Line \n")
# file.close()
# 
# 
# with open('demo.txt','r') as file:
    # for i in file:
        # print(i.strip())


# feedback =input("Enter your feed back")
# with open('demo.text','a') as file:
    # file.write(feedback + "\n")
# 
# 
# print("Thanks for your feedback")
# 

#Read One File and Write another File

with open("demo.txt",'r') as read_file ,open("demo.text",'w') as write_file:
    for line in read_file:
        print(line.strip())
        write_file.write(line)
