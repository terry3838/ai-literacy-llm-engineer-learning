---
type: lecture
week: 6
day: 2
title: "Tool Calling Fundamentals & MCP"
topic: "tool-calling"
tags:
  - topic/tool-calling
  - topic/mcp
status: complete
---

# Tool Calling Fundamentals & MCP

## 핵심 개념

> [!summary] 요약
> LLM이 외부 도구를 호출하여 실제 작업을 수행하는 Tool Calling의 기본 원리를 학습한다. 함수 정의, 파라미터 스키마, 호출/응답 흐름을 이해하고, MCP(Model Context Protocol)를 통한 표준화된 도구 연동 방법을 다룬다.

## 주요 내용

### 1. Tool Calling 기초
- LLM이 **외부 함수/API를 호출**하여 작업을 수행하는 메커니즘
- 모델은 어떤 도구를 쓸지 **판단**하고, 파라미터를 **생성**
- 실제 실행은 외부 시스템에서 수행
- 관련: [[Tool Calling]]

### 2. 함수 정의와 스키마
- 도구의 이름, 설명, 파라미터를 **JSON Schema**로 정의
- 모델이 스키마를 이해하고 적절한 인자를 생성
- 명확한 설명이 도구 선택 정확도에 영향
- 관련: [[Tool Calling]]

### 3. Tool Calling 흐름
- 사용자 요청 -> 모델이 도구 필요성 판단 -> 함수 호출 생성 -> 실행 -> 결과 반환 -> 최종 응답
- 다중 도구 호출, 순차/병렬 실행
- 관련: [[Tool Calling]]

### 4. MCP (Model Context Protocol)
- **표준화된 도구 연동 프로토콜**
- 다양한 도구와 데이터 소스를 일관된 인터페이스로 연결
- 서버-클라이언트 아키텍처
- 도구의 검색, 호출, 결과 반환의 표준화
- 관련: [[MCP]]

### 5. MCP 실전 활용
- MCP 서버 구축 및 도구 등록
- 클라이언트에서 MCP 서버 연동
- 다양한 데이터 소스 통합
- 관련: [[MCP]]

## 흐름도

![Diagram 1](../../assets/diagrams/01_Modules__Agentic-Workflow__W06D02-Tool-Calling-MCP__diagram_1.svg)

## 연결된 개념
- [[Tool Calling]]
- [[MCP]]
- [[Agentic AI]]
- [[에이전트 패턴]]
