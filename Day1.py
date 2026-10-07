# Input:  [4, 2, 9, 1, 7]
# Output: 9

def find_max(nums):
    if not nums:
        return "list is empty"
    # k = nums[0]
    # for i in range(len(nums)):
    #     if k < nums[i]:
    #         k = nums[i]
    k = 0
    for num in nums:
        if num > k:
            k = num

    return k

def count_even(nums):
    count = 0
    for num in nums:
        if num%2 == 0:
            count += 1
    return count

def running_sum(nums):
    l =[]
    k = 0
    for r in range(len(nums)):
        k += nums[r]
        l.append(k)
    return l

def range_sum(nums, left, right):
    k = 0
    for i in range(left , right+1):
        k += nums[i]
    return k


def second_max(nums):
    k = nums[0]
    for i in range(1,len(nums)):
        if k > nums[i]:
            nums[i] , k=  k, nums[i]
    return nums[-2]

second_max([2,6,8,3,5,2,4])

def reverseVowels(f):
    k = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    l = 0
    r = len(f)-1
    s = list(f)
    while l < r :
        while l < r and  s[l] not in k:
            l+=1
        while l < r and  s[r] not in k: 
            r-=1
        s[l], s[r] = s[r], s[l]
        l+=1
        r-=1
    return "".join(s)


def first(s):
    f = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] != s[j]:
                print(s[i] , "------> " , s[j])
                f.append(i)
    if not f:
        return -1
    else:
        return f[0]

def isSub(s,t):
    k = set()
    j = [item for item in t if item in s and not (item in k or k.add(item))]
    h = "".join(k)
    l = t.replace(h,"")
    print(h)
    print(l)
    print(k)
    if h == s:
        return True
    elif l == s:
        return True
    else:
        return False

def UniqueElements(arr): #   [1,1,2,2,3,3,4,4]
    l = 0
    for r in range(len(arr)):
        if arr[l] != arr[r]:
            l+=1
            arr[l] = arr[r]
    return l+1

print(UniqueElements( [1,1,2,2,3,3,4,4]))

