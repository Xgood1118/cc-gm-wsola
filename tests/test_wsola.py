# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import wsola as mod  # noqa: E402

def read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def read_hex(path):
    with open(path, encoding="utf-8") as f:
        return f.read().strip()


def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()


def test_duration_scales():
    rate, s = wsola.read_wav_samples("data/speech.wav")
    out = wsola.wsola(s, rate, 1.5)
    assert abs(len(out) - len(s) / 1.5) <= 1024


def test_fast_speed_shorter():
    rate, s = wsola.read_wav_samples("data/speech.wav")
    out_slow = wsola.wsola(s, rate, 0.8)
    out_fast = wsola.wsola(s, rate, 1.2)
    assert len(out_slow) > len(out_fast)
