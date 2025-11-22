import requests
from dotenv import find_dotenv, load_dotenv
import os

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
    posts = get_posts()
    print(posts)
    print("Weather:")
    print(posts["weather"][0]["main"])
    print("Temperature:")
    print(round(posts["main"]["temp"] - 273))
    print("Wind speed:")
    print(posts["wind"]["speed"])




if __name__ == "__main__":
    main()