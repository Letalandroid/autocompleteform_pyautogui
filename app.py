from pyautogui import hotkey
from webbrowser import open
from responses import *

# https://docs.google.com/forms/d/e/1FAIpQLScGCy48n59edD9kVyoqV8QkphBMLpaJgf-zeKwty9WTQuzrBQ/viewform

# url = input('URL del formulario: ')
url = 'https://docs.google.com/forms/d/e/1FAIpQLScGCy48n59edD9kVyoqV8QkphBMLpaJgf-zeKwty9WTQuzrBQ/viewform'

print('')
countResponses = int(input('Introduzca el número de respuestas deseadas: '))
count = 3

print('')

for c in range(count):
    print(f'Running on: {count - c}')
    sleep(1)

for _ in range(countResponses):
    try:
        open(url, 2)
    except:
        print('URL Inválida.')

    welcome()
    personalData()
    questions()
    hotkey('ctrl', 'w')

print('\n[!] App Finish')