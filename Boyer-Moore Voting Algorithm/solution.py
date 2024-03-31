#for finding the majority element based on a criteria
#criteria - the denominator

def majority_element(nums, criteria):
    n = len(nums)
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
        
    verificationCount = nums.count(candidate)
    print(candidate)
    print(verificationCount)
    
    if verificationCount > n // criteria:
        return candidate
    else: 
        return None

def main():
    input_arr = [2, 2, 1, 1, 0, 0, 5, 2, 2]
    ans = majority_element(input_arr, 2)
    print(f"The majority element is {ans}")

if __name__ == "__main__":
    main()
        