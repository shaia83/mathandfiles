print("Hello there, can you help me with something?")
print("Let's assume you said yes.")

print("Can you write two numbers?")

print("first number", end=' ')
a = input()
a = int(a)
print("the type of a is % ", type(a))

print("second number", end=' ')
b = input()
b = int(b)
print("the type of b is % ", type(b))

print(f"your numbers are: {a} and {b}, correct?", end=' ')
answer = input()

print("good! Now let's have some fun with them!")

c = a + b
print("If we add them up we get:", c)
input("ok?")

d = a * b
print("If we multiply them, we get:", d)
input("ok?")

e = a / b
print("If we divide them, we get:", e)
input("ok?")

f = a - b
print("and if we subtract them, we get:", f)
input("ok?")

print("Now we will create a file and save all the answers there.")
target = open ("mynumbers.txt", 'w')

target.write(str (c))
target.write("\n")
target.write(str (d))
target.write("\n")
target.write(str (e))
target.write("\n")
target.write(str (f))
target.write("\n")

print(f"Files are now saved in mynumbers.txt.")

target.close()
print("Thank you for playing along.")






