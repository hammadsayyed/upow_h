import os
import subprocess
import platform
from decimal import Decimal


def select_binary_name():
    system = platform.system()
    machine = platform.machine()

    if system == 'Windows':
        if machine == 'AMD64' or machine == 'x86_64':
            return "decimal-windows-amd64.exe"
        else:
            return "decimal-windows-386.exe"
    elif system == 'Linux':
        if machine == 'x86_64':
            return "decimal-linux-amd64"
        elif machine == 'i386' or machine == 'i686':
            return "decimal-linux-386"
        elif machine.startswith('arm'):
            return "decimal-linux-arm"
        elif machine == 'aarch64':
            return "decimal-linux-arm64"
    elif system == 'Darwin':
        if machine == 'x86_64':
            return "decimal-macos-amd64"
        elif machine == 'arm64':
            return "decimal-macos-arm64"
    else:
        raise Exception("Unsupported platform")


def call_go_binary(operation, a, b):
    # current_directory = os.getcwd()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print('current_directory', script_dir)
    binary_name = select_binary_name()
    binary_path = os.path.join(script_dir, binary_name)
    print('binary_path', binary_path)
    command = [binary_path, operation, a, b]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        raise Exception(f"Error: {result.stderr}")


def accurate_division(a, b):
    if isinstance(a, int | float | Decimal):
        a = str(a)
    if isinstance(b, int | float | Decimal):
        b = str(b)
    result = call_go_binary("divide", a, b)
    return Decimal(result)


# startTime = time.time()
# res = call_go_binary("divide", "4.0", "2.0")
# res = accurate_division("4.0","2.0")
# res = accurate_division(8, Decimal("2.2"))
# print("Division:", res)
# print("type:", type(res))
