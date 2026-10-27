my_tuple=("Bhavya",22,"Pink")
print(my_tuple)
my_tuple=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
print(my_tuple[5])
my_tuple1=(1,3,5)
my_tuple2=(2,4,6)
result=my_tuple1+my_tuple2
print(result)
dimensions=(10,5)
length,width=dimensions
area=length*width
print(area)
my_tuple=(10,20,30,40,50)
element=30
if element in my_tuple:
    print("element exixts")
else:
    print("element does not exists")
items=[("Apple",99),("Banana",99),("Milk",49)]
print(f"Item\tPrice")
print("-"*20)
total=0
for i,j in items:
    print(f"{i}\t{j}")
    total +=j
print("-"*20)
print(f"Total\t{total}")