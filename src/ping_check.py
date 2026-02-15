import platform
import subprocess

def ping(ip: str, timeout_ms: int = 1000) -> bool:
    """
    Returns True if host responds to ping, else False.
    Cross-platform implementation for Windows/Linux/macOS.
    """
    system = platform.system().lower()

    if system == "windows":
        # -n 1: one echo request
        # -w timeout in milliseconds
        cmd = ["ping", "-n", "1", "-w", str(timeout_ms), ip]
    else:
        # -c 1: one packet
        # -W timeout in seconds (Linux), macOS uses -W in ms differently
        # We keep it simple: use -c and rely on default timeout behavior
        cmd = ["ping", "-c", "1", ip]

    try:
        result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return result.returncode == 0
    except Exception:
        return False

