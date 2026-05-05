# user_input = input("Enter Register number: ")
# print(user_input)
# print("Type of input:", type(user_input))

# if user_input.isdigit():
#     print("you enterd a number.")
# else:
#     print("You entered a string.")    

# print("Characters in your input:")
# idx = 0
# for char in user_input:
#     idx = idx + 1
#     print( idx,")",char)

# for i in range(5):
#     print(i)
# print("==========================")

# for i in range(1, 10 , 2): 
#       print(i)

# for idx in range(1, 10, 1):
#     product = 5 * idx
#     print("5 x", idx, "=", product)
        
## nested loop 
# for i in range(3):
#     for j in range(3):
#         print(i,":",j)
#     print("***********")    

# count = 0
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             count += 1
#             print(i, ":", j, ";", k)
#             count += 1
#         print("***********")
#         count = count
# print("Total iterations =", count)


a = 10
print(a, "is of type:", type(a))
b = 3.14
print(b, "is of type:", type(b))
c = "Hello, World!"
print(c, "is of type:", type(c))
d = True
print(d, "is of type:", type(d))
e = [1, 2, 3, 4]
print(e, "is of type:", type(e))
f = (1, 2, 3)
print(f, "is of type:", type(f))
g = {1, 2, 3}
print(g, "is of type:", type(g))
h = {"name": "Alice", "age": 25}
print(h, "is of type:", type(h))