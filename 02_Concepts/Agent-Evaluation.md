---
type: concept
title: "Agent Evaluation"
category: "agent-design"
tags:
  - topic/evaluation
related:
  - "[[Agent-Architecture]]"
  - "[[AgentOps]]"
first_seen: "W06D05"
importance: low
---

# Agent Evaluation

> [!info] 한줄 정의
> LLM 에이전트의 성능과 품질을 측정하는 방법론. 정량적 메트릭과 정성적 평가를 결합하여 에이전트의 개선 방향을 도출한다.

## 핵심 이해

**LLM-as-Judge**는 강력한 LLM을 평가자로 활용하는 기법이다. 사람의 판단 기준을 프롬프트로 정의하고, 에이전트 출력을 LLM이 채점한다. 비용 효율적이고 확장 가능하지만, 평가 LLM 자체의 편향이 문제가 될 수 있다.

**벤치마크**는 표준화된 태스크 세트로 에이전트를 평가한다. RAG 시스템에서는 Faithfulness(충실도), Relevance(관련성), Groundedness(근거성)를 측정한다. **A/B 테스트**는 두 가지 에이전트 버전을 실제 사용자에게 노출하여 성능을 비교한다. 메트릭 정의 시 비즈니스 목표와 연결되는 지표를 선택해야 한다.

## 관련 강의

- [[W06D05-Agent-평가-운영]]

## 관련 개념

- [[Agent-Architecture]] - 평가 대상 에이전트 설계
- [[AgentOps]] - 운영 중 지속적 모니터링
- [[LLM-보안]] - 보안 관점의 에이전트 평가

## 참고 자료

- [RAGAS: Evaluation Framework for RAG](https://docs.ragas.io/)
- [LangSmith Evaluation](https://docs.smith.langchain.com/evaluation)
