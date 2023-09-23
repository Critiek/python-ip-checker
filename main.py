import PySimpleGUI as sg
import json
from api.greynoise import greynoise_api

sg.theme('DarkPurple1')

screen_scale_width = 3
screen_scale_height = 3

def get_screen_resolution():
  root = sg.tk.Tk()
  # Get the screen size
  width = root.winfo_screenwidth()
  height = root.winfo_screenheight()
  # Print the screen size
  print("The screen size is {}x{} \nThe scaled size will be {}x{}".format(width, height, int(width/screen_scale_width), int(height/screen_scale_height)))
  # Close the Tkinter window
  root.destroy()
  return (width, height)

(screen_width, screen_height) = get_screen_resolution()

screen_scale_width = 3
screen_scale_height = 3

# Define the window's contents
layout = [[sg.Text("Enter the IP adress:")], 
          [sg.Input(size=(15), key='-IP-')],
          [sg.Text(key='-MESSAGE-')],
          [sg.Text(key='-NOISE-'), sg.Text(key='-CLASSIFICATION-')],
          [sg.Text(key='-RIOT-'), sg.Text(key="-LASTSEEN-")],
          [sg.Button('Check'), sg.Button('Quit')]]

# Create the window
window = sg.Window('IP Checker', layout, size=(int(screen_width/screen_scale_width), int(screen_height/screen_scale_height)), resizable=True, finalize=True)

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
  if 'classification' in ip_info:
    window['-CLASSIFICATION-'].update('Classification: ' + str(ip_info['classification']))
  if 'last_seen' in ip_info:
    window['-LASTSEEN-'].update('Last Seen: ' + str(ip_info['last_seen']))

# Finish up by removing from the screen
window.close()
