# We need 3 package
# 1: tkinter for UI
# 2: Request for the Jason file
# 3: Time for the variable formatting

import tkinter as tk
import requests
import time

# Function to get the data from API
def getWeather(canvas):
    city = textfield.get()

    # getting api for the weather
    api = api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=6279d9d4b9951e19d8bc0897ae2baf07"
    json_data = requests.get(api).json()

    # accessing by using index 0
    condition = json_data['weather '][0]['main']

    # For the temperature and subtracting to make Celsius
    temp = int(json_data['main']['temp'] - 273.15)

    # Extracting min and max temperature
    temp = int(json_data['main']['temp_min'] - 273.15)
    temp = int(json_data['main']['temp_max'] - 273.15)

    # Air wind pressure and humidity
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    # sunrise and sunset: 21600 are the second to subtract to get the accurate data
    sunrise = time.strftime(" %H: %M: %S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime(" %H: %M: %S", time.gmtime(json_data['sys']['sunset'] - 21600))

    # String will get data to show the current data in big fonts and other data in short forms
    final_info = condition + "\n" + str(temp) + "C"
    final_data = "\n" + "Max Temp:" + str(max_temp) + "\n" + "Min Temp: " +str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity:" + str(humidity) + "\n " + "wind speed: " + str(wind) + "\n" + "Sunrise:" + sunrise +" \n" + "Sunset:"+ sunset
    label1.config(text = final_info)
    label2.config(text  =final_data)

# Defining UI
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Quick weather update")

f = ("Poppins", 15, "bold")
t = ("Poppins", 35, "bold")

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)

# User can defined the city or country name directly
textfield.focus()

# Loading the entered the city
textfield.bind('<Return>', getWeather)

# Showing the result
label1 = tk.Label(canvas, font=t)
label1.pack()

label2 = tk.Label(canvas, font=f)
label2.pack()





