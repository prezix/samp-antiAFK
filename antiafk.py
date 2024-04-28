# Import necessary libraries
import time
import random
import win32gui  # Import library for interacting with Windows GUI
import win32api  # Import library for simulating mouse and keyboard input
import win32con  # Import constants for Windows API
from colorama import init, Fore, Style

# Initialize colorama
init()


# Function to bring GTA SA-MP window to the foreground
def bring_gta_samp_to_foreground():
    # Find the handle of the GTA SA-MP window
    gta_samp_window = win32gui.FindWindow(None, "GTA:SA:MP")

    # Check if the window handle is valid
    if gta_samp_window != 0:
        # Bring the window to the foreground
        win32gui.ShowWindow(gta_samp_window, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(gta_samp_window)


# Function to check if GTA San Andreas window is active
def is_gta_sa_active():
    # Get the handle of the foreground window
    foreground_window = win32gui.GetForegroundWindow()

    # Get the title of the foreground window
    window_title = win32gui.GetWindowText(foreground_window)

    # Check if the window title contains "GTA: San Andreas"
    return "GTA:SA:MP" in window_title


# Function to simulate human-like activity
def simulate_human_activity():
    # Start time of the script
    start_time = time.time()
    # Set the duration for the script to run (2 hours)
    script_duration = 2 * 60 * 60  # 2 hours in seconds

    # Infinite loop to simulate human-like activity
    while time.time() - start_time < script_duration:
        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # Convert elapsed time to hours, minutes, and seconds
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)

        # Format the elapsed time string (in red)
        elapsed_time_str = f"{Fore.RED}{hours:02d}:{minutes:02d}:{seconds:02d}{Style.RESET_ALL}"

        # Print the elapsed time
        print(f"Elapsed time: {elapsed_time_str}")

        # Bring GTA SA-MP window to the foreground
        bring_gta_samp_to_foreground()

        # Check if GTA San Andreas window is active
        if is_gta_sa_active():
            # Simulate random key press
            key = random.choice([win32con.VK_UP, win32con.VK_DOWN, win32con.VK_LEFT, win32con.VK_RIGHT])

            # Press the selected key
            win32api.keybd_event(key, 0, 0, 0)

            # Simulate key press for 2 seconds
            time.sleep(2)

            # Release the pressed key
            win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)

            # Simulate mouse movement (rotation)
            # Generate random mouse movement coordinates
            mouse_x = random.randint(-10, 10)
            mouse_y = random.randint(-10, 10)

            # Move the mouse
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, mouse_x, mouse_y, 0, 0)

            # Format the action message (in blue)
            action_message = f"{Fore.BLUE}Simulating: Key press {key}, Mouse rotation ({mouse_x}, {mouse_y}){Style.RESET_ALL}"

            # Print the simulated action
            print(action_message)
        else:
            # Print a message indicating that GTA San Andreas window is not active
            print("GTA San Andreas window is not active. Script paused.")
            # Pause script execution for 5 seconds before checking again
            time.sleep(5)

    # Print a message indicating successful completion of the script
    print(f"{Fore.GREEN}Script has successfully completed its 2-hour duration.{Style.RESET_ALL}")


# Main function to execute the human emulator script
def main():
    # Call the function to simulate human-like activity
    simulate_human_activity()


# Check if the script is executed directly
if __name__ == "__main__":
    # Call the main function
    main()
