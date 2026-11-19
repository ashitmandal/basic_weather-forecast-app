
import os
import platform
import socket
import sys
import datetime


def get_system_info():

    return {
        "Operating System": platform.system(),
        "OS Release": platform.release(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Processor": platform.processor() or "Not available",
        "CPU Logical Cores": os.cpu_count(),
        "Python Version": platform.python_version(),
        "Python Implementation": platform.python_implementation(),
        "Python Executable": sys.executable,
        "Hostname": socket.gethostname(),
        "Current User": os.getenv("USERNAME") or os.getenv("USER"),
        "Current Directory": os.getcwd(),
        "System Time": datetime.datetime.now().astimezone().isoformat(),
        "GitHub Actions": os.getenv("GITHUB_ACTIONS", "false"),
        "Runner OS": os.getenv("RUNNER_OS", "Local machine"),
        "Runner Name": os.getenv("RUNNER_NAME", "Local execution"),
    }


def print_system_info(info):

    print("\n")
    print("=" * 65)
    print("             SYSTEM INFORMATION REPORT")
    print("=" * 65)

    for category, value in info.items():
        print(f"{category:<28}: {value}")

    print("=" * 65)
    print("             SYSTEM REPORT COMPLETED")
    print("=" * 65)


def test_system_information():

    info = get_system_info()

    print_system_info(info)

    # Basic validation
    assert info["Operating System"] in ["Windows", "Linux", "Darwin"]
    assert info["Python Version"]
    assert info["Architecture"]
    assert info["CPU Logical Cores"] > 0
