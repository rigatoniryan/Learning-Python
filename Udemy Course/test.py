def foo():
    print("yeaaa")
    print("boii")


test = "wowie"
print(type(test))
foo()

print("This is a string {}".format("INSERTED"))
print("the {2} {1} {0}".format("fox", "brown", "quick"))
print("the {q} {b} {f}".format(f="fox", b="brown", q="quick"))

boi = None
boi = 3
boi += -3
if boi:
    print(boi)
elif boi < 3:
    print("boiiiiii")

list = [1, 2, 3]
for x in list:
    print(x)
