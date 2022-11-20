import collections

Deque = collections.deque()

# append(x)
# deque의 오른쪽에 x를 추가
Deque.append(1) # 1
Deque.append(3) # 1 3
Deque.append(5) # 1 3 5

# appendleft(x)
# deque의 왼쪽에 x를 추가
Deque.append(2) # 2 1 3 5
Deque.append(2) # 2 2 1 3 5

# copy()
# deque의 얕은 복사본 추가
Deque_copy = Deque.copy()

# clear()
# deque의 모든 요소를 제거하고 길이가 0인 상탤 만듦
Deque_copy.clear()

# count(x)
# deque의 x와 같은 요소의 수를 반환
Deque.count(2) # 2

# extend(iterable)
# iterable 인자에서 온 요소를 추가해서 deque의 오른쪽에 추가

# extendleft(iterable)
# iterable 인자에서 온 요소를 추가해서 deque의 왼쪽에 추가

# index(x)
# deque에 있는 x의 위치를 반홥합니다.
# 찾을 수 없으면 ValueError를 발생시킵니다.
Deque.index(1) # 2

# insert(i,x)
# x를 deque의 i 위치에 삽입합니다.
Deque.insert(2, 6) # 2 2 6 1 3 5

# pop()
# deque의 오른쪽 요소를 제거하고 반환합니다.
Deque.pop() # 5  # 2 2 6 1 3

# popleft()
# deque의 왼쪽 요소를 제거하고 반환합니다.
Deque.popleft() # 2 # 2 6 1 3

# remove(x)
# x의 첫 번째 항복을 제거합니다. 찾을 수 없으면, ValueError를 발생시킵니다.
Deque.remove(2) # 6 1 3

# rotate(n=1)
# deque을 n만큼 오른쪽으로 회전합니다. n이 음수면 왼쪽으로 회전합니다.
# 오른쪽으로 한 단계 회전하는 것은 d.appendleft(d.pop())과 동등합니다.
# 왼쪽으로 한 단계 회전하는 것은 d.append(d.popleft())와 동등합니다.
Deque.rotate(1)  # 3 6 1
Deque.rotate(-1) # 6 1 3