list1 = list(int(i) for i in input("Enter number in first element").split())
list2 = list(int(i) for i in input("Enter number in second element").split())
tuple1 = (1, 2, 3, 4, 5, 6, 7)
for i in tuple1:
    print(i)
thisdictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdictionary.pop("model")
print(thisdictionary)
