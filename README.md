# 变速不变调

一个能在保持音高的前提下改变播放速度的变速器

## 保留签名

- `read_wav_samples(path)`
- `write_wav_samples(path, rate, samples)`
- `wsola(samples, rate, speed, win)`
- `overlap_add(frames, hop)`

## 自测

```
python -m pytest tests -q
python -m wsola.cli data/speech.wav --speed 1.5 --out fast.wav
```
