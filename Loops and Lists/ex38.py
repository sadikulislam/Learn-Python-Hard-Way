ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")

list = ten_things.split(' ')
print(list)

new_list = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(list) != 10:
    item = new_list.pop()
    print("Adding ", item)
    list.append(item)
    print(f"There are {len(list)} items now.")

print("There we go: ", list)

print("Let's do some things with list.")
print(list[1])
print(list[-1])
print(list.pop())
print(' '.join(list)) 
print('#'.join(list[3:5]))