# --------------------------------------------------
# network_server.py
# --------------------------------------------------
 
# import the libraries
from ez_graphics_09 import *
from ez_network_09 import *
import random
import time
 
# handler for new data that is received
def on_data_received(networklink):
    data = networklink.pop_received_data()
    set_color('black')
    fill_rect(100, 100, 200, 20)
    set_color('white')
    draw_text(str(data), 100, 100)
    
# clear the screen
clear_screen('black')

# create a new network link
netlink = create_networklink()
print netlink.conection
netlink.on_data_received_handler=on_data_received
 
# wait for a connection
set_color('white')
draw_text('Waiting for connection', 100, 100)
netlink.listen_for_connection()
 
# start sending random numbers
while True:
    print 'asdf'
    time.sleep(1)    