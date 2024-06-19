def red_light_on():
    if lights_on:
        strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.RED))
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.BLACK))
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLACK))
        strip.show()
def traffic_lights_on():
    while lights_on:
        red_light_on()
        basic.pause(2000)
        green_light_on()
        basic.pause(2000)
        yellow_light_on()
        basic.pause(0)

def on_button_pressed_a():
    global lights_on
    lights_on = True
    traffic_lights_on()
input.on_button_pressed(Button.A, on_button_pressed_a)

def set_lights_to_black(first_led: number, last_led: number):
    lights = range(first_led, last_led)
    for i in lights:
        strip.set_pixel_color(i, neopixel.colors(NeoPixelColors.BLACK))
    strip.show()
def green_light_on():
    if lights_on:
        strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.BLACK))
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.BLACK))
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.GREEN))
        strip.show()

def on_button_pressed_b():
    global lights_on
    lights_on = False
    set_lights_to_black(0, 24)
    strip.show()
input.on_button_pressed(Button.B, on_button_pressed_b)

def set_lights_to_white(first_led2: number, last_led2: number):
    lights2 = range(first_led2, last_led2)
    for j in lights2:
        strip.set_pixel_color(j, neopixel.colors(NeoPixelColors.WHITE))
    strip.show()
def yellow_light_on():
    if lights_on:
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.YELLOW))
        strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.BLACK))
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLACK))
        strip.show()
        basic.pause(500)
        blink = 4
        while blink > 0:
            strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.BLACK))
            strip.show()
            basic.pause(500)
            strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.YELLOW))
            strip.show()
            basic.pause(500)
            blink = blink - 1
lights_on = False
strip: neopixel.Strip = None
basic.clear_screen()
strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
set_lights_to_black(0, 24)
lights_on = False