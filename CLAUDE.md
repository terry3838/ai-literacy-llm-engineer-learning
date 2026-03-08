# AI Product Engineer - Interactive Learning System

이 저장소는 AI Literacy / LLM Product Engineering 과정의 **Obsidian 학습 노트 볼트**이자 **인터랙티브 학습 시스템**입니다.

## Quick Start

- `/learn` - 주차별 순서대로 학습 시작
- `/review` - 복습 퀴즈 모드
- `/explore` - 개념 허브 탐색
- `/mission` - 미션 도전
- `/roadmap` - 커리큘럼 전체 보기
- `/ask` - 학습 내용 질문
- `/progress` - 학습 진도 확인

자연어도 지원합니다: `학습시작`, `복습`, `다음`, `이전`, `퀴즈`, `도움말` 등.

## Vault Structure

```
00_Home/          # 로드맵, 전체 대시보드, 커리큘럼 캔버스
01_Weekly/        # 주차별 강의 노트 (Week01~09 -> DayXX 파일)
  Week01-AI-Literacy/            W01D03~D05
  Week02-자료구조-알고리즘/       W02D01~D05
  Week03-개발환경-Git-Docker/    W03D01~D04
  Week04-네트워크-클라우드/       (주차 인덱스)
  Week05-Prompt-Engineering-RAG/ W05D01~D05
  Week06-Agentic-Workflow/       W06D01~D05
  Week07-프로젝트/                W07 프로젝트 노트
  Week08-Agent-아키텍처/          W08D01~D05
  Week09-LLMOps/                 W09D01~D03
02_Concepts/      # 단일 개념 허브 노트 (35개)
03_Projects/      # 프로젝트 요약 (lumi-agent, 버디핏 등)
04_Missions/      # 주차별 미션 노트 (27개)
05_Resources/     # 논문/외부 참고자료 요약
exercises/        # 자기주도 실습 과제
```

## Curriculum Phases

| Phase | Weeks | Topics |
|-------|-------|--------|
| Phase 1: 기초 | Week01~02 | AI Literacy, 자료구조/알고리즘 |
| Phase 2: 개발환경 | Week03~04 | Git/Docker, 네트워크/클라우드 |
| Phase 3: AI Engineering | Week05~06 | Prompt Engineering, RAG, Agentic Workflow |
| Phase 4: 실전 | Week07~09 | 프로젝트 기획, Agent 아키텍처, LLMOps |

## Frontmatter Schema

모든 노트는 YAML frontmatter를 가진다. 타입별 필수 필드:

| type | 필수 필드 |
|------|----------|
| `lecture` | `week`, `day`, `title`, `topic`, `tags`, `status` |
| `mission` | `week`, `day`, `title`, `tags`, `status` |
| `concept` | `title`, `category`, `tags`, `related`, `first_seen`, `importance` |
| `project` | `title`, `week`, `tech_stack`, `tags`, `status` |
| `reference` | `title`, `tags` |
| `index` | `scope`, `tags` |

태그는 `topic/xxx` 형식 (예: `topic/langgraph`, `topic/docker`).

## Super Hub Concepts

Graph View에서 중심 허브 역할을 하는 핵심 개념 노트:
- `02_Concepts/RAG.md` - RAG 기초~Agentic RAG
- `02_Concepts/LangGraph.md` - 에이전트 프레임워크
- `02_Concepts/Prompt-Engineering.md` - 프롬프팅 기법
- `02_Concepts/Agent-Architecture.md` - 에이전트 설계 패턴
- `02_Concepts/FastAPI.md` - 백엔드 프레임워크

## Navigation Rules

1. **주차 노트**: `01_Weekly/WeekXX-*/` 폴더, 일별 파일 `WxxDxx-*.md`
2. **개념 허브**: `02_Concepts/`의 단일 주제 참조 노트, 주차 노트에서 wikilink로 연결
3. **미션**: `04_Missions/`의 실습 과제, `WeekXX-DayXX-*-미션.md` 패턴
4. **Wikilink**: `[[LangGraph]]` 같은 링크는 관련 노트를 찾아 연결
5. **Callout**: `> [!summary]`, `> [!info]`, `> [!task]` 등에 핵심 정보 포함

## Note Conventions

- **Wikilink**: `[[Note-Name]]` 형식 (파일명 기준)
- **Callout**: `> [!summary]`, `> [!info]`, `> [!task]`, `> [!key-concept]`
- **Mermaid**: 다이어그램은 mermaid 코드블록
- **파일명**: 한글/영문 케밥케이스 (`W03D02-Git-기본-심화.md`)

## Learning Progress

학습 진도는 `.claude/learning-progress.json`에 저장된다:
- 마지막 학습 위치 (week/day)
- 토픽별 퀴즈 점수
- 복습 필요 영역

## Response Guidelines

- 항상 한국어로 응답
- 노트 내용 제시 시 핵심 요약 먼저, 상세 내용은 후속
- 노트의 callout과 mermaid 다이어그램 활용
- wikilink로 참조된 개념 노트가 있으면 탐색 제안
- 학습 구간 완료 후 계속/복습/관련 개념 탐색 중 선택 제안

## Project Code Locations

| 노트 | 실제 코드 위치 |
|------|--------------|
| `lumi-agent-v02` | `../../../Week08/Day02/day2-mission/` |
| `lumi-agent-v06` | `../../../Week09/Day01/day6-mission/` |
| `lumi-agent-v07` | `../../../Week09/Day02/Day7_mission/` |
