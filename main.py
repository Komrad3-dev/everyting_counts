num = 0

def on_button_pressed_a():
    global num
    num += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global num
    num = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global num
    num += 0 - 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.clear_screen()
    basic.show_number(num)
basic.forever(on_forever)
