import py5
import random

# Initialize Starting Point Coordinates
x, y = 0, 0

def setup():
    # Setup Canvas Size And Background Color
    py5.size(600, 800)
    py5.background(0)

    # Disable Stroke And Set Fill Color To Bright Green
    py5.no_stroke()
    py5.fill(0, 255, 0)

    # Translate Origin To Bottom Center Of The Canvas
    py5.translate(py5.width / 2, py5.height)

    # Define Scaling Factors For Drawing The Fern
    scaleX = 60
    scaleY = 60

    global x, y

    # Iterate 100000 Times To Draw Points Of Barnsley Fern
    for _ in range(100000):
        # Generate A Random Number Between 0 And 1
        randomNumber = random.random()

        # Apply Barnsley Fern Transformation Rules Based On Random Number
        if randomNumber < 0.01:
            xNew = 0
            yNew = 0.16 * y
        elif randomNumber < 0.86:
            xNew = 0.85 * x + 0.04 * y
            yNew = -0.04 * x + 0.85 * y + 1.6
        elif randomNumber < 0.93:
            xNew = 0.2 * x - 0.26 * y
            yNew = 0.23 * x + 0.22 * y + 1.6
        else:
            xNew = -0.15 * x + 0.28 * y
            yNew = 0.26 * x + 0.24 * y + 0.44

        # Update Coordinates For Next Iteration
        x, y = xNew, yNew

        # Draw A Tiny Ellipse At The New Coordinates (Scaled And Y Inverted)
        py5.ellipse(x * scaleX, -y * scaleY, 1, 1)

    # Stop The Draw Loop Since We Rendered All Points
    py5.no_loop()

# Run The Sketch
py5.run_sketch()
