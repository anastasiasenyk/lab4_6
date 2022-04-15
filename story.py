from class_character import *
from streets import *

student = Friend('Олександр', 'Цей молодий хлопець здається розчарованим, він щось шукає.')
student.set_conservation('Привіт! Тобі допомогти? Що ти шукаєш?', \
                         'Привіт. Я студент, сьогодні писатиму підсумковий іспит, але по дорозі загубив свій конспект.')
student.set_question('Чи ти знаходив мій зошит?')
notebook = Thing('Зошит')
student.set_inducement(notebook)
student.set_assistance(15)


rascal = Enemy('Лайдак', 'Попереду стоїть неохайний чоловік.')

