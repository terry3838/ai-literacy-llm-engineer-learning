---
type: concept
title: "HTTP"
category: "devops"
tags:
  - topic/http
related:
  - "[[FastAPI]]"
  - "[[클라우드-컴퓨팅]]"
first_seen: "W04D01"
importance: low
---

# HTTP

> [!info] 한줄 정의
> HyperText Transfer Protocol — 웹에서 클라이언트와 서버 간 데이터를 주고받는 통신 프로토콜.

## 핵심 이해

HTTP는 **요청(Request)**과 **응답(Response)** 구조로 동작한다. 요청은 메서드, URL, 헤더, 바디로 구성되고, 응답은 상태코드, 헤더, 바디로 구성된다. REST API는 HTTP 메서드를 의미에 맞게 사용하는 설계 원칙이다.

주요 메서드: **GET**(조회), **POST**(생성), **PUT**(전체 수정), **PATCH**(부분 수정), **DELETE**(삭제). 상태코드: 2xx(성공), 3xx(리다이렉션), 4xx(클라이언트 오류: 400 Bad Request, 401 Unauthorized, 404 Not Found), 5xx(서버 오류). HTTP/2는 멀티플렉싱으로 성능을 개선하고, HTTPS는 TLS로 암호화한다.

## 요청-응답 흐름

![Diagram 1](../assets/diagrams/02_Concepts__HTTP__diagram_1.svg)

## 관련 개념

- [[FastAPI]] - HTTP 기반 REST API 구현
- [[클라우드-컴퓨팅]] - HTTP 서버 인프라
- [[CI-CD]] - HTTP API 자동 테스트

## 참고 자료

- [MDN HTTP Guide](https://developer.mozilla.org/ko/docs/Web/HTTP)
