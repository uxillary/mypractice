from pydub import AudioSegment
from pydub.generators import Sine

def soft_tone(freq, duration=250, gain_db=-12):
    tone = Sine(freq).to_audio_segment(duration=duration)
    tone = tone.fade_in(80).fade_out(120).apply_gain(gain_db)
    return tone

def make_beep(filename):
    tone = soft_tone(420, duration=180)
    tone.export(filename, format="wav")

def make_buy(filename):
    tone = soft_tone(370, duration=180)
    pause = AudioSegment.silent(duration=30)
    tone2 = soft_tone(440, duration=220)
    final = tone + pause + tone2
    final.export(filename, format="wav")

def make_sell(filename):
    tone = soft_tone(480, duration=180)
    pause = AudioSegment.silent(duration=30)
    tone2 = soft_tone(350, duration=220)
    final = tone + pause + tone2
    final.export(filename, format="wav")

def make_upgrade(filename):
    freqs = [300, 360, 420, 480]
    final = AudioSegment.silent(duration=0)
    for f in freqs:
        final += soft_tone(f, duration=160)
        final += AudioSegment.silent(duration=30)
    final.export(filename, format="wav")

make_beep("beep.wav")
make_buy("buy.wav")
make_sell("sell.wav")
make_upgrade("upgrade.wav")
