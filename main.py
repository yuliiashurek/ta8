import random
import string
import time

from adress import adress
from hashtable import HashTableBT

start = time.time()
table = HashTableBT()

i = 0
while i < 100:
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(45))

    i = i + 1
    test = adress(rand_string, rand_string, "24")
    table.insert(test, i)
    table.contain(test)

end = time.time()
print("Table Insertion ", end - start)

# kyivKhreschatyk = adress("Kyiv", "Khreshchatyk", "12")
# kyivVolodymyrska = adress("Kyiv", "Volodymyrska", "24")
# kyivAmur = adress("Kyiv", "Amur", "32")
# table.insert(kyivKhreschatyk, 1)
# table.insert(kyivVolodymyrska, 3)
# table.insert(kyivAmur, 2)
# print("Does table contain Kyiv, Khreshchatyk 12?", table.contain(kyivKhreschatyk))
# print("Does table contain Kyiv, Volodymyrska 24?", table.contain(kyivVolodymyrska))
# print("Does table contain Kyiv, Amur 32?", table.contain(kyivAmur))
