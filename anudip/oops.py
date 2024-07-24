# OOPS Concepts
# Class Creation
class student:
    print("-----------------------------------------------------CLASS CREATED-------------------------------------------------------")
    Name="Shubham"
    age=0
    def bgmi(self):
        print(self.Name,"plays daily")
        self.KD()
    def KD(self):
        print("My KD is more than 3")
# Object Instanciation
print("-----------------------------------------------------OBJECT INSTANCIATION-------------------------------------- -------------")
obj=student()
obj.bgmi()

#INHERITANCE
print("-----------------------------------------------------INHERITANCE-----------------------------------------------------------------")
class A:
    def show(self):
        print("This is show method")
class B(A):
    def demo(self):
        print("Demo method")
class C(A):
    pass
class D(B,C):
    pass
obj=C()
obj.show()
#obj.demo() it show error

# POLYMORPHISM
print("--------------------------------------------------------POLYMORPHISM-------------------------------------------------------------")

def sum(a=0,b=0,c=0):
    print(a+b+c)
sum(10,20,30)
print("-----------------------------------------------Polymorphism using default values---------------------------------------------")

sum(10)

print("-----------------------------------------------------Method overriding-------------------------------------------------------")


'''Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class. In inheritance, the child class inherits the methods from the parent class. However, it is possible to modify a method in a child class that it has inherited from the parent class. This is particularly useful in cases where the method inherited from the parent class doesn't quite fit the child class. In such cases, we re-implement the method in the child class. This process of re-implementing a method in the child class is known as Method Overriding.'''
class Bird:
    def intro(self):
        print("There are many types of birds.")
    def fly(self):
        print("Almost all birds can fly but some cannot.")
class sparrow(Bird):
    def fly(self):
        print("I can fly.")
class ostrich(Bird):
    def fly(self):
        print("I can't fly.")
obj=sparrow()
obj.fly()
obj1=ostrich()
obj1.fly()

print("-----------------------------------------------------Encapsulation-----------------------------------------------------------")

# __is used for private member declaration.
# _is used for protected member declaration.
class A:
    __name="abc"
class B(A):
    def show(self):
        print("This is show method",self.name)
obj=B()
obj.show()
