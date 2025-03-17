class Employee:
    def __init__(self,name,nationality,skill,gender):
        self.name=name
        self.nationality=nationality
        self.skill=skill
        self.gender=gender

    def introduction(self):
        return f"welcome {self.name}, your skills as a {self.skill}, would be most appreciated"
    def __str__(self):
        return f"This is {self.name},{self.gender} is very good at job of {self.skill}"
    def occupation_at_country(self):
        print(f"{self.gender} works as a {self.nationality}")
John=Employee("John","Kenyan","Data analyst","He")
print(John.name)
print(John.skill)
print(John.introduction())
print(John)
John.occupation_at_country()
class Manager(Employee):
    def __init__(self,name,nationality,skill,gender,department):
        super().__init__(name,nationality,skill,gender)# the parent class
        self.department=department# new parameter
    def __str__(self):
        return f"{self.name} will be in the role of {self.skill}"
Katie=Manager("Katie","Scotish","Leadership","She"
              ,"IT")
Katie_description=(f"{Katie.gender} is a {Katie.nationality} working in the {Katie.skill} "
                   f"in the {Katie.department} department")
print(Katie_description)
check_for_instance=isinstance(Katie,Manager)# to check if the object(former) for the class(latter)
print(check_for_instance)
check_for_subclass=issubclass(Manager,Employee)# check if the former is a subclass of the latter
print(check_for_subclass)
print(Katie)
