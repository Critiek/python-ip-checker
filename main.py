import PySimpleGUI as sg
import json
from api import greynoise_api

# Define the window's contents
layout = [[sg.Text("Enter the IP adress:")],
          [sg.Input(key='-IP-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

 

# Display and interact with the Window using an Event Loop
while True:
  event, values = window.read()
  # See if user wants to quit or window was closed
  if event == sg.WINDOW_CLOSED or event == 'Quit':
      break
  # Output a message to the window

  ip = values['-IP-']

  greynoise_api.get_response_from_greynoise(ip)

  with open('response.json') as response_file:
    response_data = response_file.read()

  ip_info = json.loads(response_data)

  response_file.close()

  window['-OUTPUT-'].update(ip_info['message'])

# Finish up by removing from the screen
window.close()