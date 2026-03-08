---
type: mission
week: 9
day: 1
title: "LiteLLM 통합 + Docker 미션"
tags:
  - topic/litellm
  - topic/docker
status: submitted
---

# LiteLLM 통합 + Docker 미션

> [!task] 미션 정보
> - **주차**: Week 09, Day 01
> - **유형**: 코드 구현 (Python)
> - **상태**: 제출 완료

## 미션 내용
LiteLLM Router 설정, 폴백 모델 구성, Tool 에러 핸들링 구현.

## 핵심 구현 사항
- LiteLLM 환경변수 추가 (use_litellm, fallback_model, timeout)
- RetryPolicy + Router 생성 (Primary: Solar, Fallback: Gemini)
- asyncio.wait_for 타임아웃 적용
- Docker 컨테이너화

## 관련 개념
- [[LiteLLM]] · [[Docker]] · [[CI-CD]]
- [[W09D01-API-이슈-LiteLLM]] · [[lumi-agent-v06]]
