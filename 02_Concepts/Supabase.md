---
type: concept
title: "Supabase"
category: "frameworks"
tags:
  - topic/supabase
related:
  - "[[FastAPI]]"
  - "[[LangGraph]]"
  - "[[RAG]]"
first_seen: "W08D02"
importance: medium
---

# Supabase

> [!info] 한줄 정의
> PostgreSQL 기반의 오픈소스 BaaS(Backend as a Service). 실시간 데이터베이스, 인증, 스토리지를 통합 제공하며 pgvector로 벡터 검색도 지원한다.

## 핵심 이해

Supabase의 핵심은 **PostgreSQL** 위에 구축된 풀스택 백엔드다. 자동 생성되는 REST/GraphQL API, 실시간 구독(WebSocket), Row Level Security(RLS)로 데이터 접근 제어를 제공한다. Firebase의 오픈소스 대안으로 자체 호스팅도 가능하다.

**pgvector** 확장은 PostgreSQL에서 벡터 유사도 검색을 가능하게 한다. RAG 시스템에서 임베딩을 저장하고 코사인 유사도로 검색하는 벡터 데이터베이스로 활용된다. lumi-agent 프로젝트에서 대화 기록, 메모리, 벡터 임베딩을 모두 Supabase에 저장한다.

LangGraph의 체크포인터 백엔드로도 사용된다. 에이전트 실행 상태를 Supabase에 영속화하여 중단된 대화를 재개하거나 특정 시점의 상태로 복원할 수 있다.

## 관련 강의

- [[W08D02-LangGraph-MVP]]
- [[W09D01-API-이슈-LiteLLM]]

## 관련 개념

- [[FastAPI]] - Supabase Python 클라이언트 통합
- [[LangGraph]] - 체크포인터 백엔드로 활용
- [[RAG]] - pgvector 기반 벡터 검색
- [[Memory-Management]] - 장기 메모리 저장소

## 참고 자료

- [Supabase Documentation](https://supabase.com/docs)
- [pgvector GitHub](https://github.com/pgvector/pgvector)
