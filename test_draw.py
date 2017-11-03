from ez_graphics_09 import*
import time
clear_screen('white')

buffer_image = capture_image(0,0,800,480)
set_drawing_image(buffer_image)

draw_image(load_image('Exp6.jpg'),100,100)
time.sleep(2)

set_drawing_image(None)
draw_image(buffer_image,0,0)

draw_image(load_image('Exp6.jpg'),700,100)
time.sleep(2)

set_drawing_image(None)
draw_image(buffer_image,0,0)
