---
type: index
scope: "Week 08 - Agent 아키텍처 / 서비스 배포"
tags:
  - week/08
  - type/index
---

# Week 08: Agent 아키텍처 / 서비스 배포

> [!overview] 주간 개요
> LangGraph 기반 에이전트를 실제 서비스로 배포하는 전 과정을 학습한다. 에이전트 아키텍처 설계, LangGraph MVP 구현, 스트리밍 처리, GitHub Actions CI/CD 파이프라인까지 프로덕션 수준의 서비스 배포를 다룬다. idol-agent 프로젝트를 통해 실습한다.

## 일별 강의

| Day | 주제 | 강의 노트 | 미션 |
|-----|------|-----------|------|
| Day01 | Agent Architecture | [[W08D01-Agent-Architecture]] | 프로젝트 아키텍처 설계 |
| Day02 | LangGraph MVP | [[W08D02-LangGraph-MVP]] | idol-agent v0.2 |
| Day03 | Streaming 구현 | [[W08D03-Streaming-구현]] | 스트리밍 챗봇 |
| Day04 | GitHub Actions CI | [[W08D04-CI]] | CI 파이프라인 |
| Day05 | CD (배포) | [[W08D05-CD]] | CD 파이프라인 |

## 핵심 개념
- [[Agent-Architecture]] - 에이전트 아키텍처 패턴
- [[LangGraph]] - LangGraph 프레임워크
- [[FastAPI]] - FastAPI 백엔드
- [[Supabase]] - Supabase (pgvector)
- [[CI-CD]] - CI/CD 파이프라인

## 관련 프로젝트
- [[idol-agent-v02]] - idol-agent v0.2 LangGraph MVP

## Wrap Up
- 노트북에서 프로덕션 서비스로의 전환 방법론
- LangGraph 기반 에이전트 MVP 구현
- SSE/WebSocket 기반 스트리밍 구현
- GitHub Actions를 활용한 CI/CD 자동화
