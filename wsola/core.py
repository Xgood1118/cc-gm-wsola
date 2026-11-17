# -*- coding: utf-8 -*-
"""变速不变调"""



def read_wav_samples(path):
    """读 16 位单声道 WAV"""
    raise NotImplementedError("read_wav_samples 尚未实现")


def write_wav_samples(path, rate, samples):
    """写 16 位单声道 WAV"""
    raise NotImplementedError("write_wav_samples 尚未实现")


def wsola(samples, rate, speed, win):
    """变速不变调"""
    raise NotImplementedError("wsola 尚未实现")


def overlap_add(frames, hop):
    """重叠相加合成"""
    raise NotImplementedError("overlap_add 尚未实现")

