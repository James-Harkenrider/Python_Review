import datetime as dt
import smtplib
import random


def send_email(message):
    my_gmail = "jamespythontest2024@gmail.com"

    with open("../../../day32_gmail_app_pass.txt") as pass_file:
        password = pass_file.readline()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs="jamespythontest2024@outlook.com",
            msg=f"Subject:Hello!\n\n "
                f"{message}"
        )


with open("quotes.txt", "r") as file:
    messages = file.readlines()

now = dt.datetime.now()
day = now.weekday()
if day == 5:
    new_message = random.choice(messages)
    send_email(new_message)