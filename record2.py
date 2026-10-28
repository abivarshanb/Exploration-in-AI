def calculate_bill(units):
    bill=0

    if units<=100:
        bill=units*1.50
    elif units<=200:
        bill=100*1.5+(units-100)*2.5
    elif units<=500:
        bill=(100*1.5)+(100*2.5)+(units-200)*400
    else:
        bill=(100*1.5)+(100*2.5)+(300*4.00)+(units-500)*600
    return bill
n=int(input("Enter the number of customers"))
for i in range(1,n+1):
    print("\n Customer {i}")
    name=input("Enter the customer name :")
    units=float(input("enter the units consumed"))
    bill=calculate_bill(units)
    print("Customer Name :",name)
    print("Units :",units)
    print("Bill Amount : Rs",round(bill,2))
