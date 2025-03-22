
# Single Inheritance
# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating an object of Dog
d = Dog()
d.speak()  # Inherited from Animal
d.bark()   # Defined in Dog


# Multiple Inheritance

# Parent class 1
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Parent class 2
class Walker:
    def walk(self):
        print("Animal is walking")

# Child class inheriting from both Animal and Walker
class Dog(Animal, Walker):
    def bark(self):
        print("Dog barks")

# Creating an object of Dog
d = Dog()
d.speak()  # Inherited from Animal
d.walk()   # Inherited from Walker
d.bark()   # Defined in Dog



# Multilevel Inheritance
# Base class (Parent)
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Derived class (Child of Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Another derived class (Child of Dog)
class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

# Creating an object of Puppy
p = Puppy()
p.speak()  # Inherited from Animal
p.bark()   # Inherited from Dog
p.weep()   # Defined in Puppy


# Hybrid Inheritance

class Base:
    pass
class Derived1(Base):
    pass
class Derived2(Base):
    pass

class Derived3(Derived1,Derived2):
    pass


# Hierarchical Inheritance

class Base:
    pass
class D1(Base):
    pass

class D2(Base):
    pass

class D3(D1):
    pass



