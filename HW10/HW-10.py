class Hero:
    def __init__(self, name):
        self.name = name


class Ded(Hero):
    def ask_babka_to_bake_kolobok(self, babka):
        print('_______')
        babka.bake_kolobok()


class Babka(Hero):

    def bake_kolobok(self):
        print(')))))')


class Kolobok(Hero):
    def escape(self):
        print('escape')

    def die(self):
        print('((((((')


class Fox(Hero):

    def eat_kolobok(self, kolobok):
        print('eat')
        kolobok.die()


def tale():

    ded = Ded('ded')
    babka = Babka('babka')
    kolobok = Kolobok('kolobok')
    fox = Fox('fox')

    ded.ask_babka_to_bake_kolobok(babka)
    babka.bake_kolobok()
    kolobok.escape()
    fox.eat_kolobok(kolobok)


tale()