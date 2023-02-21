data = [{"id":1,"name":"rajesh"},
        {"id":2,"name":"rahul"},
        {"id":3, "name":"sruthi"}]

person_id = int(input("enter the person id : "))

if person_id == 1:
    x = data[0].get("name")
    print(f"The name is {x}")

elif person_id == 2:
    x = data[1].get("name")
    print(f"The name is {x}")

elif person_id == 3:
    x = data[2].get("name")
    print(f"The name is {x}")

else:
    print("no data found")              