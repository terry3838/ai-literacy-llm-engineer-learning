---
type: concept
title: "Prompt Engineering"
category: "ai-engineering"
tags:
  - topic/prompt-engineering
related:
  - "[[RAG]]"
  - "[[LLM-보안]]"
  - "[[Context-Engineering]]"
first_seen: "W05D01"
importance: high
---

# Prompt Engineering

> [!info] 한줄 정의
> LLM에 최적의 출력을 유도하기 위한 입력 설계 기법. 프롬프트의 구조, 예시, 지시 방식에 따라 모델 성능이 크게 달라진다.

## 핵심 이해

프롬프트 엔지니어링의 기본은 **Zero-shot**, **One-shot**, **Few-shot** 기법이다. Zero-shot은 예시 없이 지시만으로 수행하고, Few-shot은 몇 가지 예시를 제공하여 패턴을 학습시킨다. 시스템 프롬프트(System Prompt)는 모델의 역할, 톤, 제약 조건을 정의하는 가장 중요한 레이어다.

**Chain of Thought(CoT)** 프롬프팅은 복잡한 추론 문제에 효과적이다. "단계별로 생각하세요(Think step by step)"와 같은 지시로 모델이 중간 추론 과정을 명시하게 하여 정확도를 높인다. Self-Consistency는 여러 CoT 경로를 생성하고 다수결로 최종 답을 선택하는 방법이다.

프롬프트 체이닝(Prompt Chaining)은 복잡한 작업을 여러 단계의 프롬프트로 분해하여 순차적으로 처리한다. 각 단계의 출력이 다음 단계의 입력이 되며, RAG 시스템과 결합하면 강력한 파이프라인을 구성할 수 있다. 프롬프트 인젝션 공격에 대한 방어도 설계 단계부터 고려해야 한다.

## 관련 강의

- [[W05D01-프롬프팅-기초]]
- [[W05D02-고급-프롬프팅]]

## 기법 계층도

![Diagram 1](../assets/diagrams/02_Concepts__Prompt-Engineering__diagram_1.svg)

## 관련 개념

- [[RAG]] - 외부 지식 주입을 위한 프롬프트 설계
- [[Context-Engineering]] - 컨텍스트 윈도우 최적화
- [[LLM-보안]] - 프롬프트 인젝션 방어
- [[Agent-Architecture]] - 에이전트 시스템 프롬프트 설계

## 참고 자료

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
