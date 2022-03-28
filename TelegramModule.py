import requests

url = "https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}"

botToken = "5172717646:AAE9oqTf0dWm2h9DIYhZp1dqNHsv9ACSx7A"
botChatId = "-627172603"

def send_start():
    send_message("Buurtpreventie systeem succesvol geactiveerd.")

def send_message(text):
    requests.post(url.format(botToken, botChatId, text))