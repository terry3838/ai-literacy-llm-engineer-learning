---
type: concept
title: "RAG (Retrieval-Augmented Generation)"
category: "ai-engineering"
tags:
  - topic/rag
related:
  - "[[Advanced-RAG]]"
  - "[[Agentic-RAG]]"
  - "[[LangGraph]]"
  - "[[Prompt-Engineering]]"
first_seen: "W05D03"
importance: high
---

# RAG (Retrieval-Augmented Generation)

> [!info] 한줄 정의
> 외부 지식을 검색하여 LLM 응답에 통합하는 기법. LLM의 지식 한계를 극복하고 최신 정보 및 도메인 특화 지식을 활용할 수 있게 한다.

## 핵심 이해

RAG는 **Query → Retrieve → Generate** 세 단계로 구성된 파이프라인이다. 사용자의 질의를 임베딩 벡터로 변환한 후, 벡터 데이터베이스에서 의미적으로 유사한 문서를 검색하고, 검색된 컨텍스트를 LLM 프롬프트에 주입하여 답변을 생성한다.

벡터 데이터베이스(Supabase pgvector, Pinecone, Chroma 등)는 RAG의 핵심 저장소다. 문서를 청크(Chunk) 단위로 분할하고 임베딩 모델로 벡터화하여 저장한다. 검색 시에는 코사인 유사도나 내적으로 가장 관련성 높은 청크를 반환한다.

RAG는 LLM의 환각(Hallucination)을 줄이고, 학습 데이터 기준일 이후의 정보를 제공하며, 답변의 출처를 명시할 수 있다는 장점이 있다. 청크 크기, 청크 오버랩, 임베딩 모델 선택이 검색 품질에 큰 영향을 미친다.

## 관련 강의

- [[W05D03-RAG-기초]]
- [[W05D04-Advanced-RAG-보안]]
- [[W06D03-Agentic-RAG-Memory]]

## 아키텍처 다이어그램

![Diagram 1](../assets/diagrams/02_Concepts__RAG__diagram_1.svg)

## 관련 개념

- [[Advanced-RAG]] - 쿼리 재작성, 재순위화 등 고급 기법
- [[Agentic-RAG]] - 에이전트 기반 자율적 RAG
- [[Prompt-Engineering]] - RAG 컨텍스트 주입 설계
- [[Supabase]] - pgvector 기반 벡터 저장소
- [[LangGraph]] - RAG 파이프라인 오케스트레이션

## 참고 자료

- [Retrieval-Augmented Generation for Large Language Models (Lewis et al., 2020)](https://arxiv.org/abs/2005.11401)
- [LangChain RAG Documentation](https://python.langchain.com/docs/use_cases/question_answering/)
