from pyowm import OWM

def input_city(city):

    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

    owm = OWM(API_KEY)
    mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details

    observation = mgr.weather_at_place(city)
    w = observation.weather
    temperature = w.temperature('celsius')['temp']
    wind = w.wind()['speed']

    result = f'Status: {w.detailed_status}\n'         # clouds
    result += f'Temp: {temperature} °C\n '             # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    result += f'Wind: {wind} km/h\n'                  # {'speed': 4.6, 'deg': 330}
    result += f'Humindity: {w.humidity}\n '           # 87


    label.config(text=result)

import tkinter as tk

def display():

    HEIGHT = 350
    WIDTH = 450

    root = tk.Tk()
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    root.title("Weather Application")
    canvas.pack()

    frame = tk.Frame(root, bg="deep sky blue", bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    entry_field = tk.Entry(frame, font=('Courier', 12))
    entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

    button = tk.Button(frame,
                       text="Get Weather",
                       bg="gray", fg="white",
                       font=('Courier', 8),
                       command=lambda: input_city(entry_field.get()))
    button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

    lower_frame = tk.Frame(root, bg='gold', bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    global label
    label = tk.Label(lower_frame, font=('Courier', 14))
    label.place(relx=0, rely=0, relwidth=1, relheight=1)

    root.mainloop()

display()