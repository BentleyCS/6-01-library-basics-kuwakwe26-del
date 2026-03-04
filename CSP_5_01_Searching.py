import random
def randomSearch(items:list, target) -> int:
    #Modify the below function such that it takes in a list of items and a target value.
    #Randomly choose an item from the list and if it isn't the target value try again.
    #print out the amount of tries it took and return the index of the target value
    i = random.randint(0,len(items)-1)
    tries = 1
    while items[i] != target:
        if items[i] == target:
            break
        else:
            tries+= 1
        i = random.randint(0,len(items)-1)
    print(f"It took {tries} attempts")
    print(tries)
    return i
#(randomSearch([1,3,5,9,7,12,11,10,2,4,6,8],5))



def linearSearch(items:list, target) ->tuple[int,int]:
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.
    i = 0
    tries = 1
    while items[i] != target:
        if items[i] == target:
            break
        elif items[i] > len(items):
            i = -1
            return i, tries
        else:
            tries += 1
        i +=1
    print(f"It took {tries} attempts")
    print(tries)
    return i, tries
#linearSearch([3,4,5,6,7,8,9],1)

def binarySearch(items:list, target) -> tuple[int,int]:
    # Modify the below function such that it implements linear search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.
    mid = int(len(items)/2)
    left = 0
    right = len(items)-1
    while left <= right:
        print(mid)
        if items[mid] == target:
            return mid
        elif target > items[mid]:
            left = mid + 1
            mid = int((left+right)/2)
        elif target < items[mid]:
            right = mid - 1
            mid = int((left+right)/2)
    return -1
binarySearch([1,3,5,7,9],10)
