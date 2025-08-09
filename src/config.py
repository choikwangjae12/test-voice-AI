# src/config.py
import os

ROOT = os.path.dirname(os.path.dirname(__file__))
MODELS_DIR = os.path.join(ROOT, "models")
os.makedirs(MODELS_DIR, exist_ok=True)

# Coqui TTS 모델 이름(초기값)
# 필요 시 다른 모델로 변경 가능
TTS_MODEL = "tts_models/multilingual/multi-dataset/your_tts"
VOCODER_MODEL = "vocoder/hifigan_v2"

# 합성 샘플 레이트
SAMPLE_RATE = 24000
