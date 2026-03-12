---
type: concept
title: "BFS / DFS"
category: "algorithms"
tags:
  - topic/algorithms
related:
  - "[[그래프]]"
  - "[[트리]]"
  - "[[스택]]"
  - "[[큐]]"
first_seen: "W02D03"
importance: low
---

# BFS / DFS

> [!info] 한줄 정의
> 그래프와 트리를 탐색하는 두 가지 핵심 알고리즘. BFS는 너비 우선, DFS는 깊이 우선으로 노드를 방문한다.

## 핵심 이해

**BFS(Breadth-First Search)**는 큐를 사용하여 같은 레벨의 노드를 먼저 탐색한다. 최단 경로 탐색(가중치 없는 그래프), 레벨 순서 순회에 적합하다. 시간/공간 복잡도 모두 O(V+E)다.

**DFS(Depth-First Search)**는 스택(또는 재귀)을 사용하여 한 방향으로 끝까지 탐색 후 백트래킹한다. 경로 존재 여부, 사이클 탐지, 위상 정렬, 연결 요소 탐색에 활용된다. 재귀 구현이 직관적이며 시간/공간 복잡도 O(V+E)다.

## 탐색 순서 비교

![Diagram 1](../assets/diagrams/02_Concepts__BFS-DFS__diagram_1.svg)

## 관련 개념

- [[그래프]] - BFS/DFS의 주요 적용 대상
- [[트리]] - 트리 순회에도 활용
- [[스택]] - DFS의 반복 구현
- [[큐]] - BFS의 핵심 자료구조
- [[재귀]] - DFS 재귀 구현
