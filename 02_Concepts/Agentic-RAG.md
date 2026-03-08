---
type: concept
title: "Agentic RAG"
category: "ai-engineering"
tags:
  - topic/rag
related:
  - "[[RAG]]"
  - "[[Advanced-RAG]]"
  - "[[Agent-Architecture]]"
first_seen: "W06D03"
importance: medium
---

# Agentic RAG

> [!info] 한줄 정의
> 에이전트가 자율적으로 검색 전략을 결정하고 실행하는 RAG. 단순 파이프라인을 넘어 동적이고 반복적인 검색이 가능하다.

## 핵심 이해

Agentic RAG에서 에이전트는 사용자 질의를 분석하여 언제, 무엇을, 어떻게 검색할지를 스스로 결정한다. 단일 검색으로 부족한 경우 추가 검색을 수행하고, 여러 소스를 조합하며, 검색 결과를 평가하여 재검색 여부를 판단한다.

**Reflexion** 패턴은 에이전트가 자신의 답변을 자기 평가하고 개선하는 메커니즘이다. 검색 결과가 불충분하면 질의를 수정하여 재검색하고, 답변의 품질이 낮으면 추가 컨텍스트를 수집한다. **도구 통합**으로 벡터 DB, 웹 검색, SQL 쿼리 등 다양한 검색 소스를 동적으로 선택할 수 있다.

## 관련 강의

- [[W06D03-Agentic-RAG-Memory]]

## 관련 개념

- [[RAG]] - 기본 RAG 개념
- [[Advanced-RAG]] - 고급 검색 기법
- [[Agent-Architecture]] - 에이전트 설계 원칙
- [[Tool-Calling]] - 검색 도구 호출 메커니즘
- [[Memory-Management]] - 검색 결과의 메모리 통합

## 참고 자료

- [Agentic RAG (LangChain Blog)](https://blog.langchain.dev/agentic-rag-with-langgraph/)
