---
type: reference
title: "GPT-3: Language Models are Few-Shot Learners"
tags:
  - topic/prompt-engineering
---

# GPT-3: Language Models are Few-Shot Learners

> [!abstract] 논문 요약
> OpenAI의 GPT-3 논문. 175B 파라미터 모델이 Few-shot 프롬프팅만으로 다양한 NLP 태스크에서 SOTA에 근접하는 성능을 달성.

## 핵심 아이디어

- **Few-Shot Learning**: 소수의 예시만으로 새로운 태스크 수행
- **In-Context Learning**: 파인튜닝 없이 프롬프트 내 예시로 학습
- **Scaling**: 175B 파라미터로 확장 시 emergent abilities 발현
- **3가지 모드**: Zero-shot, One-shot, Few-shot 비교

## 프롬프팅 모드 비교

```mermaid
flowchart TD
    subgraph ZeroShot["Zero-Shot"]
        Z1[태스크 설명] --> Z2[입력] --> Z3[출력]
    end
    subgraph OneShot["One-Shot"]
        O1[태스크 설명] --> O2[예시 1개] --> O3[입력] --> O4[출력]
    end
    subgraph FewShot["Few-Shot"]
        F1[태스크 설명] --> F2[예시 K개] --> F3[입력] --> F4[출력]
    end
```

## 주요 발견
- 모델 크기에 따른 성능 향상이 Few-shot에서 가장 두드러짐
- 프롬프트 엔지니어링의 효과 입증
- 대규모 언어 모델의 범용성 확인

## 관련 개념
- [[Prompt-Engineering]] - Few-shot 프롬프팅의 이론적 근거
- [[GPT-2-논문]] - GPT-3의 선행 연구
- [[RAG]] - 외부 지식 통합으로 모델 한계 보완

