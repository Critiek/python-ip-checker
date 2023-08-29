import pyglet
import greynoise_api

window = pyglet.window.Window()

response = greynoise_api.get_response_from_greynoise()

label = pyglet.text.Label('ashmongus',
                          font_name='Times New Roman',
                          font_size=11,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()

