import py5

def branch(branchLength: float) -> None:
    """Draw A Branch And Recursively Draw Two Smaller Rotated Branches."""
    if branchLength < 5:
        return  # Base Case: Stop Recursion When Branch Is Too Small

    # Draw The Main Branch
    py5.line(0, 0, 0, -branchLength)

    # Move To The End of This Branch
    py5.translate(0, -branchLength)

    # Save Current Transformation State
    py5.push_matrix()

    # Rotate Right And Draw A Smaller Branch
    py5.rotate(py5.radians(25))
    branch(branchLength * 0.67)

    # Restore State After Right Branch
    py5.pop_matrix()
    py5.push_matrix()

    # Rotate Left And Draw A Smaller Branch
    py5.rotate(py5.radians(-25))
    branch(branchLength * 0.67)

    # Restore State After Left Branch
    py5.pop_matrix()


def setup():
    # Set Up The Canvas
    py5.size(600, 600)
    py5.background(0)
    py5.stroke(255)
    py5.stroke_weight(2)

    # Move Origin To Bottom Center of The Canvas
    py5.translate(py5.width // 2, py5.height)

    # Draw The Initial Trunk Pointing Upward
    branch(100)

py5.run_sketch()