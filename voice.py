import sounddevice as sd
import numpy as np
from bark import generate_audio, SAMPLE_RATE, preload_models

preload_models()

def say(text):
    audio_array = generate_audio(text, history_prompt="v2/en_speaker_9")
    audio_array = np.expand_dims(audio_array, axis=1)
    stream = sd.OutputStream(samplerate=SAMPLE_RATE, channels=1)
    stream.start()
    stream.write(audio_array)
    stream.stop()
    stream.close()