
my_dictionary = {}
for x in range(1,16):
    x = {x:x**2}
    my_dictionary.update(x)
print(my_dictionary)
