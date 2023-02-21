class calculation():
    def __init__(self,x=0):
        self.x =x
        

    def __str__(self):
        return f"the answer is {self.x}"


    def __add__(self,other):
        a = self.x + other.x
        return calculation(a) 

    def __sub__(self,other):
        a = self.x - other.x
        return calculation(a)  

    def __mul__(self,other):
        a = self.x * other.x
        return calculation(a) 

    def __floordiv__(self,other):
        a = self.x * other.x

        return calculation(a) 


obj1 = calculation(int(input("enter the first number : ")))
obj2 = calculation(int(input("enter the second number : ")))
choose = input("enter the operation : ")

if choose == "+":
    print(obj1+obj2)

if choose == "-":
    print(obj1-obj2)

if choose == "x":
    print(obj1*obj2)

if choose == "/":
    print(obj1//obj2)    

