# src/tts_engine.py
import os
from TTS.api import TTS
from pathlib import Path
from .config import MODELS_DIR, TTS_MODEL, VOCODER_MODEL, SAMPLE_RATE

class TTSEngine:
    def __init__(self, tts_model_name=None, vocoder_name=None, use_cuda=True):
        self.tts_model_name = tts_model_name or TTS_MODEL
        self.vocoder_name = vocoder_name or VOCODER_MODEL
        self.use_cuda = use_cuda
        self._load()

    def _load(self):
        # TTS 객체 생성 (Coqui TTS API 사용)
        device = "cuda" if self.use_cuda else "cpu"
        # 모델은 로컬 캐시로 자동 다운로드 됩니다.
        self.tts = TTS(model_name=self.tts_model_name, progress_bar=False, gpu=self.use_cuda)

    def synthesize(self, text, speaker_wav=None, out_path=None):
        """
        text: 출력할 텍스트
        speaker_wav: (선택) 음성 샘플 파일 경로 (제로샷)
        out_path: 저장 경로
        returns: wav numpy array, sample_rate
        """
        if speaker_wav:
            # TTS.speak_to_file에서 voice_clone 기능 지원
            tmp_out = out_path or "out.wav"
            self.tts.tts_to_file(text=text, speaker_wav=speaker_wav, file_path=tmp_out)
            return tmp_out, SAMPLE_RATE
        else:
            tmp_out = out_path or "out.wav"
            self.tts.tts_to_file(text=text, file_path=tmp_out)
            return tmp_out, SAMPLE_RATE
