#добавление различных библиотек
from gtts import gTTS
import time
import random
import playsound
import speech_recognition as sr
import os
import PySimpleGUI as sg

#блок отвечающий за приняите речи
def hearing():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите вашу команду:")
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition
    try:
        our_speech = r.recognize_google(audio, language='ru')
        print('Вы сказали: ', our_speech)
        return(our_speech)
    except sr.UnknownValueError:
        return 'errror'
    except sr.RequestError:
        return 'error'



#блок отвечающий за распознание команды
def brain(message):
    message= message.lower()
    if "прив" in message:
        mouth('Привет!')
    elif 'как тебя зовут' in message:
        mouth('Меня зовут робот')
    elif 'как' and 'дела' in message:
        mouth('У меня все отлично!')
    elif 'планы' in message:
        mouth('Мои ближайшие планы-это захват человечества')
    elif 'врем' in message:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        mouth(current_time)
    elif 'яндекс' in message:
        mouth('Хорошо')
        os.system('C:/Users/Username/AppData/Local/Yandex/YandexBrowser/Application/browser.exe')
        exit()
    elif 'пок' in message:
        mouth('Пока!')
        exit()
    else:
        mouth('Команда не распознана!')

#блок отвечающий за воспроизведение текста
def mouth(message):
    voice = gTTS(message, lang='ru')
    file_voice_name = '_audio_'+str(time.time())+'_'+str(random.randint(0, 10000))+'.mp3'
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    print('Голосовой помошник: '+ message)
    os.remove(file_voice_name)


if __name__ == '__main__':
    while True:
        command = hearing()
        brain(command)