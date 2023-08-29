import pyglet
import json
from api import greynoise_api

window = pyglet.window.Window()

greynoise_api.get_response_from_greynoise()

with open('response.json') as response_file:
  response_data = response_file.read()

ip_info = json.loads(response_data)

response_file.close()

label = pyglet.text.Label(ip_info["message"],
                          font_name='Arial',
                          font_size=16,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()

