from ez_graphics_09 import*
from ez_touchscreen_09 import*
from ez_network_09 import*
import time,random
# handler for new data that is received
def on_data_received(networklink):
    opponent()
    
# clear the screen
clear_screen('black')
 
# create a new network link
netlink = create_networklink()
 
# wait for a connection
set_color('white')
draw_text('Waiting for connection', 100, 100)
netlink.listen_for_connection()
while True:
    try:
        netlink.send('stuff')
    except:
        pass
    else:
        break


    
character = load_image('Right1.jpg')
character = resize_image(character,28,36)
shoot = resize_image(load_image('shoot.jpg'),50,50)
up_icon = resize_image(load_image('up.jpg'),50,50)
right_icon = resize_image(load_image('right.jpg'),50,50)
left_icon = resize_image(load_image('left.jpg'),50,50)
def set_up():
    clear_screen('white')
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

set_up()
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
character_image = 'Left1.jpg'
def move_shoot():
    global char_x,char_y,jumpclick,last,shot,shot_x,shot_y,character,picnum,pics_left,pics_right,character_image
    
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
                    character_image = pics_right[picnum]
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
        if char_y > 350:
            char_y = 350
            jumpclick = 40
    


def opponent():
    global char_x,char_y,jumpclick,last,shot,shot_x,shot_y,character,picnum,pics_left,pics_right,shot_x,shot_y
    data = [char_x,char_y,character_image,shot_x,shot_y]
    netlink.send(data)
    r_data = netlink.pop_received_data()
    if r_data != None and r_data!= 'stuff' :
        if r_data == 'you_win':
            clear_screen('black')
            set_color('white')
            draw_text('YOU WIN',390,230)
            set_up()
            move_shoot()
        if len(r_data) == 5:
            char_x2= r_data[0]
            char_y2= r_data[1]
            character_image2= r_data[2]
            shot_x2= r_data[3]
            shot_y2 = r_data[4]
            set_color('white')
            if char_y2 < 399 and 200 < char_x2 < 565:
                if 400 - char_y2 < 36:
                    fill_rect(char_x2, char_y2 +36,28,400 - char_y2)
                else:
                    fill_rect(char_x2, char_y2 +36,28,36)
            if char_x2 < 201 or char_x2 > 565:
                if char_y2 < 351:
                    if 351 - char_y2 < 36:
                        fill_rect(char_x2, char_y2 +36,48,350 - char_y2)
                    else:
                        fill_rect(char_x2, char_y2 +36,48,36)
            if 195 < char_x2 < 220:
                fill_rect(200, char_y2 - 20, char_x2 - 200,20)
                fill_rect(200,char_y2,char_x2 - 200,36)
            else:
                fill_rect(char_x2 - 20, char_y2 - 20, 48,20)
                fill_rect(char_x2 - 10 ,char_y2,10,36)
            if 543 < char_x2 < 570:
                fill_rect(char_x2 + 28,char_y2,600 - char_x2 - 28,36)
            else:
                fill_rect(char_x2 + 28,char_y2,20,36)
                
        
            draw_image(load_image(character_image2),char_x2,char_y2)
            if shot_x2 != None:
                draw_image(load_image('Rocket_Left.jpg'),shot_x2,shot_y2)
            
            if shot_x2 != None:
                if shot_x2 - 10 < char_x < shot_x2 + 20 and shot_y2 - 20 < char_y < shot_y2 + 20:
                    clear_screen('black')
                    set_color('white')
                    draw_text('YOU LOSE',390,470)
                    time.sleep(2)
                    r_data = None
                    char_x = 100
                    char_y = 200
                    netlink.send('you_win')
                    set_up()
                    move_shoot()

while True:
    move_shoot()
    opponent()
            