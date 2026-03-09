# Learning Mode - 주차별 순서 학습

사용자가 `/learn` 또는 `학습시작`을 입력했습니다. 아래 절차대로 진행하세요.

## 시작 절차

1. `.claude/learning-progress.json` 파일이 있으면 읽어서 마지막 학습 위치 확인
2. 처음이면: `00_Home/00_학습로드맵.md`를 읽어 커리큘럼 개요를 보여주고 "Week01부터 시작할까요?" 질문
3. 이어하기면: "지난번에 Week[X] Day[Y]까지 학습했습니다. 이어서 할까요?" 질문

## 학습 진행

### 주차 시작
1. 해당 주차의 인덱스 파일을 읽음 (예: `01_Modules/Prompt-Engineering-RAG/Week05-Prompt-Engineering-RAG.md`)
2. 주차 개요와 일별 주제 목록을 보여줌
3. "Day 1부터 시작할까요?" 질문

### 일별 학습
1. 해당 일자 파일을 읽음 (예: `01_Modules/Prompt-Engineering-RAG/W05D01-프롬프팅-기초.md`)
2. `> [!summary]` callout의 요약을 먼저 제시
3. 주요 내용을 섹션별로 설명 (mermaid 다이어그램 포함)
4. 핵심 포인트 3가지를 정리
5. "이해하셨나요?" 질문

### 사용 가능 명령어
| 입력 | 동작 |
| --- | --- |
| 다음, n, next | 다음 Day 또는 다음 Week |
| 이전, p, prev | 이전 Day |
| 퀴즈, quiz | 현재 내용 기반 퀴즈 3문제 |
| 요약, summary | 현재까지 학습 내용 요약 |
| 개념, concept | 현재 노트의 wikilink 개념 탐색 |
| 실습, exercise | 현재 주차 관련 실습 확인 |
| 종료, exit, quit | 진도 저장 후 종료 |

## 진도 저장

학습 종료 시 `.claude/learning-progress.json`에 저장:
```json
{
  "lastPosition": { "week": 5, "day": 1 },
  "completedDays": ["W01D03", "W01D04", "W01D05", "W02D01"],
  "updatedAt": "2026-03-07"
}
```

## 챕터 완료 시

1. `04_Exercises/` 폴더에서 현재 주차/일자 관련 실습 확인
2. 실습이 있으면: "관련 실습이 있습니다: [실습명]. 도전해보시겠습니까?"
3. `exercises/` 폴더에서 관련 실습 확인
4. 없으면 다음 Day로 자동 진행 제안

## 주차 완료 시

1. 해당 주차 전체 핵심 요약 제공
2. "복습 퀴즈를 풀어보시겠습니까?" 제안
3. 다음 주차 미리보기 제공
