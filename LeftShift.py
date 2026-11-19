from typing import List

def leftShift(arr: List[int], K: int) -> List[int]:
    n = len(arr)
    
    if K >= n:
        return [0] * n
        
    return arr[K:] + [0] * K


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    K = 2
    print("Left Shift Output:", leftShift(arr, K))