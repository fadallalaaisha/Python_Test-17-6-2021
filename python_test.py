x = [100,110,120,130,140,150]
M=5
for M in x:
    M*=x
    print(M)

    

def divisible_by_three():
    n=range(1,20) 
    for x in n:
        if x%3==0:
            print("{} divisible by 3".format(x)) 
divisible_by_three()



def flatten_list():
    a = [[1,2],[3,4],[5,6]]
    print(x)
  


def smallest():
    lis=[2,4,5,6,1,7,8]
    lis.sort()
    return f"Smallest element is:", *lis[:4]
smallest()
    

def remove_duplicate():
    x = ['a','b','a','e','d','b','c','e','f','g','h']
    x.remove('h')
    return x
remove_duplicate()

def divisible_by_seven():
    z=range(100,200)
    for number in z:
        if number%7==0:
            print("{} is divisible by 7".format(number))
divisible_by_seven()


def greets():
    students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
    
    print("Hello {name},you were born in the year 2002 {age}")

greets()

class Rectangle():
    def __init__(self,width, length):
        self.width=width
        self.length=length

    def area(self,A):
        A=width*length 

    def perimeter(self, P):
        P= 2(length+width)

Rectangle()        
        



