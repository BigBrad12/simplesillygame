import os
from sys import exit

class Engine(object):

    def __init__(self, stages):
        self.stages = stages

    def play(self):

        current_stage = self.stages.get_stage()
        os.system('cls')
        while True:
            next_stage = current_stage.enter()
            os.system('cls')
            current_stage = self.stages.get_next_stage(next_stage)

class LifeStage16(object):

    xp = 0

    def enter(self):

        file = open('16.txt', 'r')
        print(file.read())
        answer = input("> ")

        check_it = CheckList(answer)
        check_it.check()
        return '18'

class LifeStage18(object):


    def enter(self):
        print(f"Current XP is: {LifeStage16.xp}")
        file = open('18.txt', 'r')
        print(file.read())
        answer = input("> ")

        check_it = CheckList(answer)
        check_it.check()
        return '20'

class LifeStage20(object):


    def enter(self):
        print(f"Current XP is: {LifeStage16.xp}")
        file = open('20.txt', 'r')
        print(file.read())
        answer = input("> ")

        check_it = CheckList(answer)
        check_it.check()
        return '22'

class LifeStage22(object):


    def enter(self):
        print(f"Current XP is: {LifeStage16.xp}")
        file = open('22.txt', 'r')
        print(file.read())
        answer = input("> ")

        check_it = CheckList(answer)
        check_it.check()

        if LifeStage16.xp <= 45:
            return 'jeffrey'
        elif LifeStage16.xp > 45 and LifeStage16.xp <= 105:
            return 'conrad'
        else:
            return 'adonis'

class Adonis(object):

    def enter(self):
        file = open('adonis.txt', 'r')
        print(file.read())
        input('\nenter to close')

class Conrad(object):

    def enter(self):
        file = open('conrad.txt', 'r')
        print(file.read())
        input('\nenter to close')

class Jeffrey(object):

    def enter(self):
        file = open('jeffrey.txt', 'r')
        print(file.read())
        input("\nenter to close")

class InstantWin(object):

    def enter(self):
        file = open('instant_win.txt', 'r')
        print(file.read())
        input('\nenter to close')
        system.exit()

class Dictionary(object):

    dict = {
        '16': LifeStage16(),
        '18': LifeStage18(),
        '20': LifeStage20(),
        '22': LifeStage22(),
        'adonis': Adonis(),
        'conrad': Conrad(),
        'jeffrey': Jeffrey(),
        'instant_win': InstantWin(),
}

    def __init__(self, stage):
        self.stage = stage

    def get_stage(self):
        return Dictionary.dict.get(self.stage)

    def get_next_stage(self, stage_name):
        return Dictionary.dict.get(stage_name)

class CheckList(object):

    list = [ 'mihaela', 'role', 'model', 'read', 'book', 'books' 'study', 'school', 'community', 'friendship', 'friendships', 'respect', 'spiritual', 'spirit', 'love', 'workout', 'friend', 'good', 'learn', 'brave', 'exercise' ]

    def __init__(self, answer):
        self.answer = answer

    def check(self):
        dict = Dictionary('instant_win')
        eng = Engine(dict)
        self.answer = self.answer.lower()
        answer_list = self.answer.split()

        unwanted = [ "!", ",", ".", ":", "?" ]

        for x in range(0, len(unwanted)):
            if unwanted[x] in self.answer:
                self.answer = self.answer.replace(unwanted[x], "")
        answer_list = self.answer.split()

        for word in answer_list:
            for good in CheckList.list:
                if word == 'mihaela':
                    eng.play()
                elif word == good:
                    LifeStage16.xp += 15
        print(LifeStage16.xp)
        return

dict = Dictionary('16')
game = Engine(dict)
game.play()
