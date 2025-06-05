# Спершу треба встановити бібліотеку (якщо ще не встановлена)
# !pip install chatterbot chatterbot_corpus

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Створюємо чат-бота
bot = ChatBot('SchoolBot')

# Тренуємо на простих питаннях/відповідях
trainer = ListTrainer(bot)

conversation = [
    "Привіт",
    "Привіт! Як можу допомогти?",
    "Який сьогодні розклад?",
    "Сьогодні у тебе математика, англійська і фізкультура.",
    "Коли наступний шкільний захід?",
    "Наступний захід буде в п'ятницю о 15:00.",
    "Дякую",
    "Завжди радий допомогти!"
]

trainer.train(conversation)

# Запускаємо спілкування
print("Пиши щось (для виходу введи 'вихід')")

while True:
    query = input("Ти: ")
    if query.lower() == 'вихід':
        print("Бот: До побачення!")
        break
    response = bot.get_response(query)
    print("Бот:", response)
