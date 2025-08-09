# src/audio_utils.py
import soundfile as sf
import numpy as np


def load_wav(path, target_sr=24000):
    wav, sr = sf.read(path)
    if wav.ndim > 1:
        wav = np.mean(wav, axis=1)
    if sr != target_sr:
        # 간단한 리샘플링 (scipy 의존)
        from scipy.signal import resample
        ratio = target_sr / sr
        wav = resample(wav, int(len(wav) * ratio))
    return wav.astype('float32'), target_sr


def save_wav(path, samples, sr=24000):
    sf.write(path, samples, sr)
