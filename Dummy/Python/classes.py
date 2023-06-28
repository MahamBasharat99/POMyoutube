class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person1("John", 36)

print(p1.name)
print(p1.age)


#####

class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def my_func(self):
      print('person name is {} person age is {}'.format(self.name,self.age))

p1 = Person2("John", 36)
p1.my_func()
p2= Person2("maham",16)
p2.age=13 #update
p2.my_func()


############1
class Person3:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person3("John", "Doe")
x.printname()
#2
class Student(Person3):
  pass
#3
x = Student("Mike", "Olsen")
x.printname()

#4
class Student(Person3):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("harry", "potter", 2019)
x.printname()

#5
class Student(Person3):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Bad Experience of", self.firstname, self.lastname, "to the session of", self.graduationyear)

y = Student("covid", "disease", 2019)
y.welcome()