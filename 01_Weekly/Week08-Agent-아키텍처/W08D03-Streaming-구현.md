---
type: lecture
week: 8
day: 3
title: "Streaming 구현"
topic: "streaming"
tags:
  - topic/streaming
status: complete
---

# Chatbot Streaming 구현

## 핵심 개념

> [!summary] 요약
> 챗봇 서비스에서 사용자 경험을 향상시키는 스트리밍 응답 구현 방법을 학습한다. SSE(Server-Sent Events)를 활용한 실시간 토큰 스트리밍, LangGraph와 FastAPI의 스트리밍 통합, 그리고 프론트엔드에서의 스트리밍 처리를 다룬다.

## 주요 내용

### 1. 스트리밍 기초
- 일반 응답 vs 스트리밍 응답의 차이
- 사용자 경험 관점에서의 스트리밍 필요성
- SSE (Server-Sent Events) 프로토콜
- 관련: [[FastAPI]]

### 2. FastAPI 스트리밍
- `StreamingResponse` 활용
- async generator를 통한 토큰 단위 전송
- SSE 이벤트 포맷팅
- 에러 핸들링과 연결 관리

### 3. LangGraph 스트리밍
- LangGraph의 `astream` / `astream_events`
- 노드별 스트리밍 출력 처리
- 중간 상태 전달 (node 시작/완료 이벤트)
- 관련: [[LangGraph]]

### 4. 프론트엔드 통합
- Gradio에서의 스트리밍 수신
- EventSource API 활용
- 실시간 UI 업데이트
- 관련: [[Gradio]]

## 흐름도

```mermaid
sequenceDiagram
    participant User as 사용자
    participant UI as Gradio UI
    participant API as FastAPI
    participant Graph as LangGraph
    participant LLM as Solar LLM

    User->>UI: 메시지 입력
    UI->>API: POST /chat (stream=true)
    API->>Graph: astream_events()
    Graph->>LLM: 토큰 생성 요청
    loop 토큰 단위
        LLM-->>Graph: 토큰
        Graph-->>API: SSE event
        API-->>UI: StreamingResponse
        UI-->>User: 실시간 표시
    end
```

## 연결된 개념
- [[LangGraph]] - LangGraph 스트리밍 API
- [[FastAPI]] - FastAPI StreamingResponse
- [[Gradio]] - Gradio UI
