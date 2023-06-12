class Human:
    def __init__(self, name):
        self.name = name

    # ответ по умолчанию для всех одинаковый, можно
    # доверить его родительскому классу
    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю.')

    def __str__(self):
        return self.name


class Student(Human):
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос;
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone, question):
        # напечатайте на экран вопрос в нужном формате
        print(f'{someone}, {question}')
        # запросите ответ на вопрос у someone
        someone.answer_question(question)
        print()  # этот print выводит разделительную пустую строку


class Curator(Human):
    questions = {
        'мне грустненько, что делать?': 'Держись, всё получится. Хочешь видео с котиками?'
    }

    def answer_question(self, question):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса
        if question in Curator.questions:
            print(Curator.questions[question])
        else:
            super().answer_question(question)


# объявите и реализуйте классы CodeReviewer и Mentor

class CodeReviewer(Human):
    questions = {
        'что не так с моим проектом?': 'О, вопрос про проект, это я люблю.'
    }

    def answer_question(self, question):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса
        if question in CodeReviewer.questions:
            print(CodeReviewer.questions[question])
        else:
            super().answer_question(question)


class Mentor(Human):
    questions = {
        'мне грустненько, что делать?': 'Отдохни и возвращайся с вопросами по теории.',
        'как устроиться работать питонистом?': 'Сейчас расскажу.'
    }

    def answer_question(self, question):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса
        if question in Mentor.questions:
            print(Mentor.questions[question])
        else:
            super().answer_question(question)


# следующий код менять не нужно, он работает, мы проверяли
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')


answers = """
Марина, мне грустненько, что делать?
Держись, всё получится. Хочешь видео с котиками?

Ира, мне грустненько, что делать?
Отдохни и возвращайся с вопросами по теории.

Евгений, когда каникулы?
Очень интересный вопрос! Не знаю.

Евгений, что не так с моим проектом?
О, вопрос про проект, это я люблю.

Виталя, как устроиться на работу питонистом?
Очень интересный вопрос! Не знаю.

Ира, как устроиться работать питонистом?
Сейчас расскажу.
"""

correct = """
Марина, мне грустненько, что делать?
Держись, всё получится. Хочешь видео с котиками?

Ира, мне грустненько, что делать?
Отдохни и возвращайся с вопросами по теории.

Евгений, когда каникулы?
Очень интересный вопрос! Не знаю.

Евгений, что не так с моим проектом?
О, вопрос про проект, это я люблю.

Виталя, как устроиться на работу питонистом?
Очень интересный вопрос! Не знаю.

Ира, как устроиться работать питонистом?
Сейчас расскажу.
"""
print(answers == correct)