# Roadmap - 커리큘럼 전체 보기

사용자가 `/roadmap` 또는 `로드맵`을 입력했습니다. 아래 절차대로 진행하세요.

## 표시 내용

1. `00_Home/00_학습로드맵.md` 파일을 읽어 커리큘럼 흐름도(mermaid)를 표시
2. 아래 형식으로 주차별 상세 내용 제시:

```
Phase 1: 기초 (Week 01~02)
  Week 01 - AI Literacy
    Day03: AI 대화 설계
    Day04: 산업별 AI 적용
    Day05: AI 윤리와 사회
  Week 02 - 자료구조와 알고리즘
    Day01: 알고리즘 분석 (시간복잡도)
    Day02: 스택, 큐, 해시
    Day03: 트리, 그래프, 탐색
    Day04: 힙, 재귀
    Day05: 정렬, 문제풀이

Phase 2: 개발환경 (Week 03~04)
  Week 03 - Git, Docker
    Day01: 개발환경 구성
    Day02: Git 기본/심화
    Day03: GitHub 협업
    Day04: Docker, MySQL
  Week 04 - 네트워크와 클라우드
    (주차 인덱스 참조)

Phase 3: AI Engineering (Week 05~06)
  Week 05 - Prompt Engineering & RAG
    Day01: 프롬프팅 기초
    Day02: 고급 프롬프팅
    Day03: RAG 기초
    Day04: Advanced RAG, 보안
    Day05: 트렌드, Agentic AI
  Week 06 - Agentic Workflow
    Day01: AI 서비스 에이전트 설계
    Day02: Tool Calling, MCP
    Day03: Agentic RAG, Memory
    Day04: Context Engineering, Safety
    Day05: Evaluation, AgentOps

Phase 4: 실전 (Week 07~09)
  Week 07 - 프로젝트
    Agent 개발 팁, AI 서비스 기획, Workflow Design
  Week 08 - Agent 아키텍처
    Day01: Agent Architecture
    Day02: LangGraph MVP
    Day03: Streaming 구현
    Day04: CI
    Day05: CD
  Week 09 - LLMOps
    Day01: API 이슈, LiteLLM
    Day02: 상태관리
    Day03: Observability
```

3. `.claude/learning-progress.json`이 있으면 완료한 항목에 체크 표시

## 후속 안내

- "어떤 주차부터 학습할까요?" 질문
- `/learn`, `/explore`, `/mission` 명령어 안내
