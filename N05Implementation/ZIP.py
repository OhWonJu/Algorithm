# 문자열 압축


  
def solution(N):
    result = len(N)
    for c in range(1, len(N)//2 + 1):
        temp_str = ""
        count = 1
        prev_start = 0
        prev_end = c 
        while(prev_end <= len(N)):
            if N[prev_start : prev_end] == N[prev_end : prev_end+c]:
                count += 1
            else:
                temp_str += N[prev_start:prev_end] if count == 1 else str(count) + N[prev_start:prev_end]
                count = 1
            prev_start = prev_end
            prev_end = prev_end + c
        temp_str += N[prev_start:prev_end] if count == 1 else str(count) + N[prev_start:prev_end]
        result = min(len(temp_str), result)
    return result    

def solution2(N):
    result = len(N)
    for step in range(1, len(N)//2 + 1):
        temp_str = ""
        count = 1
        prev_str = N[0: step]
        for r in range(step, len(N), step):
            if prev_str == N[r : r + step]:
                count += 1
            else:
                temp_str += prev_str if count == 1 else str(count) + prev_str
                count = 1
                prev_str = N[r:r+step]
        temp_str += prev_str if count == 1 else str(count) + prev_str
        result = min(len(temp_str), result)
    return result

# if __name__ == "__main__":
#     solution()
    
# Pythonic...
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    # 전체 word를 1개 차이씩 zip 마지막 word는 공백과 zip
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
]

for x in a:
    print(solution(x))
