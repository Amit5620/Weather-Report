from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

import requests
import os
from datetime import datetime

user_api = os.environ['current_weather_data']

def get_weather(location):
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    if api_data['cod'] == '404':
        return None
    else:
        #create variables to store and display data
        # print(api_data)
        city = api_data['name']
        country = api_data['sys']['country']
        # temp_city = ((api_data['main']['temp']) - 273.15)
        temp_cel = ((api_data['main']['temp']) - 273.15)
        temp_fer = ((api_data['main']['temp']))
        icon = api_data['weather'][0]['icon']
        # weather = api_data['weather'][0]['main']
        weather_desc = api_data['weather'][0]['description']
        # hmdt = api_data['main']['humidity']
        # wind_speed = api_data['wind']['speed']
        # date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        final_data = (city, country, temp_cel, temp_fer, icon, weather_desc)

    return final_data

def search():
    city = city_text.get()
    weather = get_weather(city)
    print(weather)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])

        # load and display image
        img = ImageTk.PhotoImage(Image.open('C:/Users/mamit/OneDrive/Desktop/code/Python Projects/Weather App/weather_icons/{}.png'.format(weather[4])))
        img_lbl.config(image=img)
        img_lbl.image = img

        temp_lbl['text'] = '{:.2f}°C , {:.2f}°F'.format(weather[2], weather[3])
        weather_lbl['text'] = weather[5]
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))

app = Tk()
app.title("Weather App")
app.geometry('400x300')

app.configure(bg='#BFACE2')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text="Search Weather", width=15, command=search)
search_btn.pack()

location_lbl = Label(app, text='', font=('bold', 20), bg='#BFACE2')
location_lbl.pack()


# create label for image
img_lbl = Label(app, bg='#BFACE2')
img_lbl.pack()

temp_lbl = Label(app, text='', bg='#BFACE2')
temp_lbl.pack()

weather_lbl = Label(app, text='', bg='#BFACE2')
weather_lbl.pack()

app.mainloop()