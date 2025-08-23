from pyautogui import hotkey, click
from webbrowser import open
from responses import *
from time import sleep

# url = input('URL del formulario: ')
url = 'https://docs.google.com/forms/d/e/1FAIpQLSfg5OzObDummVVBx_oj91IK1kQL8-5aCjLLuZsfF_FhzYTgVw/viewform'

print('')
countResponses = int(input('Introduzca el número de respuestas deseadas: '))
count = 3

print('')

for c in range(count):
    print(f'Running on: {count - c}')
    sleep(1)

for i in range(countResponses):
    open(url, 2) # Abrir URL

    sleep(5)    # Esperar a que este lista
    click()     # Y darle focus

    for _ in range(3): # Centrarnos en la primera pregunta
        press('tab')

    first_questions()
    questions()

    press('enter')

    sleep(3)
    hotkey('ctrl', 'w')
    print(f'\nQuestion {i + 1} OK.')

print('\n[!] App Finish')