---
type: concept
title: "Observability (관측 가능성)"
category: "devops"
tags:
  - topic/agentops
related:
  - "[[AgentOps]]"
  - "[[CI-CD]]"
first_seen: "W09D03"
importance: medium
---

# Observability (관측 가능성)

> [!abstract] 한줄 정의
> 시스템의 내부 상태를 외부 출력(로그, 메트릭, 트레이스)을 통해 파악하는 능력.

## 핵심 이해

Observability는 로깅(Logging), 메트릭(Metrics), 트레이싱(Tracing)의 세 기둥으로 구성된다. LLM 에이전트 시스템에서는 LangSmith, AgentOps 등의 도구를 활용하여 에이전트의 실행 흐름, 토큰 사용량, 응답 품질을 모니터링한다.

## 관련 강의
- [[W09D03-Observability]] - Observability 실습

## 세 기둥

![Diagram 1](../assets/diagrams/02_Concepts__Observability__diagram_1.svg)

## 관련 개념
- [[AgentOps]] - 에이전트 운영 모니터링
- [[CI-CD]] - 배포 파이프라인 모니터링
