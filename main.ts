function red_light_on() {
    if (lights_on) {
        strip.setPixelColor(2, neopixel.colors(NeoPixelColors.Red))
        strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Black))
        strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Black))
        strip.show()
    }
    
}

function traffic_lights_on() {
    while (lights_on) {
        red_light_on()
        basic.pause(2000)
        green_light_on()
        basic.pause(2000)
        yellow_light_on()
        basic.pause(0)
    }
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    lights_on = true
    traffic_lights_on()
})
function set_lights_to_black(first_led: number, last_led: number) {
    let lights = _py.range(first_led, last_led)
    for (let i of lights) {
        strip.setPixelColor(i, neopixel.colors(NeoPixelColors.Black))
    }
    strip.show()
}

function green_light_on() {
    if (lights_on) {
        strip.setPixelColor(2, neopixel.colors(NeoPixelColors.Black))
        strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Black))
        strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Green))
        strip.show()
    }
    
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    lights_on = false
    set_lights_to_black(0, 24)
    strip.show()
})
function set_lights_to_white(first_led2: number, last_led2: number) {
    let lights2 = _py.range(first_led2, last_led2)
    for (let j of lights2) {
        strip.setPixelColor(j, neopixel.colors(NeoPixelColors.White))
    }
    strip.show()
}

function yellow_light_on() {
    let blink: number;
    if (lights_on) {
        strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Yellow))
        strip.setPixelColor(2, neopixel.colors(NeoPixelColors.Black))
        strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Black))
        strip.show()
        basic.pause(500)
        blink = 4
        while (blink > 0) {
            strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Black))
            strip.show()
            basic.pause(500)
            strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Yellow))
            strip.show()
            basic.pause(500)
            blink = blink - 1
        }
    }
    
}

let lights_on = false
let strip : neopixel.Strip = null
basic.clearScreen()
strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
set_lights_to_black(0, 24)
lights_on = false
