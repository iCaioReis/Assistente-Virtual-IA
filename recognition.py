import speech_recognition as sr

#função que reconhece a fala e transforma em texto ( utiliza api do Google)
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Fale o que deseja calcular...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="pt-BR")
            return text
        except sr.UnknownValueError:
            return "Não entendi o que você disse."
        except sr.RequestError:
            return "Erro ao conectar ao serviço de reconhecimento."
