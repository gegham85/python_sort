def sort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)

        return sort(less) + equal + sort(greater)

    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

# print(sort([12,4,5,6,7,3,1,15]))