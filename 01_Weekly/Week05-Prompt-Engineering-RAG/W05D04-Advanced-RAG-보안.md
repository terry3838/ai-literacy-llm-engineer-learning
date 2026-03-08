---
type: lecture
week: 5
day: 4
title: "Advanced RAG 2 & LLM 보안"
topic: "rag"
tags:
  - topic/rag
  - topic/llm-security
status: complete
---

# Advanced RAG 2 & LLM 보안

## 핵심 개념

> [!summary] 요약
> Advanced RAG의 심화 기법(Self-RAG, CRAG, Graph RAG 등)을 학습하고, LLM의 프롬프트 기반 보안 취약점과 안전성 검증 방법을 다룬다. Prompt Injection, Jailbreaking, Data Poisoning 등 주요 공격 기법과 이에 대한 방어 전략을 이해한다.

## 주요 내용

### 1. Advanced RAG 심화
- **Self-RAG**: 모델 스스로 검색 필요성 판단 및 검증
- **CRAG (Corrective RAG)**: 검색 결과의 품질을 평가하고 보정
- **Graph RAG**: 지식 그래프 기반 RAG
- 관련: [[Advanced RAG]], [[Self-RAG]]

### 2. RAG 평가
- 검색 품질 평가: Precision, Recall, MRR
- 생성 품질 평가: Faithfulness, Relevance
- RAG 평가 프레임워크 활용
- 관련: [[RAG 평가]]

### 3. Prompt Injection 공격
- 시스템 프롬프트를 **우회하거나 무시**하도록 유도하는 공격
- Direct Injection: 직접적인 지시 변경 시도
- Indirect Injection: 외부 데이터를 통한 간접 주입
- 관련: [[Prompt Injection]]

### 4. Jailbreaking
- 모델의 **안전 가드레일을 우회**하는 기법
- 역할극, 가상 시나리오 등을 통한 제한 해제 시도
- 관련: [[Jailbreaking]]

### 5. 안전성 검증과 방어 전략
- 입력 필터링 및 검증
- 출력 모니터링
- Red Teaming을 통한 취약점 발견
- 다층 방어(Defense in Depth) 전략
- 관련: [[LLM 보안]]

> [!tip] 보안 원칙
> LLM 보안은 단일 방어가 아닌 **다층 방어** 접근이 필수적이다. 입력 검증, 시스템 프롬프트 강화, 출력 필터링을 모두 적용해야 한다.

## 연결된 개념
- [[Advanced RAG]]
- [[Self-RAG]]
- [[Prompt Injection]]
- [[Jailbreaking]]
- [[LLM 보안]]
- [[RAG 평가]]
