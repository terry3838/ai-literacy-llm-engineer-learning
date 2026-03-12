---
type: project
title: "idol-agent v0.2 - LangGraph MVP"
week: 8
tech_stack:
  - FastAPI
  - LangGraph
  - Supabase
  - Solar LLM
tags:
  - topic/langgraph
  - topic/agent-architecture
status: complete
---

# idol-agent v0.2 - LangGraph MVP

> [!info] 프로젝트 정보
> - **위치**: `Week08/Day02/day2-mission/`
> - **기술 스택**: FastAPI, LangGraph, Supabase, Solar LLM
> - **주차**: Week 08

## 아키텍처

![Diagram 1](../assets/diagrams/03_Projects__idol-agent-v02__diagram_1.svg)

## 프로젝트 구조

```
app/
  main.py              # FastAPI 진입점
  api/routes/chat.py   # 채팅 엔드포인트
  graph/
    state.py           # AgentState 정의
    nodes.py           # 노드 함수 (분류/검색/도구/응답)
    edges.py           # 조건부 엣지 (라우팅)
    graph.py           # StateGraph 구성 및 컴파일
  core/                # 설정, LLM 초기화
  repositories/        # Supabase 접근
  schemas/             # Pydantic 모델
```

## 핵심 구현 포인트

### 1. AgentState 정의
- messages, intent, retrieved_docs 등 상태 필드
- tool 관련 필드 및 세션 정보

### 2. LangGraph 노드 구현
- **intent_classifier**: LLM structured output으로 의도 분류 (chat/rag/tool)
- **rag_retriever**: Supabase pgvector 검색
- **tool_executor**: ToolExecutor로 외부 도구 실행
- **response_generator**: intent별 프롬프트로 최종 응답 생성

### 3. 조건부 엣지
- intent에 따라 chat/rag/tool 노드로 분기

### 4. 그래프 컴파일
- StateGraph 빌더 → 노드 추가 → 엣지 설정 → 컴파일

## 사용된 개념
- [[LangGraph]] - 상태 기반 에이전트 그래프
- [[Agent-Architecture]] - ReAct 패턴, 의도 분류
- [[RAG]] - 벡터 검색 기반 지식 증강
- [[Tool-Calling]] - 외부 도구 호출
- [[FastAPI]] - 비동기 API 서버
- [[Supabase]] - pgvector 벡터 DB

## 회고
- LangGraph의 노드/엣지/상태 개념을 실제 에이전트로 구현
- 의도 분류 → 조건부 라우팅 → 응답 생성의 에이전트 파이프라인 학습
