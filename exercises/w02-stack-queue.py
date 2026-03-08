# Week02 실습: 스택과 큐 구현
# 관련 강의: W02D02-스택-큐-해시
# 관련 개념: [[스택]], [[큐]]

# === 실습 1: 스택 구현 ===
# TODO: 리스트를 이용한 스택 클래스를 구현하세요
# - push(item): 스택에 아이템 추가
# - pop(): 스택에서 아이템 제거 및 반환
# - peek(): 최상단 아이템 확인 (제거하지 않음)
# - is_empty(): 스택이 비어있는지 확인
# - size(): 스택 크기 반환

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        # TODO: 구현하세요
        pass

    def pop(self):
        # TODO: 구현하세요
        pass

    def peek(self):
        # TODO: 구현하세요
        pass

    def is_empty(self):
        # TODO: 구현하세요
        pass

    def size(self):
        # TODO: 구현하세요
        pass


# === 실습 2: 큐 구현 ===
# TODO: 리스트를 이용한 큐 클래스를 구현하세요
# - enqueue(item): 큐에 아이템 추가
# - dequeue(): 큐에서 아이템 제거 및 반환
# - front(): 맨 앞 아이템 확인
# - is_empty(): 큐가 비어있는지 확인
# - size(): 큐 크기 반환

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # TODO: 구현하세요
        pass

    def dequeue(self):
        # TODO: 구현하세요
        pass

    def front(self):
        # TODO: 구현하세요
        pass

    def is_empty(self):
        # TODO: 구현하세요
        pass

    def size(self):
        # TODO: 구현하세요
        pass


# === 실습 3: 괄호 검사기 ===
# TODO: 스택을 이용하여 괄호가 올바르게 짝지어졌는지 검사하는 함수를 구현하세요
# 예: "(())" -> True, "([)]" -> False, "{[]()}" -> True

def check_brackets(expression: str) -> bool:
    # TODO: 위에서 구현한 Stack 클래스를 활용하여 구현하세요
    pass


# === 테스트 ===
if __name__ == "__main__":
    # 스택 테스트
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.peek() == 2
    assert s.size() == 2
    print("스택 테스트 통과!")

    # 큐 테스트
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    assert q.dequeue() == "a"
    assert q.front() == "b"
    assert q.size() == 2
    print("큐 테스트 통과!")

    # 괄호 검사 테스트
    assert check_brackets("(())") == True
    assert check_brackets("([)]") == False
    assert check_brackets("{[]()}") == True
    assert check_brackets("") == True
    assert check_brackets("(") == False
    print("괄호 검사 테스트 통과!")

    print("\n모든 테스트 통과!")
