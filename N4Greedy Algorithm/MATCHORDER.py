# 출전 순서 구하기

# 상대방 출전 순서를 알 때
# 최대 승수구하기

# 1. 상대방 레이팅이 크면 패배
# 2. 상대방 승수가 같거나 작으면 승리

# 상대방을 이길 수 있는 최소의 전력 (탐욕)을 매 부분문제마다 내놓으면 된다.
# 팀 전체가 이길 수 없는 경우. 가장 약한 전력을 내놓으면된다.

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from IN04TreeAndGraph import Treap


def solution():
    russians = [3000, 2700, 2800, 2200, 2500, 1900]
    koreans = [2800, 2750, 2995, 1800, 2600, 2000]

    koreanStandBy = Treap.init(koreans)
    wins = 0

    # 매 반복마다 탐색, 삭제가 일어난다. BST를 써야함..
    for russian in russians:  # N
        # 모든 한국 선수보다 레이팅이 높을 경우 가장 낮은 선수를 출전
        if Treap.kth(koreanStandBy, koreanStandBy.size).data < russian:
            # print(Treap.kth(koreanStandBy, 1).data)
            Treap.eraseKth(koreanStandBy, 1)
        else:
            key = Treap.lowerBound(koreanStandBy, russian)
            # print(Treap.kth(koreanStandBy, key).data)
            Treap.eraseKth(koreanStandBy, key)
            wins += 1
        # print(koreans)

    print(wins)


if __name__ == "__main__":
    solution()
