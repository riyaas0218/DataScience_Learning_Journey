#today i learned about string and f string and string method

song="Shape OF YOu"
authour= "Riyas"

formatchange=f"{song.title()} is sing by {authour.title()}"
print(formatchange)

#split and stript funtions

message= " The Uber booking Id is : 23455 .please key it safe and secure"
booking_id = message.split(":")[1].split(".")[0].strip()
print(booking_id)

#now we are going to take one single particular word from that paragraph

pharagarph ="Hello Im Riyas from Sivaganga "

if "Hello" in pharagarph:
    print("yaah it here")

print(pharagarph.find("Riyas"))

#word  count

word_count  = len(message.split())
print(word_count)

