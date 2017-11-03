from ez_graphics_09 import*
from ez_touchscreen_09 import*
from ez_network_09 import*
import time
clear_screen('white')
character = load_image('Right1.jpg')
character = resize_image(character,28,36)


set_color('black')
draw_rect(700,430,50,50)
draw_rect(750,430,50,50)
shoot = resize_image(load_image('shoot.jpg'),50,50)
up_icon = resize_image(load_image('up.jpg'),50,50)
right_icon = resize_image(load_image('right.jpg'),50,50)
left_icon = resize_image(load_image('left.jpg'),50,50)
draw_image(shoot,750,430)
draw_image(up_icon,700,430)
draw_image(right_icon,50,430)
draw_image(left_icon,0,430)
char_x = 100
char_y = 200
jumpclick = 10
last = None
shot_x = 0
shot_y = 0
shot = False
picnum = 0
pics_right = ['Right1.jpg','Right1.jpg','Right2.jpg','Right2.jpg']
pics_left  = ['Left1.jpg','Left1.jpg','Left2.jpg','Left2.jpg']
def move_shoot():
    global char_x,char_y,jumpclick,last,shot,shot_x,shot_y,character,picnum,pics_left,pics_right
    
    # read a single finger point from the touchscreen
    touch_points = touchscreen_finger_points_multitouch()
    for point in touch_points:
        # get the x and y coordinates of the touch
        x = point['x']
        y = point['y']
        
        if 700 < x < 750 and y > 430 and jumpclick > 39:
            jumpclick = 0
        if 750 < x < 800 and y > 430 and not shot:
            shot = True
            if last == 'left':
                shot_x = char_x
            if last == 'right':
                shot_x = char_x + 28
            shot_y = char_y + 18
        if y > 430:
            if x < 50:
                char_x = char_x - 5
                if picnum > 3:
                    picnum = 0
                if jumpclick > 25:
                    character_image = pics_left[picnum]
                    character = load_image(character_image)
                picnum = picnum + 1
                if not shot:
                    shot_x = None
                    last = 'left'
            if 50 < x < 100:
                char_x = char_x + 5
                if picnum > 3:
                    picnum = 0
                if jumpclick > 25:
                    character_image = pics_left[picnum]
                    character = load_image(character_image)
                picnum = picnum + 1
                if not shot:
                    shot_x = None
                    last = 'right'
    
    if shot:        
        if last == 'left':
            shot_x = shot_x - 5
            rocket = load_image('Rocket_Left.jpg')
        if last == 'right':
            shot_x = shot_x + 5
            rocket = load_image('Rocket_Right.jpg')
        if shot_x < 0 or shot_x > 800:
            shot = False
        if shot_y > 372:
            if shot_x < 200 or shot_x > 600:
                shot = False
        if not shot:
            exps = ['Exp1.jpg','Exp2.jpg','Exp3.jpg','Exp4.jpg','Exp5.jpg','Exp6.jpg']
            for i in exps:
                if last == 'left':
                    draw_image(load_image(i),shot_x - 20,shot_y - 13)
                if last == 'right':
                    draw_image(load_image(i),shot_x -20,shot_y - 13)
                time.sleep(.005)
            set_color('white')
            fill_rect(shot_x,shot_y,25,14)
            shot_x = None
        else:
            set_color('white')
            draw_image(rocket,shot_x,shot_y)
            fill_rect(shot_x + 21, shot_y,10,14)
            fill_rect(shot_x -10, shot_y,10,14)
    else:
        shot_x = None
        shot_y = None
    if jumpclick < 22:
        if last == 'left':
            character = load_image('jump_left.jpg')
        if last == 'right':
            character = load_image('jump_right.jpg')
        char_y = char_y - 5
        jumpclick = jumpclick + 1
        time.sleep(.002)
    
    
    set_color('black')
    fill_rect(100,436,600,44)
    fill_rect(0,386,196,44)
    fill_rect(600,386,200,44)
    fill_rect(100,400,96,80)
    fill_rect(600,400,100,80)
    set_color('white')
    if char_y < 399 and 200 < char_x < 565:
        if 400 - char_y < 36:
            fill_rect(char_x, char_y +36,28,400 - char_y)
        else:
            fill_rect(char_x, char_y +36,28,36)
    if char_x < 201 or char_x > 565:
        if char_y < 351:
            if 351 - char_y < 36:
                fill_rect(char_x, char_y +36,48,350 - char_y)
            else:
                fill_rect(char_x, char_y +36,48,36)
    if 195 < char_x < 220:
        fill_rect(200, char_y - 20, char_x - 200,20)
        fill_rect(200,char_y,char_x - 200,36)
    else:
        fill_rect(char_x - 20, char_y - 20, 48,20)
        fill_rect(char_x - 10 ,char_y,10,36)
    if 543 < char_x < 570:
        fill_rect(char_x + 28,char_y,600 - char_x - 28,36)
    else:
        fill_rect(char_x + 28,char_y,20,36)
        
    if char_y > 351:
        if char_x < 202:
            char_x = 201
        if char_x > 564:
            char_x = 564
    set_color('black')
    draw_image(character,char_x,char_y)
    char_y = char_y + 1
    time.sleep(.002)
    
    # boundries
    if char_y > 399 and 200 < char_x < 600:
        char_y = 400
        jumpclick = 40
    
    if char_x > 564 or char_x < 201:
        if char_y > 349:
            char_y = 350
            jumpclick = 40
        
