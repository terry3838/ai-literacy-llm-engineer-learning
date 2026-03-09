# Explore Mode - 개념 탐색

사용자가 `/explore` 또는 `탐색`을 입력했습니다. 아래 절차대로 진행하세요.

## 시작 절차

1. `02_Concepts/` 폴더의 모든 개념 노트를 카테고리별로 정리하여 제시:

### AI/LLM 핵심
- RAG, Advanced-RAG, Agentic-RAG
- Prompt-Engineering, Context-Engineering
- LLM-보안

### Agent & Workflow
- Agent-Architecture, Agentic-Workflow
- LangGraph, Tool-Calling, MCP
- AgentOps, Agent-Evaluation
- Memory-Management, 상태관리

### 인프라 & 도구
- FastAPI, Docker, Git, Supabase
- CI-CD, 클라우드-컴퓨팅, HTTP, Gradio
- LiteLLM, Observability

### 자료구조 & 알고리즘
- 스택, 큐, 해시, 트리, 그래프, 힙
- BFS-DFS, 재귀, 정렬-알고리즘, 시간복잡도

2. "어떤 개념을 탐색할까요?" 질문

## 탐색 진행

1. 선택된 개념 노트 (`02_Concepts/[개념명].md`) 읽기
2. `> [!info]` 한줄 정의 먼저 제시
3. 핵심 이해 섹션 요약
4. 관련 강의 노트 목록 (frontmatter의 `related` 필드와 wikilink)
5. Mermaid 다이어그램 포함

## 연결 탐색

개념 노트의 wikilink와 `related` 필드를 활용:
- "관련 개념: [[Agent-Architecture]], [[Agentic-Workflow]] - 탐색할까요?"
- "이 개념이 등장하는 강의: W08D02, W09D02 - 학습할까요?"

## 사용 가능 명령어

| 입력 | 동작 |
| --- | --- |
| [개념명] | 해당 개념 노트 탐색 |
| 관련, related | 현재 개념의 관련 개념 표시 |
| 강의, lecture | 이 개념이 나오는 강의 노트로 이동 |
| 미션, mission | 이 개념 관련 미션 확인 |
| 목록, list | 전체 개념 목록 다시 표시 |
| 돌아가기, back | 이전 화면으로 |
