---
type: project
title: "PPT Workspace - HTML to PPTX 변환"
week: 1
tech_stack:
  - Node.js
  - pptxgenjs
  - Playwright
tags:
  - topic/ai-literacy
status: complete
---

# PPT Workspace - HTML to PPTX 변환

> [!info] 프로젝트 정보
> - **위치**: `Week01/ppt-workspace/`
> - **기술 스택**: Node.js, pptxgenjs, Playwright
> - **주차**: Week 01

## 아키텍처

```mermaid
flowchart LR
    A[HTML 슬라이드\nslide1~7.html] --> B[Playwright\n렌더링/캡처]
    B --> C[pptxgenjs\nPPTX 생성]
    C --> D[출력\n.pptx 파일]
```

## 프로젝트 구조

```
ppt-workspace/
  create-pptx.js    # 메인 변환 스크립트
  slide1~7.html     # HTML 슬라이드 7장
  package.json       # 의존성 (pptxgenjs, playwright)
```

## 핵심 구현 포인트

### 1. HTML 슬라이드 렌더링
- Playwright로 HTML 파일을 브라우저에서 렌더링
- 각 슬라이드를 이미지로 캡처

### 2. PPTX 생성
- pptxgenjs 라이브러리로 PowerPoint 파일 생성
- 캡처된 이미지를 슬라이드로 삽입

## 사용된 개념
- Node.js 패키지 관리 (npm)
- 브라우저 자동화 (Playwright)
- 파일 변환 파이프라인

## 회고
- HTML로 슬라이드를 디자인하고 자동으로 PPTX로 변환하는 워크플로우 학습
