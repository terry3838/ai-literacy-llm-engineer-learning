---
type: concept
title: "Memory Management"
category: "agent-design"
tags:
  - topic/agent-architecture
related:
  - "[[Agent-Architecture]]"
  - "[[RAG]]"
  - "[[Supabase]]"
first_seen: "W06D03"
importance: medium
---

# Memory Management

> [!info] 한줄 정의
> LLM 에이전트가 대화 맥락과 과거 경험을 저장·검색하는 메커니즘. 상태 없는 LLM에 지속성을 부여한다.

## 핵심 이해

에이전트 메모리는 네 가지 유형으로 구분된다. **단기 메모리(Short-term)**는 현재 대화의 컨텍스트 윈도우 내 이력이고, **장기 메모리(Long-term)**는 벡터 DB에 저장된 과거 대화 및 지식이다. **에피소드 메모리(Episodic)**는 특정 경험과 사건의 기록이고, **의미 메모리(Semantic)**는 도메인 지식과 사실 정보다.

**Conversation Buffer Memory**는 모든 대화를 그대로 저장하여 간단하지만 토큰 소모가 크다. **Summary Memory**는 대화를 주기적으로 요약하여 토큰을 절약한다. **벡터 메모리**는 임베딩으로 저장하고 관련성 기반으로 검색하여 장기 메모리를 효율적으로 관리한다. idol-agent에서 Supabase를 장기 메모리 저장소로 활용한다.

## 관련 강의

- [[W06D03-Agentic-RAG-Memory]]

## 메모리 유형 분류

![Diagram 1](../assets/diagrams/02_Concepts__Memory-Management__diagram_1.svg)

## 관련 개념

- [[Agent-Architecture]] - 메모리를 활용한 에이전트 설계
- [[RAG]] - 장기 메모리의 벡터 검색
- [[Supabase]] - 메모리 영속화 저장소
- [[LangGraph]] - 체크포인터 기반 상태 메모리
