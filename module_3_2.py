def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender or not (recipient.endswith(('.com', '.ru', '.net')) and sender.endswith(('.com', '.ru', '.net'))):
        print(f"Невозможно отправить письмо с адреса на адрес который вы указали")
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return


    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса на адрес {recipient}.")
    else:

        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса на адрес {recipient}.")

send_email("Тестовое сообщение", "recipient@example.com")
send_email("Тестовое сообщение", "recipient@example.com", "sender@example.net")
send_email("Тестовое сообщение", "recipient@example.com", "university.help@gmail.com")
send_email("Тестовое сообщение", "recipient@example.com", "recipient@example.com")
send_email("Тестовое сообщение", "invalid.email", "sender@example.com")
