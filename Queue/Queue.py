import queue

queue = queue.Queue()
# FIFO(선입선출) 구조
# First Input First Output

# put 함수
# queue 자료에 데이터를 넣음
queue.put(1)  # 1
queue.put(2)  # 1 2
queue.put(5)  # 1 2 5

# get 함수
# queue 맨 앞 자료를 반환하고 제거한다.
queue.get()  # 출력값 1
# 자료안 2 5

# empty 함수
# queue가 비어있으면 True 반환, 그렇지 않으면 False 반환
queue.empty() # False

# qsize 함수
# queue의 size를 반환하는 함수
queue.qsize() # 2
