"""
   Today i Learned Varible,Data Type,type Casting ,Vaible Scope
   Today interting concept is Variable scope 
   varible scope means how we access the varible that scope follow some Rules
    L --> E --> G --> B
    L = Local,E=Encoding,G= Global,b= Build In

"""

discount=10   #global  varible

def total():
    item_price =500   # Local varibable
    def offer():
        final_price = item_price - discount   #Enclosnig varible 
        print(final_price)
    offer()
total()
print(__file__)  # BuildIn varible




""""
    "The input() function is used to receive data from the user during program execution. 
    By default, it returns the entered value as a string, so we use type casting when we need 
    another data type.

    Hardcoding means directly assigning fixed values in the source code. To make programs more 
    flexible, we can accept input from users or use configuration files, 
    command-line arguments, or environment variables, depending on the application.

    For automated or scheduled applications, we generally avoid interactive
     input because the program needs to run without waiting for a user."
"""

# for schduler

import sys
                                #index 0               index=1
report_date = sys.argv[1]  # .\python\Input_Var_con.py  Riyas
print("Generating report for:", report_date)

full_name = sys.argv[1]
email = full_name.lower().replace(" ","_")+"@company.com"

print(full_name)
print(email)


#to run this   python .\python\Input_Var_con.py Riyas

#If we dont know how many value gonna give by user 
#we can write  full_name= " ".join(sys.argv[1:])
