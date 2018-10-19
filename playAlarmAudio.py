import wave
import pyaudio
import winsound

CHUNK = 1024
from config import PATH
# def play():
#     wf = wave.open(f"{PATH}/src/audio/alarm.wav", 'rb')
#
#     p = pyaudio.PyAudio()
#     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                     channels=wf.getnchannels(),
#                     rate=wf.getframerate(),
#                     output=True)
#     data = wf.readframes(CHUNK)
#
#     while data:
#         stream.write(data)
#         data = wf.readframes(CHUNK)
#     stream.stop_stream()
#     stream.close()
#     p.terminate()
def play():
    winsound.PlaySound(f"{PATH}/src/audio/alarm.wav",winsound.SND_ALIAS)

