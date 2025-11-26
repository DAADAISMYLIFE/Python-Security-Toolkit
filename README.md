# Python-Security-Toolkit

파이썬으로 작성한 웹 보안 및 네트워크 프로그래밍 툴 제작 프로젝트입니다.

## 📁 프로젝트 구조

### 01_Socket_Programming (소켓 프로그래밍)
기본적인 소켓 통신과 멀티클라이언트 채팅 시스템 구현

- **basic_client.py** - 기본 소켓 클라이언트
- **basic_server.py** - 기본 소켓 서버
- **multi_chat_client.py** - 멀티 클라이언트 채팅 프로그램
- **multi_chat_server.py** - 멀티 클라이언트 채팅 서버

### 02_Requests_Library (HTTP 해킹 기법)
웹 보안 관련 요청 조작 및 프록시 활용

- **basic_requests.py** - 기본 HTTP 요청 방법
- **fake_browser.py** - User-Agent 위조를 통한 브라우저 위장
- **session_test.py** - 쿠키 및 세션 관리
- **proxy_test.py** - 프록시를 통한 네트워크 요청

### 03_Async_Performance (비동기 프로그래밍 & 성능)
동기식과 비동기식 프로그래밍 비교 및 성능 최적화

- **sync_cook.py** - 동기식 라면 요리 시뮬레이션
- **async_cook.py** - 비동기식 라면 요리 시뮬레이션
- **fast_port_scanner.py** - 비동기 포트 스캐너
- **fast_scraper.py** - 비동기 웹 스크래퍼
- **async_multi_chat_server.py** - 비동기 멀티 채팅 서버

## 🛠️ 기술 스택

- **Python 3.x**
- **socket** - 네트워크 통신
- **threading** - 멀티스레드 처리
- **asyncio** - 비동기 프로그래밍
- **requests** - HTTP 요청
- **aiohttp** - 비동기 HTTP 클라이언트

## 📝 라이센스

MIT License - 자유롭게 사용, 수정, 배포 가능합니다.

Copyright (c) 2025 DAADAISMYLIFE

---

**주요 학습 내용:**
- 소켓 프로그래밍의 기초와 실무
- 멀티스레드 및 멀티클라이언트 처리
- 웹 보안 기법 및 HTTP 프로토콜 조작
- 비동기 프로그래밍을 통한 성능 최적화
