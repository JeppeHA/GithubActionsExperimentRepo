import requests
from dotenv import find_dotenv, load_dotenv
import os
import smtplib

def get_posts():
    env_path = find_dotenv()
    load_dotenv(env_path)
    API_KEY = os.getenv("API_KEY")
    CITY_NAME = "Odense"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print("Error:", response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


def main():
    send_email()


def send_email():
    posts = get_posts()
    email = "jeppe.holmandersen@gmail.com"
    subject = "Weather forecast"
    message = f"The weather is {posts['weather'][0]['main']} and {round(posts['main']['temp'] - 273)} degrees Celsius"
    text = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, os.getenv("APP_PASSWORD"))
    server.sendmail(email, email, text)
    server.quit()
    print("Email sent!")


if __name__ == "__main__":
    main()