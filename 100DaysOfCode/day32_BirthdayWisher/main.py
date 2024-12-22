import pandas
import datetime as dt
import random
import smtplib


def send_email(message):
    my_gmail = "Blank@gmail.com"

    with open("../../../day32_gmail_app_pass.txt") as pass_file:
        password = pass_file.readline()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs="blank@outlook.com",
            msg=f"Subject:Happy Birthday!\n\n "
                f"{message}"
        )


today_month = dt.datetime.now().month
today_day = dt.datetime.now().day
birthdays_df = pandas.read_csv("birthdays.csv")
birthday_to_send = birthdays_df[(birthdays_df.day == today_day) & (birthdays_df.month == today_month)]

birthday_list = birthday_to_send.to_dict(orient="records")
for birthday in birthday_list:
    letter_number = random.randint(1,3)
    letter_to_use = f"./letter_templates/letter_{letter_number}.txt"
    name = birthday["name"]
    with open(letter_to_use, "r") as letter:
        letter_to_send = letter.readlines()
        letter_to_send[0] = f"Dear {name},\n"
        letter_to_send = ''.join(letter_to_send)

    send_email(letter_to_send)
