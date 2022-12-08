def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

def count(array, element):
    count_element = 0
    for i, a in enumerate(array):
        if a == element:
            count_element += 1
    if count_element != 0:
        return count_element
    else:
        return False

array = list(map(int, input().split()))
element = int(input())

print(find(array, element))
print(count(array, element))