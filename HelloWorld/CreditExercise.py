price= 1000000
is_credit_good = False

if is_credit_good:
    msg=f"The down payment is ${price*0.1}"

else:
    msg = f"The down payment is ${abs(price * 0.2)}"

print(msg)