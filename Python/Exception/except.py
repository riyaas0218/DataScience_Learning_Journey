try:
    number_of_item = int(input("Enter a Number"))
    total_price=200*number_of_item
    average_price = total_price /number_of_item
    print("Average price is ",average_price)
except ArithmeticError:
    print("Divide number must be greatherthen 0")
except FileNotFoundError:
    print("File not found")
finally:
    print("logout")
