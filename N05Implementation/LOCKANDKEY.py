# def rotate90(metrix):
#   rotated = None
#   for i in range(len(metrix)):
#               # 각 cal을 zip하고 revers
#     rotated = [rc[::-1] for rc in zip(*metrix)]
#   return rotated

    

import itertools

def shift(key, direction):
    start = 0 if direction == 1 else len(key)-1
    stop = len(key)-1 if direction == 1 else 0
    
    for i in range(start, stop, direction):
      key[i] = key[i+direction]
    key[-direction] = 0
      
def goLeft(key, lock):
    lock_sum = sum(lock)
    key_sum = sum(key)  
    while(key_sum != 0):
      shift(key, 1)
      key_sum = sum(key)
      if key_sum + lock_sum == len(lock):
        return True
    return False
      
def goRight(key, lock):
    lock_sum = sum(lock)
    key_sum = sum(key)
    while(key_sum != 0):
      shift(key, -1)
      key_sum = sum(key)
      if key_sum + lock_sum == len(lock):
        return True
    return False

def solution(key, lock):
    key = list(itertools.chain(*key))
    lock = list(itertools.chain(*lock))
    if sum(lock) == len(lock):
      if sum(key) == 0: return True
      else: return False
    if sum(lock) == 0:
      if sum(key) == len(lock): return True
      else: return False
        

    if goLeft(key, lock): return True
    if goRight(key, lock): return True
    return False  
  
if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0] , [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    # lock = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    
    print(solution(key, lock))