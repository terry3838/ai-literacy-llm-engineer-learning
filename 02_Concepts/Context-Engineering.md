---
type: concept
title: "Context Engineering"
category: "ai-engineering"
tags:
  - topic/context-engineering
related:
  - "[[Prompt-Engineering]]"
  - "[[LLM-보안]]"
first_seen: "W06D04"
importance: low
---

# Context Engineering

> [!info] 한줄 정의
> LLM의 컨텍스트 윈도우를 최적으로 활용하기 위한 정보 설계 기법. 제한된 토큰 예산 내에서 최대 품질의 출력을 이끌어낸다.

## 핵심 이해

컨텍스트 윈도우는 LLM이 한 번에 처리할 수 있는 최대 토큰 수다. GPT-4는 128K, Claude는 200K 토큰까지 지원하지만, 긴 컨텍스트에서도 중요 정보가 주의를 덜 받는 **Lost in the Middle** 현상이 발생한다. 가장 중요한 정보를 컨텍스트의 앞과 뒤에 배치하는 것이 효과적이다.

**정보 밀도(Information Density)** 최적화는 중복되거나 불필요한 정보를 제거하여 토큰을 효율적으로 사용한다. 시스템 프롬프트는 간결하되 완전해야 하며, RAG로 검색된 컨텍스트는 질의와 관련성 높은 청크만 포함해야 한다. 대화 이력은 요약하거나 슬라이딩 윈도우로 관리한다.

## 관련 강의

- [[W06D04-Context-Engineering-Safety]]

## 관련 개념

- [[Prompt-Engineering]] - 시스템 프롬프트 설계
- [[LLM-보안]] - 컨텍스트 조작 공격 방어
- [[Memory-Management]] - 대화 이력 관리
- [[RAG]] - 검색된 컨텍스트 통합

## 참고 자료

- [Context Engineering (Simon Willison)](https://simonwillison.net/2025/Jun/27/context-engineering/)
