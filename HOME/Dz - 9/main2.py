# Пользователь выбирает, 1 путь из 3, при выборе , выводит загадку + ответить на
# нее исход действий, на ваш выбор.(?)

class Question:
    def __init__(self, text, real_answer):
        self.text = text
        self.real_answer = real_answer
        self.answers = [real_answer]
 
    def add_false_answer(self, answer):
        self.answers.append(answer)
 
    def __str__(self):
        return f'Загадка: {self.text}\nВарианты ответов:{list(set(self.answers))}'
 
 
class Game:
    def __init__(self):
        self.questions = []
        self.wrong = self.right = 0
 
    def add(self, question):
        self.questions.append(question)
 
    def run(self):
        for question in self.questions:
            print(question)
            answer = input('Ответ>>>')
            if answer == question.real_answer:
                print('Верно!')
                self.right += 1
            else:
                print('Неверно!')
                self.wrong += 1
        print(f'Верных ответов {self.right}, неверных {self.wrong}')
 
 
if __name__ == '__main__':
    game = Game()
    question1 = Question('Зимой и летом одним цветом', 'елка')
    question1.add_false_answer('дуб')
    question1.add_false_answer('береза')
    question2 = Question('Летит, а не птица,воет, а не зверь', 'ветер')
    question2.add_false_answer('самолёт')
    question2.add_false_answer('ракета')
    question3 = Question('Столица России', 'Москва')
    question3.add_false_answer('Вашингтон')
    question3.add_false_answer('Токио')
    question4 = Question('Белый камушек растаял,на доске следы оставил', 'мел')
    question4.add_false_answer('лёд')
    question4.add_false_answer('сахар')
    question5 = Question('Висит груша-нельзя скушать', 'лампочка')
    question5.add_false_answer('яблоко')
    question5.add_false_answer('неспелая груша')
    game.add(question1)
    game.add(question2)
    game.add(question3)
    game.add(question4)
    game.add(question5)
    game.run()