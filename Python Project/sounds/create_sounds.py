from playsound import playsound
from gtts import gTTS
from time import sleep


sounds = ["business.mp3", "crime.mp3", "entertainment.mp3", "health.mp3", "politics.mp3", "sport.mp3", "tech_science.mp3"]
texts = ["Category of the news is: Business", "Category of the news is: Crime", "Category of the news is: Entertainment",
         "Category of the news is: Health", "Category of the news is: Politics", "Category of the news is: Sport", "Category of the news is: Technology and Science",]

def createAndSave():
    global sounds, texts

    zipped = zip(texts, sounds)
    
    for item in zipped:
        tts = gTTS(item[0])
        tts.save(f"sounds/{item[1]}")


def playSound():
    global sounds

    for sound in sounds:
        playsound(f"sounds/{sound}")
        sleep(1)


createAndSave()
sleep(3)
playSound()
