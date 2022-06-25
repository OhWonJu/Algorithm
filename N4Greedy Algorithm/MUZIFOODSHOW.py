import heapq

def solution(food_times, k):
    if sum(food_times) <=k:
        return -1
    
    foods_pair = []
    for i in range(len(food_times)):
        heapq.heappush(foods_pair, (food_times[i], i+1))
                
    left_foods = len(foods_pair)
    spand_eating_time = 0
    prev_eating_time = 0
    
    while spand_eating_time + (foods_pair[0][0] - prev_eating_time) * left_foods <= k: 
        now = heapq.heappop(foods_pair)[0]  
        spand_eating_time += (now - prev_eating_time) * left_foods
        prev_eating_time = now
        left_foods -= 1

    result = sorted(foods_pair, key = lambda x: x[1])
    return result[(k-spand_eating_time) % left_foods][1]
  
if __name__ == "__main__":
    food_times = [3, 1, 2]
    k = 5
    solution(food_times, k)