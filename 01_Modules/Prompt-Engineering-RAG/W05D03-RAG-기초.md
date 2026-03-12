---
type: lecture
week: 5
day: 3
title: "RAG Fundamentals & Advanced RAG 1"
topic: "rag"
tags:
  - topic/rag
status: complete
---

# RAG Fundamentals & Advanced RAG 1

## 핵심 개념

> [!summary] 요약
> RAG(Retrieval-Augmented Generation)는 LLM의 한계(환각, 지식 제한)를 극복하기 위해 외부 지식을 검색하여 생성에 활용하는 기법이다. 문서 임베딩, 벡터 저장소, 유사도 검색, 청크 분할 등 RAG 파이프라인의 핵심 구성요소와 고급 RAG 기법(Re-ranking, Query Transformation 등)을 학습한다.

## 주요 내용

### 1. RAG란?
- **Retrieval-Augmented Generation**: 검색 증강 생성
- LLM의 한계 극복: 환각(Hallucination), 최신 정보 부재, 도메인 지식 부족
- 외부 지식 소스에서 관련 정보를 **검색**하여 생성에 활용
- 관련: [[RAG]]

### 2. RAG 파이프라인
- **문서 로딩**: 다양한 형식의 문서 수집
- **청크 분할**(Chunking): 문서를 적절한 크기로 분할
- **임베딩**(Embedding): 텍스트를 벡터로 변환
- **벡터 저장소**(Vector Store): 임베딩 벡터 저장/검색
- **유사도 검색**: 질의와 가장 관련 높은 문서 검색
- **LLM 생성**: 검색된 컨텍스트를 포함하여 응답 생성
- 관련: [[벡터 임베딩]], [[벡터 DB]]

### 3. 청크 분할 전략
- 고정 크기 분할, 의미 기반 분할
- 청크 크기와 오버랩 설정의 트레이드오프
- 관련: [[청킹]]

### 4. 임베딩과 유사도 검색
- 텍스트를 고차원 벡터 공간에 매핑
- 코사인 유사도 등으로 관련성 측정
- 관련: [[벡터 임베딩]]

### 5. Advanced RAG 기법
- **Re-ranking**: 검색 결과 재정렬로 정확도 향상
- **Query Transformation**: 질의 변환/확장으로 검색 품질 개선
- **Hybrid Search**: 키워드 검색 + 의미 검색 결합
- 관련: [[Advanced RAG]]

## 흐름도

![Diagram 1](../../assets/diagrams/01_Modules__Prompt-Engineering-RAG__W05D03-RAG-기초__diagram_1.svg)

## 연결된 개념
- [[RAG]]
- [[벡터 임베딩]]
- [[벡터 DB]]
- [[청킹]]
- [[Advanced RAG]]
