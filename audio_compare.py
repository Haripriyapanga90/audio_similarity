import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cosine

# Load audio files
audio1, sr1 = librosa.load("audio1.wav", sr=None)
audio2, sr2 = librosa.load("audio2.wav", sr=None)

# Match sampling rates
if sr1 != sr2:
    audio2 = librosa.resample(audio2, orig_sr=sr2, target_sr=sr1)

# Convert to frequency domain using FFT
fft1 = np.abs(np.fft.fft(audio1))
fft2 = np.abs(np.fft.fft(audio2))
freqs = np.fft.fftfreq(len(fft1), 1/sr1)

# Plot frequency comparison
plt.figure(figsize=(10, 5))
plt.plot(freqs[:len(freqs)//2], fft1[:len(fft1)//2], label="Audio 1")
plt.plot(freqs[:len(freqs)//2], fft2[:len(fft2)//2], label="Audio 2")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Frequency Domain Comparison of Two Audio Signals")
plt.legend()
plt.grid(True)
plt.show()

# Extract MFCC features
mfcc1 = librosa.feature.mfcc(y=audio1, sr=sr1, n_mfcc=13)
mfcc2 = librosa.feature.mfcc(y=audio2, sr=sr1, n_mfcc=13)

# Compute similarity score
mfcc1_mean = np.mean(mfcc1, axis=1)
mfcc2_mean = np.mean(mfcc2, axis=1)
similarity_score = 1 - cosine(mfcc1_mean, mfcc2_mean)

print("Similarity Score:", round(similarity_score, 4))