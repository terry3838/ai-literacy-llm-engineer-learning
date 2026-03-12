---
type: concept
title: "MCP (Model Context Protocol)"
category: "ai-engineering"
tags:
  - topic/mcp
related:
  - "[[Tool-Calling]]"
  - "[[Agent-Architecture]]"
first_seen: "W06D02"
importance: medium
---

# MCP (Model Context Protocol)

> [!info] 한줄 정의
> Model Context Protocol — LLM과 외부 도구/데이터를 연결하는 표준 프로토콜. Anthropic이 제안한 개방형 표준으로 도구 통합을 표준화한다.

## 핵심 이해

MCP는 **Host**, **Client**, **Server** 세 계층으로 구성된다. Host는 Claude Desktop 같은 LLM 애플리케이션이고, Client는 MCP 서버와 통신하는 컴포넌트며, Server는 실제 도구와 리소스를 제공하는 프로세스다. JSON-RPC 2.0 프로토콜로 통신한다.

MCP Server는 세 가지 주요 기능을 제공한다. **Tools**는 LLM이 호출할 수 있는 함수, **Resources**는 파일이나 데이터 소스에 대한 접근, **Prompts**는 재사용 가능한 프롬프트 템플릿이다. 표준화된 인터페이스 덕분에 한 번 만든 MCP 서버를 여러 LLM 애플리케이션에서 재사용할 수 있다.

## 관련 강의

- [[W06D02-Tool-Calling-MCP]]

## MCP 아키텍처

![Diagram 1](../assets/diagrams/02_Concepts__MCP__diagram_1.svg)

## 관련 개념

- [[Tool-Calling]] - MCP의 기반이 되는 도구 호출 메커니즘
- [[Agent-Architecture]] - MCP를 활용한 에이전트 확장

## 참고 자료

- [MCP Official Documentation](https://modelcontextprotocol.io/)
- [MCP GitHub](https://github.com/modelcontextprotocol)
