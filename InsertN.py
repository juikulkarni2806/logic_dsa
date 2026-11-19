from typing import List

def insertAtPosition(arr: List[int], X: int, P: int) -> List[int]:
    for i in range(len(arr) - 1, P, -1):
        arr[i] = arr[i - 1]
    
    if 0 <= P < len(arr):
        arr[P] = X
        
    return arr

# --- Test in VS Code ---
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    X = 99
    P = 2
    print("Insert Output:", insertAtPosition(arr, X, P))