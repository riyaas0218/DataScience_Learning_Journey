#type 1
####       TAKE ANOTHER FUNCTION AS A ARGUMENT


def gmail_Emil(username,domain='gmail.com'):
    return f"{username}@{domain}"

def Ymail_email(username,domain='ymail.com'):
    return f"{username}@{domain}"

def hotmail_emil(username,domain="hotmail.com"):
    return f"{username}@{domain}"


def build_Mail(username,email_func):
    return email_func(username)

print(build_Mail("Riyas",gmail_Emil))
print(build_Mail("Magu",Ymail_email))
print(build_Mail("Bala",hotmail_emil))

#type ---- 2
#Return ANOTHER FUNCTION AS A RESULT


def email_builder(domain):
    def build_emil(username):
        return f"{username}@{domain}"

    return build_emil


gmail = email_builder("gmail.com")
ymail = email_builder("Ymail.com")


print(gmail("Riyas0216"))
print(ymail("Riyas0218"))


#lambda functions   calll anonymys funtions 

#map --->iterate take one by one perform the condition
#filder ---->take one by one but return only elements are if condition statisfy
#reduce ---->whatever and howmany element in the list but result only one element like cumulative

from functions import reduce
price=[1001,200,23,435,2455,222]

expensive=list(filter(lambda x : x>1000 , price))

total=reduce(lambda a,b : a+b ,expensive)
print(total)