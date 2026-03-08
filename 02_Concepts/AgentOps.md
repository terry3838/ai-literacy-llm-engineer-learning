---
type: concept
title: "AgentOps"
category: "agent-design"
tags:
  - topic/agentops
related:
  - "[[Agent-Evaluation]]"
  - "[[Observability]]"
first_seen: "W06D05"
importance: medium
---

# AgentOps

> [!abstract] 한줄 정의
> AI 에이전트의 운영, 모니터링, 비용 관리를 위한 운영 프레임워크.

## 핵심 이해

AgentOps는 MLOps/LLMOps의 에이전트 특화 버전이다. 에이전트의 실행 추적, 비용 모니터링, 성능 분석, 장애 대응 등 프로덕션 운영에 필요한 기능을 제공한다.

주요 기능으로는 세션 추적(에이전트 실행 흐름 기록), 비용 추적(API 호출 비용 모니터링), 성능 분석(지연시간, 처리량 측정), 그리고 알림(임계값 초과 시 알림)이 있다.

## 관련 강의
- [[W06D05-Evaluation-AgentOps]] - AgentOps 실습

## 관련 개념
- [[Agent-Evaluation]] - 에이전트 성능 평가
- [[Observability]] - 관측 가능성
- [[CI-CD]] - 배포 자동화와의 통합
