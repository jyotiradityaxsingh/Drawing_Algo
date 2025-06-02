import py5
import math

dotCount = 0       # Keeps Track Of Number of Dots Placed
dotSpacing = 4     # Controls Spacing Between Dots

def setup():
    py5.size(600, 600)                     # Set Canvas Size
    py5.background(0)                      # Set Background To Black
    py5.color_mode(py5.HSB, 255)           # Use HSB Color Mode For Colorful Effect
    py5.no_stroke()                        # Disable Stroke For Clean Circles
    py5.frame_rate(60)                     

def draw():
    global dotCount

    golden_angle = 137.508                 # More Accurate Golden Angle
    radius = dotSpacing * math.sqrt(dotCount)
    angle = math.radians(dotCount * golden_angle)

    x = radius * math.cos(angle) + py5.width / 2
    y = radius * math.sin(angle) + py5.height / 2

    py5.fill(dotCount % 255, 255, 255)     # Set Fill Color Based On Dot Count
    py5.ellipse(x, y, 6, 6)                # Draw A Dot

    dotCount += 1                          # Increment The Dot Counter

    if radius > py5.width / 2:
        py5.no_loop()                      # Stop Drawing When Dots Reach Canvas Edge

# Required To Run The Sketch
py5.run_sketch()
