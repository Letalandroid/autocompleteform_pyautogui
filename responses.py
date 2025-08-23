from pyautogui import press
from random import randint


def first_questions():
    resQuestions(1)
    resQuestions(1, 4)
    resQuestions(1)

    print('[!] First Questions Finish')

def questions():
    answers = 46
    resQuestions(answers, initPoint=2)

    print('[!] Questions Finish')

def resQuestions(answers: int, maxQuestions: int = 5, initPoint: int = 0):

    for _ in range(answers):
        responses = randint(initPoint, maxQuestions - 1)
        print(initPoint, responses)
        salt = maxQuestions - responses

        for _ in range(responses):
            press('tab')

        press('space')

        for _ in range(salt):
            press('tab')