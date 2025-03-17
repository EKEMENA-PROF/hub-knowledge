cube=lambda x:x*x*x
print(cube(4))
numbers=[1,2,3,4,9,10,20,12]
square=list(map(lambda n:n**2,numbers))
print(square)
test=int(input("Let's test your theory"))
square_of_theory=lambda subj:subj**2
print(square_of_theory(test))
even_numbers=list(filter(lambda n1:n1%2==0,numbers))
print(even_numbers)