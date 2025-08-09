# voice-clone-gui
GPU 가속 TTS + 간단 GUI 실행파일 빌드 레포지토리

## 요구사항 (빌드 머신)
- Windows 10/11 (관리자 권한 권장)
- Python 3.10
- NVIDIA GPU + CUDA (권장: CUDA 11.7) + cuDNN (권장 일치 버전)
- Visual C++ Build Tools (PyInstaller가 내부적으로 사용함)
- 인터넷 연결 (초기 모델 다운로드)

## 빌드 방법
1. 레포지토리 클론
2. build.bat 실행 (관리자 권한 권장)
3. dist\main.exe 생성

## 실행 방법 (사용자 머신)
- 모델은 첫 실행 시 `models/` 폴더로 자동 다운로드됩니다.
- GPU가 설치되어 있으면 자동으로 CUDA로 합성합니다.

## 라이선스 및 법적
- legal/voice_consent_template.md 문서 참조

개발중0.01 버전
