from typing import List

def rightShift(arr: List[int], K: int) -> List[int]:
    n = len(arr)
    
    if K >= n:
        for i in range(n):
            arr[i] = 0
        return arr
        
    for i in range(n - 1, K - 1, -1):
        arr[i] = arr[i - K]
        
    for i in range(K):
        arr[i] = 0
        
    return arr

# --- Test in VS Code ---
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    K = 2
    print("Right Shift Output:", rightShift(arr, K))