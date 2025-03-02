#Color Fading Across the Strip (Each LED smoothly fades into the next color)
import time
from opineo import OPiNeo

def color_fade(neo, colors, delay=0.02):
    steps = 100  # Smoothness of the fade
    num_leds = neo.num_leds
    num_colors = len(colors)

    while True:
        for i in range(num_colors):
            next_color = colors[(i + 1) % num_colors]
            # Transition from current color to next color in steps
            for step in range(steps):
                for led in range(num_leds):
                    color = tuple(
                        int(colors[i][c] + ((next_color[c] - colors[i][c]) * (step / steps)))
                        for c in range(3)
                    )
                    neo.set_led_color(led, *color)
                neo.update_strip()
                time.sleep(delay)

# Initialize OPiNeo with 10 LEDs
neo = OPiNeo('/dev/spidev1.1', 10, 800)

# Smooth fade through red, green, and blue
color_fade(neo, [(255, 0, 0), (0, 255, 0), (0, 0, 255)])
