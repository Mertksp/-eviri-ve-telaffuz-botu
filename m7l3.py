import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random
from ses_tanıma import ses_tanima
duration = 5  # kayıt saniyeleri
sample_rate = 44100

mod = int(input("Translate uygulamasına erişmek için 0 a Telaffuz oynuna erişmek için 1 e basınız. "))
if mod == 0 :
        
    print("Şimdi konuşun...")
    recording = sd.rec(
    int(duration * sample_rate), # kaydedilecek örnek sayısı
    samplerate=sample_rate,      # örnekleme hızı
    channels=1,                  # 1, mono kayıt anlamına gelir.
    dtype="int16")               # kayıtlı örnekler için veri türü
    sd.wait()  # kayıt bitene kadar beklemek

    wav.write("output.wav", sample_rate, recording)
    print("Kayıt tamamlandı, şimdi tanıma işlemi devam ediyor...")

    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="tr")
        print("Şunu söylediniz:", text)

        lang = input("Hangi dile çevirmeliyim? (e.g., 'it' – italyanca, 'es' – İspanyolca 'en' - İngilizce 'ru' - Rusça 'pt' - Portekizce 'id' - Endonezyaca 'pl' Lehçe 'tr' - Türkçe 'de' - Almanca 'hu' - Macarca 'ja' - Japonca 'fr' Fransızca): ")

        translator = Translator()
        translated = translator.translate(text, dest=lang)  # buradaki 'es' İspanyolca için bir koddur
        print("🌍 işte istediğiniz çevirip:", translated.text)

    except sr.UnknownValueError:             # - Google gürültü veya sessizlik nedeniyle konuşmayı anlayamadığında
        print("Konuşma tanınamadı.")
    except sr.RequestError as e:             # - İnternet bağlantısı yoksa veya API kullanılamıyorsa
        print(f"Hizmet hatası: {e}")
elif mod == 1 :
    print("Telaffuz oyununa hoş geldiniz")
    seviye = input("Lütfen zorluk seviyesi seçiniz : Kolay Orta Zor: ").lower().strip()

    kelime_sozlugu = {
    "kolay": ["cat", "dog", "apple", "milk", "sun"],
    "orta": ["banana", "school", "friend", "window", "yellow"],
    "zor": ["technology", "university", "information", "pronunciation", "imagination"]
}
    if seviye == "kolay":
        print("Lütfen aşağıdaki kelimeyi telaffuz ediniz.")
        secilen = random.choice(kelime_sozlugu["kolay"])
        print(secilen)

        telaffuz = ses_tanima()
        if telaffuz == secilen:
            print("Tebrikler doğru telafuuz ettiniz.")
        else: print("Lütfen tekrar telaffuz etmeyi deneyiniz.")



else: 
    print("LÜtfen 1 veya 0 rakamlarını deneyiniz.")
    

