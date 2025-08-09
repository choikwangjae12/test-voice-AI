@echo off
REM 환경: Python 3.10 권장, CUDA + cuDNN 설치 완료
REM 1) 가상환경 생성 (선택)
python -m venv .venv
call .venv\Scripts\activate

REM 2) 의존성 설치
pip install --upgrade pip
pip install -r requirements.txt

REM 3) PyInstaller 빌드 (onefile, 콘솔 창 없음)
pyinstaller --noconfirm --onefile --add-data "resources;resources" --add-data "legal;legal" --hidden-import=pkg_resources.py2_warn src/main.py

echo BUILD COMPLETE. 결과는 dist\main.exe 입니다.
pause
