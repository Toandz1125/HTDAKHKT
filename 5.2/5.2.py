## Bai tap list comprehensions
odds =[x for x in range(1, 21) if x % 2 != 0]
print(odds)

hellos = ["Hello" for _ in range(5)]
print(hellos)


## Bai tap generator expressions
gen = (x for x in range(16) if x % 3 == 0)
print(list(gen))

gen = (x for x in range(16) if x % 3 == 0)
first = next(gen)
print(first)
second = next(gen)
print(second)


## Bai tap tong hop
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Test Plot")
plt.show()

divisible_by_3_and_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(divisible_by_3_and_5)

gen = (x for x in range(2, 101) 
       if all(x % i != 0 for i in range(2, int(x**0.5) + 1)))

for _ in range(25):
    print(next(gen))