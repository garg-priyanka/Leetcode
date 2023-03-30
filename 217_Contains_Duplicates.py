# day 1
def containsDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

#test
print(containsDuplicate([1,2,3,0]))