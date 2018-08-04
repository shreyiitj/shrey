# shuffle array using hashmap.

arr = [1,2,3,4]

def shuffle(arr):
    length = len(arr)
    hash_map = [-99 for i in range(length)]
    for i in arr:
        pos = i%length
        for j in range(length):
            if hash_map[pos] == -99:
                hash_map[pos] = i
                break
            else:
                pos = (pos+1)%length
    print(hash_map)

shuffle(arr)
