import PySimpleGUI as sg

sg.theme('DarkPurple1')

layout = [[sg.Text('No Greynoise API key detected! Please enter one to be saved:')], 
          [sg.Input(size=(15), key='-KEY-')],
          [sg.Button('Save'), sg.Button('Quit')]]


def create_entry_window(scaled_screen_width, scaled_screen_height):
    key_window = sg.Window('Key Entry', layout, size=(int(scaled_screen_width), int(scaled_screen_height)), resizable=True, finalize=True)

def test():
    print('test')
