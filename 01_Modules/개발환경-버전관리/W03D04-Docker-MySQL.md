---
type: lecture
week: 3
day: 4
title: "Docker 인프라와 MySQL 데이터베이스"
topic: "docker"
tags:
  - topic/docker
status: complete
---

# Docker 인프라와 MySQL 데이터베이스

## 핵심 개념

> [!summary] 요약
> Docker를 활용하여 개발/배포 환경의 일관성을 보장하는 방법을 학습한다. 컨테이너의 개념, Dockerfile 작성, docker-compose를 통한 멀티 컨테이너 관리, 그리고 MySQL 데이터베이스의 기초를 다룬다.

## 주요 내용

### 1. Docker의 필요성

**인프라 수준의 문제들**
- OS 차이 (Mac/Windows/Linux) -- 같은 코드도 다르게 동작할 수 있음
- 시스템 패키지/버전 차이
- 외부 서비스 환경 차이 (MySQL, Redis 등의 설정/버전)
- 서버와 로컬 환경의 불일치

> [!key-concept] Docker의 핵심 가치
> "내 컴퓨터에서는 되는데요" 문제를 해결. 개발/테스트/배포 환경을 **동일하게 패키징**하여 어디서든 같은 결과를 보장한다.

### 2. Docker 핵심 개념

| 개념 | 설명 |
|------|------|
| **이미지 (Image)** | 컨테이너를 만들기 위한 읽기 전용 템플릿 (설계도) |
| **컨테이너 (Container)** | 이미지를 기반으로 실행되는 격리된 프로세스 (실제 실행 환경) |
| **Dockerfile** | 이미지를 빌드하기 위한 명령어 스크립트 |
| **레지스트리 (Registry)** | 이미지 저장소 (Docker Hub 등) |

![Diagram 1](../../assets/diagrams/01_Modules__개발환경-버전관리__W03D04-Docker-MySQL__diagram_1.svg)

### 3. Docker 기본 명령어

| 명령어 | 설명 |
|--------|------|
| `docker build -t <이름> .` | Dockerfile로 이미지 빌드 |
| `docker run <이미지>` | 컨테이너 실행 |
| `docker ps` | 실행 중인 컨테이너 목록 |
| `docker stop <ID>` | 컨테이너 중지 |
| `docker logs <ID>` | 컨테이너 로그 확인 |
| `docker exec -it <ID> bash` | 실행 중 컨테이너에 접속 |

### 4. Docker Compose

- **목적**: 여러 컨테이너를 하나의 파일(`docker-compose.yml`)로 정의하고 한 번에 관리
- 예: 웹 앱 + 데이터베이스 + 캐시를 한 번에 실행

```yaml
# docker-compose.yml 기본 구조 예시
services:
  app:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: mydb
    ports:
      - "3306:3306"
```

| 명령어 | 설명 |
|--------|------|
| `docker-compose up` | 모든 서비스 시작 |
| `docker-compose up --build` | 이미지 재빌드 후 시작 |
| `docker-compose down` | 모든 서비스 중지 및 제거 |
| `docker-compose logs` | 전체 서비스 로그 확인 |

### 5. MySQL 데이터베이스 기초

**데이터베이스란?**
- 구조화된 데이터를 저장/관리하는 시스템
- **관계형 데이터베이스(RDBMS)**: 테이블(행/열) 형태로 데이터 저장

**MySQL 핵심 개념**
| 개념 | 설명 |
|------|------|
| Database | 테이블들의 집합 |
| Table | 행(Row)과 열(Column)으로 구성된 데이터 저장 단위 |
| Primary Key | 각 행을 고유하게 식별하는 키 |
| Foreign Key | 다른 테이블과의 관계를 나타내는 키 |
| SQL | 데이터베이스를 조작하는 질의 언어 |

**기본 SQL 문법**
```sql
-- 데이터 조회
SELECT * FROM users WHERE age > 20;

-- 데이터 삽입
INSERT INTO users (name, age) VALUES ('홍길동', 25);

-- 데이터 수정
UPDATE users SET age = 26 WHERE name = '홍길동';

-- 데이터 삭제
DELETE FROM users WHERE name = '홍길동';
```

### 6. Docker + MySQL 실습

- docker-compose로 MySQL 컨테이너 실행
- 로컬에서 MySQL 클라이언트로 접속하여 SQL 실습
- 앱 컨테이너에서 DB 컨테이너로 연결 (`depends_on`)

![Diagram 2](../../assets/diagrams/01_Modules__개발환경-버전관리__W03D04-Docker-MySQL__diagram_2.svg)

## 연결된 개념
- [[Docker]] - 컨테이너 기반 가상화 플랫폼
- [[MySQL]] - 관계형 데이터베이스
- [[Git]] - Docker 프로젝트의 버전 관리
