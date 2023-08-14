import os
import azure.cognitiveservices.speech as speechsdk
import pyaudio
import wave

def record_audio(output_filename, duration, sample_rate=16000):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=sample_rate, input=True,
                        frames_per_buffer=CHUNK)

    print("Nagrywanie...")

    frames = []

    for _ in range(0, int(sample_rate / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Nagrywanie zakończone.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

if __name__ == "__main__":
    print("Witaj w Speech2Text!")

    audio_file = "recording.wav"
    recording_duration = int(input("Dlugosc nagrania (sekudny): "))
    
    record_audio(audio_file, recording_duration)

    #następnie dodaj sdk do konwersji zapisanej mowy na tekst