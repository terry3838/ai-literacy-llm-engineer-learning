---
type: concept
title: "CI/CD"
category: "devops"
tags:
  - topic/ci-cd
related:
  - "[[Git]]"
  - "[[Docker]]"
  - "[[클라우드-컴퓨팅]]"
first_seen: "W08D04"
importance: low
---

# CI/CD

> [!info] 한줄 정의
> 지속적 통합(Continuous Integration)과 지속적 배포(Continuous Delivery/Deployment). 코드 변경을 자동으로 빌드·테스트·배포하는 파이프라인이다.

## 핵심 이해

**CI(지속적 통합)**는 개발자가 코드를 병합할 때마다 자동으로 빌드와 테스트를 실행한다. 빠른 피드백으로 버그를 조기에 발견하고 통합 문제를 줄인다. GitHub Actions, GitLab CI, Jenkins가 대표적인 CI 도구다.

**CD(지속적 배포)**는 CI를 통과한 코드를 자동으로 스테이징 또는 프로덕션 환경에 배포한다. Docker 이미지를 빌드하고 컨테이너 레지스트리에 푸시한 뒤 클라우드 서비스에 배포하는 흐름이 일반적이다. idol-agent 프로젝트(Week09)에서 GitHub Actions 기반 CI/CD 파이프라인을 구성했다.

## 파이프라인 흐름

```mermaid
flowchart LR
    GIT["git push"] --> CI["CI\n빌드+테스트"]
    CI -- "통과" --> DR["Docker\n이미지 빌드"]
    DR --> REG["컨테이너\n레지스트리"]
    REG --> DEP["클라우드\n배포"]
    CI -- "실패" --> NOT["알림"]
```

## 관련 개념

- [[Git]] - CI/CD 트리거의 기반
- [[Docker]] - 컨테이너 이미지 빌드 및 배포
- [[클라우드-컴퓨팅]] - 배포 대상 인프라
- [[Observability]] - 배포 후 모니터링

## 참고 자료

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
