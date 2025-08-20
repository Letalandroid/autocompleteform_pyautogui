from webbrowser import open
from responses import *

# https://docs.google.com/forms/d/e/1FAIpQLScGCy48n59edD9kVyoqV8QkphBMLpaJgf-zeKwty9WTQuzrBQ/viewform

# url = input('URL del formulario: ')
url = 'https://docs.google.com/forms/d/e/1FAIpQLScGCy48n59edD9kVyoqV8QkphBMLpaJgf-zeKwty9WTQuzrBQ/viewform'
count = 3

for c in range(count):
    print(f'Running on: {count - c}')
    sleep(1)

try:
    open(url, 2)
except:
    print('URL Inválida.')

welcome()
personalData()
questions()