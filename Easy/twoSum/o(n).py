
def myTwoSum(nums, target):
    seenMap = {} #Value : Index #dictionary hashmap

    for seenValue,seenIndex in enumerate(nums):
        #print(f"Índice: {seenValue}\nValor: {seenIndex}") #Debug
        diff_needed = target - seenIndex
        if diff_needed in seenMap:
            return [seenMap[diff_needed], seenValue]
        seenMap[seenIndex] = seenValue
    return []


result = myTwoSum([1,2,3,4,5], 4)
print("The two Numbers are: ", result)

