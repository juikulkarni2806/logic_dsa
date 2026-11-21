from typing import List

def insertZeroAfterEveryElement(arr: List[int]) -> List[int]:
    n = len(arr)
    result = []
    
    for num in arr:
        if len(result) < n:
            result.append(num)
        if len(result) < n:
            result.append(0)
        else:
            break
            
    return result

if __name__ == "__main__":
    # Sample Test Case 1
    arr1 = [1, 6, 3, 2, 4, 8]
    print("Input 1 :", arr1)
    print("Output 1:", insertZeroAfterEveryElement(arr1))  # Expected: [1, 0, 2, 0, 3, 0]

    # Sample Test Case 2 (Odd length)
    arr2 = [6, 8, 9]
    print("\nInput 2 :", arr2)
    print("Output 2:", insertZeroAfterEveryElement(arr2))  # Expected: [7, 0, 8]