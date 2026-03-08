# Week08 실습: LangGraph 기본 그래프 구현
# 관련 강의: W08D02-LangGraph-MVP
# 관련 개념: [[LangGraph]], [[Agent-Architecture]]
#
# 이 실습을 실행하려면 langgraph 패키지가 필요합니다:
#   pip install langgraph langchain-core

# === 실습 1: 간단한 상태 그래프 ===
# TODO: 아래 그래프를 완성하세요
# 흐름: START -> greet -> ask_question -> respond -> END

from typing import TypedDict


# 상태 정의
class State(TypedDict):
    messages: list[str]
    current_step: str


# TODO: greet 노드 구현
# - State에 인사 메시지 추가
# - current_step을 "greeted"로 변경
def greet(state: State) -> State:
    pass


# TODO: ask_question 노드 구현
# - State에 질문 메시지 추가
# - current_step을 "asked"로 변경
def ask_question(state: State) -> State:
    pass


# TODO: respond 노드 구현
# - State에 응답 메시지 추가
# - current_step을 "responded"로 변경
def respond(state: State) -> State:
    pass


# === 실습 2: 조건부 라우팅 ===
# TODO: 조건부 엣지를 사용하는 그래프를 설계하세요
# 흐름: START -> classify -> (positive -> thank) or (negative -> apologize) -> END

def classify(state: State) -> State:
    # TODO: 메시지 감성을 분류하여 state에 저장
    pass


def route_by_sentiment(state: State) -> str:
    # TODO: 감성에 따라 "positive" 또는 "negative" 반환
    pass


# === 그래프 구성 (langgraph 설치 후 주석 해제) ===
# from langgraph.graph import StateGraph, START, END
#
# # 실습 1 그래프
# graph1 = StateGraph(State)
# graph1.add_node("greet", greet)
# graph1.add_node("ask_question", ask_question)
# graph1.add_node("respond", respond)
# graph1.add_edge(START, "greet")
# graph1.add_edge("greet", "ask_question")
# graph1.add_edge("ask_question", "respond")
# graph1.add_edge("respond", END)
# app1 = graph1.compile()
#
# # 테스트
# result = app1.invoke({"messages": [], "current_step": "start"})
# print("실습 1 결과:", result)


if __name__ == "__main__":
    print("LangGraph 실습 파일입니다.")
    print("langgraph 패키지 설치 후 위 주석을 해제하여 실행하세요.")
    print("pip install langgraph langchain-core")
