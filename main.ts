let num = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    num += 1
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    num = 0
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    num += 0 - 1
})
basic.forever(function on_forever() {
    basic.clearScreen()
    basic.showNumber(num)
})
