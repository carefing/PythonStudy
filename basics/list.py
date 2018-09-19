def main():
    # initialize
    list1 = [1, 3, 5, 7, 9]
    list2 = ['hello'] * 5
    # length of list
    print('length of list1:', len(list1))
    # access with index
    print('list1:', list1)
    print('list2:', list2)
    print('list1[1]:', list1[1])
    print('list1[3]:', list1[3])
    print('list1[-1]:', list1[-1])
    print('list1[-3]:', list1[-3])
    list1[2] = 100
    print(list1)
    # add element
    list1.append(200)
    list1.insert(1, 300)
    list1 += [1000, 2000]
    print(list1)
    # remove element
    list1.remove(3)
    if 1234 in list1:
        list1.remove(1234)
    del list1[0]
    print(list1)
    # clear list
    list1.clear()
    print(list1)

    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    print(fruits)
    for fruit in fruits:
        print(fruit.title(), end=' ')
    print()
    # slice
    fruits2 = fruits[1:4]
    print(fruits2)
    # fruits3 = fruits  # create a new reference, not copy the list
    fruits3 = fruits[:] # copy the list
    print(fruits3)
    # order
    fruits4 = sorted(fruits) # sorted and copy to fruits4, not change the order of fruits
    fruits5 = sorted(fruits, reverse=True)
    fruits6 = sorted(fruits, key=len)
    print(fruits4)
    print(fruits5)
    print(fruits6)

if __name__ == '__main__':
    main()