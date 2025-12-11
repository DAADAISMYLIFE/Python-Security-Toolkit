# Python-Security-Toolkit

파이썬으로 작성한 웹 보안, 네트워크 프로그래밍 및 모듈화 실습 프로젝트입니다.

## 📁 프로젝트 구조

### 01_Socket_Programming (소켓 프로그래밍)
기본적인 소켓 통신, 파일 전송 및 멀티클라이언트 채팅 시스템 구현

- **basic_client.py** - 기본 소켓 클라이언트
- **basic_server.py** - 기본 소켓 서버
- **file_transfer_client.py** - 파일 전송 클라이언트
- **file_transfer_server.py** - 파일 전송 서버
- **multi_chat_client.py** - 멀티 클라이언트 채팅 프로그램
- **multi_chat_server.py** - 멀티 클라이언트 채팅 서버

### 02_Requests_Library (HTTP 해킹 기법)
웹 보안 관련 요청 조작 및 프록시 활용

- **basic_requests.py** - 기본 HTTP 요청 방법
- **fake_browser.py** - User-Agent 위조를 통한 브라우저 위장
- **session_test.py** - 쿠키 및 세션 관리
- **proxy_test.py** - 프록시를 통한 네트워크 요청

### 03_Async_Performance (비동기 프로그래밍 & 성능)
동기식과 비동기식 프로그래밍 비교, 성능 최적화 및 동시성 제어

- **sync_cook.py** - 동기식 라면 요리 시뮬레이션
- **async_cook.py** - 비동기식 라면 요리 시뮬레이션
- **async_order_process.py** - 비동기 주문 처리 프로세스
- **async_timeout.py** - 비동기 작업 타임아웃 처리
- **async_timer_bomb.py** - 비동기 타이머 이벤트 실습
- **fast_port_scanner.py** - 비동기 포트 스캐너 (성능 최적화)
- **fast_scraper.py** - 비동기 웹 스크래퍼
- **async_multi_chat_server.py** - 비동기 멀티 채팅 서버
- **no_semaphore_work.py** - 세마포어 미적용 시 동시성 이슈 테스트
- **semaphore_work.py** - 세마포어를 활용한 동시성 제어 및 자원 관리

### 04_Python_Module (모듈화 및 알고리즘)
파이썬 패키지 구조화, 모듈 작성 및 알고리즘 패턴 실습

- **calculator/** - 기본 연산 모듈 패키지
  - `basic.py`, `calculator_main.py`
- **filetool/** - 파일 읽기/쓰기 처리 모듈
  - `reader.py`, `writer.py`, `filetool_main.py`
- **sorter/** - 정렬 알고리즘 및 전략 패턴(Strategy Pattern) 구현
  - `strategies/` (Bubble, Quick Sort 등), `sorter_main.py`
- **textutil/** - 텍스트 분석 및 포맷팅 도구
  - `analyzer.py`, `formatter.py`, `textutil_main.py`

### 09_Advanced_Program (고급 / 공격 시뮬레이션)
취약점 분석 및 공격 시뮬레이션 성격의 심화 예제입니다.  
**주의: 본 디렉터리의 코드는 교육용 및 격리된 환경에서의 실습용으로만 사용해야 합니다.**

- **open_port_scanner.py** - 오픈 포트 스캐닝 도구
- **rev_sh_attacker.py** - 리버스 쉘 생성·연결 (공격자 역할)
- **rev_sh_victim.py** - 리버스 쉘 수신·실행 (피해자 역할)
- **structure.md** - 해당 폴더에 대한 설명 및 실습 가이드

---

## ⚠️ 주의사항 및 안전수칙

위 스크립트 중 공격 시뮬레이션 관련 코드는 **반드시 본인이 소유한 기기 또는 허가된 가상 환경(VirtualBox, Docker 등)**에서만 실행해야 합니다. 타인의 시스템이나 공용 네트워크에서 무단으로 사용할 경우 **정보통신망법 등 관련 법령에 의해 처벌**받을 수 있습니다.

**권장 실습 환경:**
- VM(Virtual Machine) 또는 Docker 컨테이너 내부
- 외부와 격리된 사설 네트워크(Private Network)

## 🛠️ 기술 스택

- **Python 3.x**
- **Network:** `socket`, `asyncio`, `aiohttp`, `requests`
- **Concurrency:** `threading`, `asyncio` (Semaphore, Timeout)
- **Structure:** Package & Module Design, Strategy Pattern

## 📝 라이센스

MIT License - 자유롭게 사용, 수정, 배포 가능합니다.

Copyright (c) 2025 DAADAISMYLIFE

---

**주요 학습 내용:**
- 소켓 프로그래밍을 통한 네트워크 통신 이해
- 비동기(`asyncio`) 프로그래밍을 통한 고성능 애플리케이션 개발
- 파이썬 모듈 및 패키지 구조화 능력 배양
- 웹 보안 기초 및 공격 기법의 원리 이해