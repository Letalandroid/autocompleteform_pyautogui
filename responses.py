from pyautogui import press, click, write
from random import choice, randint
from time import sleep

nombres = ['Juan', 'Joaquin', 'Esmeralda', 'Josue', 'Gustavo', 'Mucho doxeo por un dia']
windowChangeTime = 3
windowOpenTime = 7

# Execute welcome (cierta persona quiso pedir permisos al usuario)
def welcome():
    sleep(windowOpenTime)
    click()
    for _ in range(3):
        press('tab')
    for _ in range(2):
        press('down')
    press('tab')
    press('enter')
    print('\n[!] Welcome Finish')

def personalData(): # Pata no los doxees pes :v
    sleep(windowChangeTime)
    genName()
    genAge()
    genSex()
    genState()
    genGrade()
    press('tab')
    press('enter')
    print('[!] PersonalData Finish')

def questions():
    answers = 27
    sleep(windowChangeTime)

    for _ in range(3):
        press('tab')

    for _ in range(answers):
        responses = randint(1, 5)

        for _ in range(responses):
            press('down')
        press('tab')
    press('tab')
    press('enter')
    print('[!] Questions Finish')
    sleep(windowChangeTime)


def genName():
    name = choice(nombres)

    for _ in range(3):
        press('tab')
    write(name)

def genAge():
    age = randint(18, 30)
    press('tab')
    write(f'{age}')

def genSex():
    count = randint(1, 2)
    press('tab')
    for _ in range(count):
        press('down')

def genState():
    count = randint(1, 4)
    press('tab')
    for _ in range(count):
        press('down')

def genGrade():
    count = randint(1, 10)
    press('tab')
    for _ in range(count):
        press('down')
    press('tab')