sheep_xr = 0
sheep_y = 200

def opponent():
    global char_x,char_y,jumpclick,last,shot,shot_x,shot_y,character,picnum,pics_left,pics_right,shot_x,shot_y
    data = [char_x,char_y,character,shot_x,shot_y]
    netlink.send(data)
    r_data = None
    while r_data == None:
        r_data = netlink.pop_received_data
    [char_x,char_y,character,shot_x,shot_y] = r_data
    draw_image(load_image(character),char_x,char_y)
    if shot_x != None:
        draw_image(load_image('rocket_left.jpg'),shot_x,shot_y)
        
    


def sheep():
    global sheep_xr, sheep_y,char_x,char_y
    set_color('white')
    sheep_x = int(sheep_xr)
    fill_rect(sheep_x - 10, sheep_y,10,36)
    fill_rect(sheep_x-5,sheep_y-10,32,10)
    if sheep_y > 351:
        if sheep_x < 202:
            sheep_x = 201
        if sheep_x > 564:
            sheep_x = 564
    set_color('black')
    draw_image(load_image('Left1.jpg'),sheep_x,sheep_y)
    sheep_y = sheep_y + 1
    time.sleep(.002)
    
    # boundries
    if sheep_y > 399 and 200 < sheep_x < 600:
        sheep_y = 400
        jumpclick = 40
    
    if sheep_x > 564 or sheep_x < 201:
        if sheep_y > 349:
            sheep_y = 350
            jumpclick = 40
    sheep_xr = sheep_xr + .5
    if sheep_xr > 800:
        sheep_xr = 0
    time.sleep(.001)
    if sheep_x - 26 < char_x < sheep_x + 26 and sheep_y - 36 < char_y < sheep_y + 36:
        clear_screen('white')
        sheep_xr = 0
        sheep_y = 400
        shoot = resize_image(load_image('shoot.jpg'),50,50)
        up_icon = resize_image(load_image('up.jpg'),50,50)
        right_icon = resize_image(load_image('right.jpg'),50,50)
        left_icon = resize_image(load_image('left.jpg'),50,50)
        draw_image(shoot,750,430)
        draw_image(up_icon,700,430)
        draw_image(right_icon,50,430)
        draw_image(left_icon,0,430)
        move_shoot()
        sheep()
    if sheep_x - 26 < shot_x < sheep_x + 26 and sheep_y - 36 < shot_y < sheep_y + 36:
        shot = False
        exps = ['Exp1.jpg','Exp2.jpg','Exp3.jpg','Exp4.jpg','Exp5.jpg','Exp6.jpg','Exp7.jpg']
        for i in exps:
            if last == 'left':
                draw_image(load_image(i),shot_x - 20,shot_y - 13)
            if last == 'right':
                draw_image(load_image(i),shot_x -20,shot_y - 13)
            time.sleep(.005)
        clear_screen('white')
        sheep_xr = 0
        sheep_y = 200
        shoot = resize_image(load_image('shoot.jpg'),50,50)
        up_icon = resize_image(load_image('up.jpg'),50,50)
        right_icon = resize_image(load_image('right.jpg'),50,50)
        left_icon = resize_image(load_image('left.jpg'),50,50)
        draw_image(shoot,750,430)
        draw_image(up_icon,700,430)
        draw_image(right_icon,50,430)
        draw_image(left_icon,0,430)
        move_shoot()
        sheep()
        


while True:

    
    move_shoot()
#    opponent()
    sheep()
                
                
                
                