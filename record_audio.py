import sounddevice as sd
import soundfile as sf

duration = 5  # seconds
sample_rate = 44100  # Hz

print("Recording Audio 1... Speak now!")
audio1 = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
sd.wait()
sf.write("audio1.wav", audio1, sample_rate)
print("Saved audio1.wav")

print("Recording Audio 2... Speak now!")
audio2 = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
sd.wait()
sf.write("audio2.wav", audio2, sample_rate)
print("Saved audio2.wav")