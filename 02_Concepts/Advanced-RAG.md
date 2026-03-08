---
type: concept
title: "Advanced RAG"
category: "ai-engineering"
tags:
  - topic/rag
related:
  - "[[RAG]]"
  - "[[Agentic-RAG]]"
first_seen: "W05D04"
importance: medium
---

# Advanced RAG

> [!info] 한줄 정의
> 기본 RAG의 한계를 극복하는 고급 검색 증강 기법. 쿼리 재작성, 재순위화, 하이브리드 검색 등으로 검색 품질을 향상시킨다.

## 핵심 이해

**Query Rewriting**은 사용자의 모호한 질의를 더 명확하고 검색에 적합한 형태로 변환한다. HyDE(Hypothetical Document Embedding)는 가상의 답변 문서를 생성하여 임베딩 검색에 활용하는 기법이다. Multi-Query는 하나의 질의를 여러 관점으로 재작성하여 다양한 관련 문서를 검색한다.

**Re-ranking**은 벡터 검색으로 후보 문서를 수집한 뒤 Cross-Encoder 모델로 정밀 재순위화한다. **Hybrid Search**는 벡터 검색(의미적 유사도)과 BM25(키워드 매칭)를 결합하여 보완적 검색을 수행한다. **Multi-step Retrieval**은 초기 검색 결과를 기반으로 추가 검색을 반복하여 더 깊은 컨텍스트를 수집한다.

## 관련 강의

- [[W05D04-Advanced-RAG-보안]]

## 관련 개념

- [[RAG]] - 기본 RAG 파이프라인
- [[Agentic-RAG]] - 에이전트 기반 고급 RAG
- [[Prompt-Engineering]] - 쿼리 재작성 프롬프트 설계

## 참고 자료

- [Advanced RAG Techniques (Llamaindex)](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/advanced_retrieval/)
