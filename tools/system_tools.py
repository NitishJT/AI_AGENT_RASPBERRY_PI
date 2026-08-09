import os
import subprocess
import platform


def get_system_info():

    system = platform.system()

    return f"Operating system: {system}"


def open_terminal():

    try:

        subprocess.Popen([
            "lxterminal"
        ])

        return "Opening terminal."

    except Exception as e:

        return f"Could not open terminal: {e}"


def open_browser():

    try:

        subprocess.Popen([
            "chromium-browser"
        ])

        return "Opening browser."

    except Exception as e:

        return f"Could not open browser: {e}"


def shutdown():

    os.system(
        "sudo shutdown -h now"
    )

    return "Shutting down the Raspberry Pi."


def reboot():

    os.system(
        "sudo reboot"
    )

    return "Restarting the Raspberry Pi."