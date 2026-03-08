---
type: mission
week: 9
day: 2
title: "상태관리 + 비용 추적 미션"
tags:
  - topic/state-management
  - topic/langgraph
status: submitted
---

# 상태관리 + 비용 추적 미션

> [!task] 미션 정보
> - **주차**: Week 09, Day 02
> - **유형**: 코드 구현 (Python)
> - **상태**: 제출 완료

## 미션 내용
LangGraph 체크포인터, 토큰 카운터, 비용 추적, 메시지 트리밍 구현.

## 핵심 구현 사항
- Checkpointer 선택 로직 (MemorySaver vs PostgreSQL)
- tiktoken 기반 토큰 수 계산
- Discord Webhook 비용 알림
- 메시지 트리밍 for 루프

## 관련 개념
- [[상태관리]] · [[LangGraph]] · [[Supabase]]
- [[W09D02-상태관리]] · [[lumi-agent-v07]]
