class Employee:
    hike = 1.2
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if  isinstance(name,str) and len(name) > 0  :
            self._name = name
        else:
            raise ValueError("Name must be of type string and also cannot be empty")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        if isinstance(age, int) and age > 0 :
            self._age = age
        else:
            raise ValueError('Age must be of type integer and must be higher than zero')

    @age.deleter
    def age(self):
        self._age = None

    def __str__(self):
        return "Name = {}, age = {}, salary = {}".format(self.name,self.age,self.salary)

    def __repr__(self):
        return "Employee(Name = {}, age = {}, salary = {})".format(self.name,self.age,self.salary)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if (isinstance(salary,int) or isinstance(salary,float)) and salary > 0:
            self._salary = salary
        else:
            raise ValueError("Salary must be an integer")

    def raise_salary(self):
        self.salary = self.salary * self.hike

class Developer(Employee):
    hike = 5.2
    def __init__(self,name, age, salary, prog_lang):
        super().__init__(name, age, salary)
        self.prog_lang = prog_lang

    def add_prog_lang(self, prog_lang):
        if prog_lang.strip() not in self.prog_lang:
            self.prog_lang.append(prog_lang.strip())

p = Developer("gurudatt",37,1000.0,["python","java"])
print(p.age)
print(p.raise_salary())
p.add_prog_lang("  c  ")
print(p.prog_lang)
print(repr(p))
