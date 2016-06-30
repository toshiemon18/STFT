import wave as w
import numpy as np
import matplotlib.pyplot as plt


class STFT:
    def __init__(self, wavfile):
      # Load wav file
      # Fetch sampling rate adn signal object
      wf = w.open(wavfile)
      self.sampling_rate = wf.getframerate()
      s = w.readframes(w.getnframes())
      self.signal = np.frombuffer(s, dtype="int16")
      ef.close()

      # Define constants
      n0 = 0      # start point for sa
      N = 1024    # number of sample

    # Discrete Fourier Transform
    def dft(n0, N, signal):
      G = [0.0] * N
      for i in range(N):
        for j in range(N):
          real =  np.cos(2 * np.pi * i * j / N)
          imag = -np.sin(2 * np.pi * i * j / N)
          G[k] += g[n0 + j] * complex(real, imag)
      
      return G

    # Short-Time Fourier Transform
    def stft():
      # spectral = np.fft.fft(self.signal[n0:n0+N])
      # amp = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in G]
      # phs = [np.arctan2(int(c.imag), int(c.real)) for c in G]
      # freq_list = np.fft.fftfreq(N, d=1.0/self.sampling_rate)
      winfunc = np.hamming(N)
      spectral = np.fft.fft(winfunc * self.signal[n0:n0+N])
      amp = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in spectral]

      return amp

