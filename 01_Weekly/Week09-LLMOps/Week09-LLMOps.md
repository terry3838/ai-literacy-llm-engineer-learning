---
type: index
scope: "Week 09 - LLMOps"
tags:
  - week/09
  - type/index
---

# Week 09: LLMOps

> [!overview] 주간 개요
> LLM 기반 서비스의 운영(LLMOps)을 학습한다. API 이슈 해결과 LiteLLM을 통한 멀티 LLM 관리, 에이전트 상태 관리 패턴, 그리고 Observability를 통한 모니터링·추적을 다룬다. lumi-agent v0.6~v0.7 프로젝트를 통해 실습한다.

## 일별 강의

| Day | 주제 | 강의 노트 | 미션 |
|-----|------|-----------|------|
| Day01 | API 이슈 & LiteLLM | [[W09D01-API-이슈-LiteLLM]] | lumi-agent v0.6 |
| Day02 | 상태 관리 | [[W09D02-상태관리]] | lumi-agent v0.7 |
| Day03 | Observability | [[W09D03-Observability]] | 모니터링 구현 |

## 핵심 개념
- [[LiteLLM]] - 멀티 LLM 프록시
- [[상태관리]] - 에이전트 상태 관리
- [[AgentOps]] - Observability & 모니터링
- [[Docker]] - Docker 기반 배포

## 관련 프로젝트
- [[lumi-agent-v06]] - lumi-agent v0.6 (LiteLLM, Docker, CI/CD)
- [[lumi-agent-v07]] - lumi-agent v0.7 (상태 관리)

## Wrap Up
- LiteLLM을 통한 다중 LLM 프로바이더 통합 관리
- 에이전트 서비스의 상태 관리 패턴
- Observability 도구를 활용한 프로덕션 모니터링
