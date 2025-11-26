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

### 04_Advanced_Programm (고급 / 공격 시뮬레이션)

취약점 분석 및 공격 시뮬레이션 성격의 예제들이 포함되어 있습니다. 본 디렉터리의 코드는 교육용으로만 사용합니다.

- **rev_sh_attacker.py** - 리버스 쉘을 생성·연결하는 공격측 스크립트 예제 (공격자 역할)
- **rev_sh_victim.py** - 리버스 쉘을 수신·실행하는 피해측(실습용) 스크립트 예제 (피해자 역할)
- **structure.md** - 해당 폴더에 대한 설명 및 실습 가이드

주의: 위 스크립트는 보안 실습 환경(오프라인 랩 또는 개인 VM)에서만 실행해야 합니다. 공용 네트워크나 타인 시스템에 무단으로 사용하면 법적 문제가 발생할 수 있습니다.

권장 개선 및 안전수칙:
- 실습은 격리된 네트워크(예: VirtualBox, Docker, 사설 랩)에서 수행
- 코드에 인증·암호화, 입력 검증, 로깅 추가
- 테스트용 계정 및 시스템만 사용

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
