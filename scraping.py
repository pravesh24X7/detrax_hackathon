import wikipedia
from gtts import gTTS
from playsound import playsound


def speak_aloud(text, name):
    
    obj = gTTS(text=text, lang='en', slow=True)
    obj.save(f'{name}.mp3')

    playsound(f'{name}.mp3')


title = input('[+] Input Search String: ')
speak = wikipedia.summary(title, sentences=3)

speak_aloud(speak)

print('[+] Other Search Results: ')
r1 = wikipedia.search(title,  results=10)

print('[+] Whole Infomation saved in file {}.html'.format(title))
name = f'{title}.html'

page_result = wikipedia.page(title)
with open(name, 'a') as file:
    file.write(page_result.html)

text_info = f'{title}.txt' 
with open(text_info, 'a') as file:
    file.write(page_result.original_title)


page_links = f'{title}.links'
with open(page_links, 'a') as file:
    file.write(str(page_result.links[:]))

