def myfunc(e):
    return len(e)


mylist = [4, 3, 5, 7, 3, 2]
strlist = ['BMW', 'Tesla', 'GM']
mylist.sort()
print('#1', mylist)
mylist.sort(reverse=True)
print('#2', mylist)
print('#3', mylist.count(2))
strlist.sort(key=myfunc)
print('#4', strlist)