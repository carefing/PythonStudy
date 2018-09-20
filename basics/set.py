def main():
    set1 = {1, 2, 3, 4, 3, 3, 2}
    print(set1)
    print('length:', len(set1))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    print(set1)
    print(set2)
    set2.discard(5)
    if 4 in set2:
        set2.remove(4)
    print('set 2:', set2)
    for element in set2:
        print(element ** 2, end=' ')
    print()
    
    # set operation: two methods
    # intersection, union, difference
    print(set1.pop())
    print('set 1:', set1)
    set3 = set((1, 2, 3, 3, 2, 1))  # tuple to set
    print('set 3:', set3)
    # print(set1.intersection(set3))
    print(set1 & set3)
    # print(set1.union(set3))
    print(set1 | set3)
    # print(set1.difference(set3))
    print(set1 - set3)
    # print(set1.symmetric_difference(set3))
    print(set1 ^ set3)
    # subset and superset
    #print(set3.issubset(set2))
    print(set3 <= set2)
    #print(set2.issuperset(set1))
    print(set2 >= set1)

if __name__ == '__main__':
    main()