from functools import partial


#define the original function
def calculate_gst(price,tax_rate):
    return price*(1+tax_rate)

#create a partically appield function with GST FIXED
price_with_gst =partial(calculate_gst,tax_rate=0.18)


#Now using without passing TAX_RATE  again

print(calculate_gst(10000))
print(calculate_gst(5000))





