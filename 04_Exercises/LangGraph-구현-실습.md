---
type: exercise
week: 8
day: 2
title: "LangGraph 에이전트 구현 실습"
tags:
  - topic/langgraph
  - topic/agent-architecture
status: 완료
---

# LangGraph 에이전트 구현 실습

> [!task] 실습 정보
> - **주차**: Week 08, Day 02
> - **유형**: 코드 구현 (Python)
> - **상태**: 완료

## 실습 목표
LangGraph 기반 에이전트 MVP 구현. State, Nodes, Edges, Graph 구성.

## 핵심 구현 사항
- AgentState 정의 (messages, intent, retrieved_docs 등)
- 노드 함수 구현 (intent_classifier, rag_retriever, tool_executor, response_generator)
- 조건부 엣지 라우팅 (chat/rag/tool)
- StateGraph 컴파일 및 FastAPI 연동

## 관련 개념
- [[LangGraph]] · [[Agent-Architecture]] · [[RAG]] · [[Tool-Calling]]
- [[W08D02-LangGraph-MVP]] · [[idol-agent-v02]]
