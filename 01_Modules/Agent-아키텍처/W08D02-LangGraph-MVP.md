---
type: lecture
week: 8
day: 2
title: "LangGraph MVP"
topic: "langgraph"
tags:
  - topic/langgraph
status: complete
---

# LangGraph MVP

## 핵심 개념

> [!summary] 요약
> LangGraph를 활용하여 에이전트 MVP(Minimum Viable Product)를 구현한다. 그래프 기반의 에이전트 워크플로우를 설계하고, 노드/엣지를 구성하여 실제 동작하는 챗봇 에이전트를 만든다. idol-agent v0.2 프로젝트를 통해 실습한다.

## 주요 내용

### 1. LangGraph 핵심 개념
- **State**: 그래프 전체에서 공유되는 상태
- **Node**: 각 처리 단계 (함수)
- **Edge**: 노드 간 연결 (조건부 분기 포함)
- **Graph**: 노드와 엣지의 조합
- 관련: [[LangGraph]]

### 2. MVP 구현
- 그래프 상태 정의 (TypedDict)
- 노드 구현: chat, rag, tool_call
- 조건부 엣지를 통한 라우팅
- 체크포인터를 통한 대화 이력 관리
- 관련: [[LangGraph]]

### 3. idol-agent v0.2
- FastAPI + LangGraph 통합
- RAG 노드: Supabase pgvector 검색
- 채팅 노드: Solar LLM 호출
- API 엔드포인트 설계
- 관련: [[idol-agent-v02]]

## 실습/코드

- Day2 Mission: idol-agent v0.2 (LangGraph MVP) - `Week08/Day02/day2-mission/`

## 흐름도

![Diagram 1](../../assets/diagrams/01_Modules__Agent-아키텍처__W08D02-LangGraph-MVP__diagram_1.svg)

## 연결된 개념
- [[LangGraph]] - LangGraph 프레임워크
- [[RAG]] - Retrieval-Augmented Generation
- [[FastAPI]] - FastAPI
- [[Supabase]] - Supabase pgvector
