# src/gui.py
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QFileDialog, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt
from .tts_engine import TTSEngine
from .audio_utils import load_wav, save_wav

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voice Clone GUI - Demo")
        self.setGeometry(200, 200, 700, 400)
        self.engine = TTSEngine(use_cuda=True)
        self.speaker_wav = None
        self.out_wav = None
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout()

        # 파일 로드
        h1 = QHBoxLayout()
        self.load_btn = QPushButton("음성 파일 불러오기")
        self.load_btn.clicked.connect(self.load_file)
        self.file_label = QLabel("(선택된 파일 없음)")
        h1.addWidget(self.load_btn)
        h1.addWidget(self.file_label)
        layout.addLayout(h1)

        # 텍스트 입력
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("여기에 합성할 텍스트를 입력하세요.")
        layout.addWidget(self.text_edit)

        # 합성 버튼
        h2 = QHBoxLayout()
        self.synth_btn = QPushButton("합성 실행")
        self.synth_btn.clicked.connect(self.synthesize)
        self.play_btn = QPushButton("재생(시스템 오디오)")
        self.play_btn.clicked.connect(self.play_audio)
        self.save_btn = QPushButton("저장")
        self.save_btn.clicked.connect(self.save_audio)
        h2.addWidget(self.synth_btn)
        h2.addWidget(self.play_btn)
        h2.addWidget(self.save_btn)
        layout.addLayout(h2)

        # 로그
        self.log_label = QLabel("")
        self.log_label.setWordWrap(True)
        layout.addWidget(self.log_label)

        self.setLayout(layout)

    def log(self, msg):
        self.log_label.setText(str(msg))

    def load_file(self):
        fn, _ = QFileDialog.getOpenFileName(self, "음성 파일 선택", "", "Audio Files (*.wav *.mp3)")
        if fn:
            self.speaker_wav = fn
            self.file_label.setText(fn)
            self.log("음성 파일 로드 완료: %s" % fn)

    def synthesize(self):
        text = self.text_edit.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, "경고", "합성할 텍스트를 입력하세요.")
            return
        if not self.speaker_wav:
            QMessageBox.warning(self, "경고", "참조할 음성 파일을 먼저 불러오세요.")
            return
        self.log("합성 중... (GPU 사용) ... 잠시 기다려주세요")
        out_path = "out.wav"
        try:
            self.out_wav, sr = self.engine.synthesize(text=text, speaker_wav=self.speaker_wav, out_path=out_path)
            self.log(f"합성 완료: {out_path}")
        except Exception as e:
            self.log(f"합성 실패: {e}")

    def play_audio(self):
        if not self.out_wav:
            QMessageBox.information(self, "정보", "먼저 합성된 오디오가 필요합니다.")
            return
        # 간단한 재생 (platform dependent)
        try:
            import sounddevice as sd
            import soundfile as sf
            data, sr = sf.read(self.out_wav)
            sd.play(data, sr)
        except Exception as e:
            QMessageBox.warning(self, "재생 실패", str(e))

    def save_audio(self):
        if not self.out_wav:
            QMessageBox.information(self, "정보", "먼저 합성된 오디오가 필요합니다.")
            return
        fn, _ = QFileDialog.getSaveFileName(self, "저장할 파일 선택", "out.wav", "WAV Files (*.wav)")
        if fn:
            import shutil
            shutil.copy(self.out_wav, fn)
            self.log(f"저장 완료: {fn}")
