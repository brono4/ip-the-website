import socket
from colorama import init, Fore, Style

# Initialize colorama
init()

# Print "BRONO" in red color with ASCII art style
print(Fore.RED + '''
BBBBB   RRRRR   OOOOO   N   N   OOOOO       FREE FILISTANE
B    B  R    R  O    O  NN  N  O     O      FREE FILISTANE
BBBBB   RRRRR   O    O  N N N  O     O      FREE FILISTANE
B    B  R   R   O    O  N  NN  O     O      FREE FILISTANE
BBBBB   R    R  OOOOO   N   N   OOOOO       FREE FILISTANE
''' + Style.RESET_ALL)

# Define green and red colors for specific text
green_text = Fore.GREEN
red_text = Fore.RED

# Prompt the user to enter a URL
a = input(green_text + "Enter the SUBDOMEN of the website: " + Style.RESET_ALL)

# Get the IP address of the entered URL
try:
    ip = socket.gethostbyname(a)
    print(green_text + "The IP address of " + a + " is " + ip + Style.RESET_ALL)
except socket.gaierror:
    print(red_text + "$Error: Invalid SUBDOMEN or unable to resolve the host.$must be without https/http like this ---->example.com$" + Style.RESET_ALL)
