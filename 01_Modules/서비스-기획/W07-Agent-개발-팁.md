---
type: lecture
week: 7
day: 3
title: "Agent 개발 팁, 효과적인 프로젝트 운영 전략"
topic: "Agent 개발 전략"
tags:
  - topic/agent-architecture
status: complete
---

# Agent 개발 팁, 효과적인 프로젝트 운영 전략

## 핵심 개념

> [!summary] 요약
> TPM(Technical Program Manager)의 실무 경험을 바탕으로 한 AI Agent 개발 전략 특강. LLM 솔루션의 4단계 접근법(Prompt Engineering -> Agent Pipeline -> Fine Tuning -> Post Training), Backward Discovery를 통한 아이디어 발굴, LLM/인간/룰 기반의 역할 구분, 성능 평가 전략, 모니터링 설계를 다룬다.

## 주요 내용

### 1. AI Application 트렌드

- **기술 Driven 아이디어**: "이 기술로 어떤 문제를 해결해 볼 수 있을까?"
- **Backward Discovery**: LLM의 핵심 역량(번역, 요약, 생성, 분류)에서 출발하여 자동화할 도메인 탐색
- **개인비서의 시대**: OpenClaw, Clawdbot 등 AI를 활용한 SaaS 내재화/자체 개발 트렌드

### 2. LLM 솔루션 4단계 접근법

| Level | 단계 | 핵심 질문 |
|-------|------|--------|
| 1 | Prompt Engineering | 프롬프트 가이드만으로 해결 가능한가? |
| 2 | Agent Pipeline | 외부 지식/맥락이 필요한가? 조건별 분기가 필요한가? |
| 3 | Fine Tuning | 특정 시나리오에 특화된 일관된 모델 행동이 필요한가? |
| 4 | Post Training | 특정 도메인 지식에 대한 추가 학습이 필요한가? |

> [!tip] 핵심 원칙
> Level 1에서 시작하여 필요할 때만 다음 단계로 올라간다. 처음부터 복잡한 파이프라인을 만들지 않는다.

### 3. 역할 구분: LLM vs 인간 vs 룰 기반

| LLM이 수행할 것 | 인간이 수행할 것 | 룰 기반으로 수행할 것 |
|-------------|------------|--------------|
| 정답이 하나가 아닌 경우 | 최종 책임이 필요한 영역 | LLM이 잘 못하는 영역 |
| 맥락이 방대한 경우 | 법/윤리/전략 결정 | 단순 계산 |
| 사람이 하면 느리고 비용이 큰 영역 | 틀리면 안 되는 결정 | 규칙이 명확한 경우 |
| 언어 이해/요약/추론/패턴 인식 | Human in the loop | 항상 같은 입출력 |

### 4. 성능 목표와 평가

- **LLM은 확률모델**: 매번 답이 달라지므로 성능 지표 설정이 필수
- **평가 방법**: 도메인 전문가 평가, LLM as a Judge, 벤치마크/리더보드
- **LLM as a Judge 유형**: 정답과의 유사도 측정, T/F 판정, 후보군 순위 매기기, 점수 평가

### 5. 모니터링과 유지보수

- AI는 빠른 속도로 변화하므로 **제품의 유지보수가 더욱 중요**
- **Trace 로그**: User Query, Prompt, Assistant Output, Pipeline 단계별 결과, I/O Tokens, Latency
- **모니터링 지표**: 사용자 중단 빈도, API 에러 빈도, 파이프라인 타임아웃, 평균 토큰수, TTFT, 응답 지연시간

## 흐름도

![Diagram 1](../../assets/diagrams/01_Modules__서비스-기획__W07-Agent-개발-팁__diagram_1.svg)

## 연결된 개념

- [[W07-AI-서비스-기획]]
- [[W07-Workflow-Design]]
- [[W08D01-Agent-Architecture]]
