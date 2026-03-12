---
type: concept
title: "FastAPI"
category: "frameworks"
tags:
  - topic/fastapi
related:
  - "[[LangGraph]]"
  - "[[Supabase]]"
  - "[[Docker]]"
first_seen: "W03D01"
importance: high
---

# FastAPI

> [!info] 한줄 정의
> Python 기반 고성능 비동기 웹 프레임워크. Pydantic과 타입 힌트를 활용하여 자동 문서화와 데이터 검증을 제공한다.

## 핵심 이해

FastAPI는 **async/await** 기반의 비동기 처리로 높은 동시성을 달성한다. Starlette을 기반으로 하며, ASGI 서버(Uvicorn)와 함께 동작한다. Python 타입 힌트를 통해 요청/응답 스키마를 정의하면 자동으로 OpenAPI(Swagger) 문서가 생성된다.

**Pydantic 모델**은 FastAPI의 핵심 데이터 검증 레이어다. 요청 바디, 쿼리 파라미터, 응답 모델을 Pydantic BaseModel로 정의하면 자동 검증과 직렬화가 이루어진다. 의존성 주입(Dependency Injection) 시스템으로 인증, DB 연결 등 공통 로직을 재사용할 수 있다.

미들웨어(Middleware)와 라우터(Router) 분리로 대규모 애플리케이션을 모듈화할 수 있다. CORS 설정, 예외 핸들러, 백그라운드 태스크도 지원한다. idol-agent 프로젝트에서 LangGraph 에이전트를 HTTP API로 노출하는 서빙 레이어로 사용된다.

## 관련 강의

- [[W03D01-개발환경-구성]]
- [[W08D01-Agent-Architecture]]

## 요청 처리 흐름

![Diagram 1](../assets/diagrams/02_Concepts__FastAPI__diagram_1.svg)

## 관련 개념

- [[LangGraph]] - 에이전트 로직 구현
- [[Supabase]] - 데이터베이스 연동
- [[Docker]] - 컨테이너 배포
- [[LiteLLM]] - LLM API 프록시 통합

## 참고 자료

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)
