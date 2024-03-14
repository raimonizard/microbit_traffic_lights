def red_light_on():
    if lights_on:
        strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.RED))
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.BLACK))
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLACK))
        strip.show()
        basic.pause(2000)

def traffic_lights_on():
    while lights_on:
        basic.show_number(input.light_level())
            if input.light_level() < 100:
                set_lights_to_white(3, 255)
        basic.clear_screen()
        red_light_on()
        yellow_light_on()
        green_light_on()
        set_lights_to_black(0, 24)
        strip.show()

def on_button_pressed_a():
    global lights_on
    basic.clear_screen()
    lights_on = True
    traffic_lights_on()
input.on_button_pressed(Button.A, on_button_pressed_a)

def set_lights_to_black(first_led: number, last_led: number):
    lights = range(first_led, last_led)
    for i in lights:
        strip.set_pixel_color(i, neopixel.colors(NeoPixelColors.BLACK))
    strip.show()

def set_lights_to_white(first_led: number, last_led: number):
    lights = range(first_led, last_led)
    for i in lights:
        strip.set_pixel_color(i, neopixel.colors(NeoPixelColors.WHITE))
    strip.show()

def green_light_on():
    if lights_on:
        strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.BLACK))
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.BLACK))
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.GREEN))
        strip.show()
        basic.pause(2000)

def on_button_pressed_b():
    global lights_on
    lights_on = False
    set_lights_to_black(0, 24)
    strip.show()
input.on_button_pressed(Button.B, on_button_pressed_b)

def yellow_light_on():
    if lights_on:
        strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.BLACK))
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLACK))
        blink = 4
        while blink > 0:
            strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.YELLOW))
            strip.show()
            basic.pause(500)
            strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.BLACK))
            strip.show()
            blink = blink - 1
        basic.pause(2000)


lights_on = False
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
set_lights_to_black(0, 24)