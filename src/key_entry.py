import PySimpleGUI as sg

sg.theme('DarkPurple1')

layout = [[sg.Text('No Greynoise API key detected! Please enter one to be saved:')], 
          [sg.Input(size=(15), key='-KEY-')],
          [sg.Button('Save'), sg.Button('Quit')]]


def create_entry_window(scaled_screen_width, scaled_screen_height):
    key_window = sg.Window('Key Entry', layout, size=(int(scaled_screen_width), int(scaled_screen_height)), resizable=True, finalize=True)
    while True:
        event, values = key_window.read()

        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            key_window.close()
            quit()

        if event == 'Save':
            with open('keys/greynoise_key.key', 'w') as file:
                file.write(values['-KEY-'])
            key_window.close()
            break
