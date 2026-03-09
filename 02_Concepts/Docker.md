---
type: concept
title: "Docker"
category: "devops"
tags:
  - topic/docker
related:
  - "[[Git]]"
  - "[[CI-CD]]"
  - "[[클라우드-컴퓨팅]]"
first_seen: "W03D04"
importance: medium
---

# Docker

> [!info] 한줄 정의
> 컨테이너 기반 애플리케이션 패키징 및 배포 플랫폼. 환경 의존성을 격리하여 어디서나 동일하게 실행되는 이미지를 만든다.

## 핵심 이해

Docker의 핵심 개념은 **이미지(Image)**와 **컨테이너(Container)**다. 이미지는 실행 환경과 코드를 포함한 불변 패키지이고, 컨테이너는 이미지를 실행한 인스턴스다. Dockerfile에 빌드 명령을 정의하면 레이어 캐싱으로 효율적으로 이미지를 생성한다.

**docker-compose**는 여러 컨테이너를 정의하고 함께 실행하는 도구다. FastAPI 앱, 데이터베이스, 캐시 서버 등을 하나의 `docker-compose.yml`로 관리한다. idol-agent 프로젝트에서 FastAPI + DB를 함께 컨테이너화하여 배포한다.

## 관련 강의

- [[W03D04-Docker-MySQL]]
- [[W09D01-API-이슈-LiteLLM]]

## 이미지 빌드 흐름

```mermaid
flowchart LR
    DF[Dockerfile] --> B[docker build]
    B --> IMG[이미지]
    IMG --> R[docker run]
    R --> C[컨테이너]
    DC[docker-compose.yml] --> UP[docker-compose up]
    UP --> MC[멀티 컨테이너]
```

## 관련 개념

- [[Git]] - 소스 코드 버전 관리와 연동
- [[CI-CD]] - 자동 빌드 및 배포 파이프라인
- [[클라우드-컴퓨팅]] - 클라우드 컨테이너 서비스(ECS, GKE 등)
- [[FastAPI]] - 컨테이너화 대상 앱

## 참고 자료

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Reference](https://docs.docker.com/compose/)
