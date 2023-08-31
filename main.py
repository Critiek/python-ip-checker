import PySimpleGUI as sg
import json
from api import greynoise_api

sg.theme('DarkPurple1')

# Define the window's contents
layout = [[sg.Text("Enter the IP adress:")],
          [sg.Input(size=(15), key='-IP-')],
          [sg.Text(key='-MESSAGE-')],
          [sg.Text(key='-NOISE-')],
          [sg.Text(key='-RIOT-')],
          [sg.Button('Check'), sg.Button('Quit')]]

# Create the window
window = sg.Window('IP Checker', layout, size=(500, 150), resizable=True, finalize=True)

keys_to_clear = ['-MESSAGE-', '-NOISE-', '-RIOT-']

# Display and interact with the Window using an Event Loop
while True:
  event, values = window.read()

  for key in keys_to_clear:
    window[key]('')

  # See if user wants to quit or window was closed
  if event == sg.WINDOW_CLOSED or event == 'Quit':
      break
  # Output a message to the window

  ip = values['-IP-']

  greynoise_api.get_response_from_greynoise(ip)

  with open('response.json') as response_file:
    response_data = response_file.read()
    ip_info = json.loads(response_data)

  window['-MESSAGE-'].update(ip_info['message'])

  if 'noise' in ip_info:
    window['-NOISE-'].update('Noise: ' + str(ip_info['noise']))
  if 'riot' in ip_info:
    window['-RIOT-'].update('Riot: ' + str(ip_info['riot']))

# Finish up by removing from the screen
window.close()