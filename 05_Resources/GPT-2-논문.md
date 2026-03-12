---
type: reference
title: "GPT-2: Language Models are Unsupervised Multitask Learners"
tags:
  - topic/prompt-engineering
---

# GPT-2: Language Models are Unsupervised Multitask Learners

> [!abstract] 논문 요약
> OpenAI의 GPT-2 논문. 대규모 언어 모델이 별도의 지도 학습 없이도 다양한 NLP 태스크를 수행할 수 있음을 보여줌.

## 핵심 아이디어

- **Unsupervised Multitask Learning**: 하나의 모델로 번역, 요약, QA 등 다양한 태스크 수행
- **Zero-shot Transfer**: 태스크별 파인튜닝 없이 프롬프트만으로 성능 달성
- **WebText 데이터셋**: 800만 웹페이지, 40GB 텍스트로 학습
- **모델 크기**: 1.5B 파라미터 (당시 최대)

## 아키텍처

![Diagram 1](../assets/diagrams/05_Resources__GPT-2-논문__diagram_1.svg)

## 주요 발견
- 모델 크기가 클수록 zero-shot 성능 향상 (scaling law의 초기 증거)
- 프롬프트 설계가 모델 성능에 큰 영향

## 관련 개념
- [[Prompt-Engineering]] - GPT-2가 프롬프트 기반 학습의 가능성을 보여줌
- [[GPT-3-논문]] - GPT-2의 후속 연구

