import string
import random

# Banner and ASCII art logo
banner = """

⠀⠀⠀⠀⠀⠀⢠⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⢹⠀⠀⠀⠀⢠⣺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣼⡀⠀⣀⣤⣶⡴⠒⠒⠒⠒⠒⠠⣤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣃⣗⣿⠇⣿⣧⡃⠀⠀⠀⠀⠀⠀⠀⠹⣾⠱⠤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡰⠋⢸⢾⣿⢣⣿⣿⠷⣄⡒⢤⣀⣀⠀⢐⢀⠀⠦⠀⠉⢕⢄⠀⠀⠀⠀
⠀⠀⠀⡠⣎⣃⠀⠀⢟⣽⢸⣿⣿⡀⠱⣷⡾⣡⣦⣝⡀⠉⠘⠃⠠⠄⠀⢈⣧⡀⠀⠀
⠀⠀⠰⠁⢸⡟⠲⠀⢘⣜⣿⣿⡟⣉⣣⣼⣷⣻⣯⣙⣿⣿⣶⣶⣦⣴⣶⡿⠋⠱⡀⠀
⠀⠀⡸⠀⡀⠀⠀⠀⠠⡽⢟⣵⣾⣿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠱⠀
⠀⡇⡃⠀⢁⡀⠀⠀⠠⠷⢟⣿⣵⣶⣶⣇⣿⣿⣿⣟⣛⣛⠻⣯⠀⠀⠀⠀⠀⠀⠀⡇
⠀⢿⡃⠀⠈⠈⠀⠀⠀⠀⠃⢌⣿⣿⣿⣾⣿⣎⣋⣴⣶⣯⣿⣿⡆⠀⠀⠀⠀⠀⢠⢰
⢠⠸⢋⡀⡀⢀⣴⣮⠀⢀⡀⠀⣴⡿⠻⠘⠛⡟⡿⡬⢧⢊⡩⢿⣷⡀⠀⠀⠀⠀⠫⡞
⠘⣇⣇⢟⢶⠟⡉⠀⠀⠀⠁⣰⠊⢀⡀⣄⡰⣱⡷⡗⣭⢄⣐⠙⢿⡂⠠⠿⠇⠀⢀⡇
⠀⢟⡵⠈⣵⠀⠀⠀⠀⠀⠀⣷⢜⠊⣭⡴⢁⣽⡷⡖⣪⠴⢆⣉⣿⡇⠀⠀⠀⠘⡺⠀
⠀⠘⡜⣧⠘⠃⠀⠀⡐⠀⡼⡝⣮⣩⢴⣈⣿⣽⡇⡇⢼⠒⠬⣘⣿⡇⠀⠀⠀⣰⡅⠀
⠀⠀⠘⢌⢷⡔⠦⢀⣈⢠⡓⣭⣰⡴⣽⡽⢿⠍⡿⠏⠇⠒⠡⣽⣟⡅⠀⠀⣼⡟⠀⠀
⠀⠀⠀⠈⠢⣸⣾⣿⠟⣹⣭⣾⠷⣛⢭⣻⣿⣿⣷⣶⣴⣦⣬⣼⣿⣆⠈⡠⠊⠀⠀⠀
⠀⠀⠀⠀⣀⣈⣫⡼⡿⣟⢬⡢⣝⣮⣵⣿⣿⣿⣿⣿⣿⣿⣷⡉⠻⡧⠊⠁⠀⠀⠀⠀
⠀⠀⢠⢖⢧⣛⣛⣛⣾⣾⣷⡿⣟⣋⣽⣿⣿⣿⣿⣿⣯⣿⠼⠓⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⠿⢼⣸⡽⠿⠿⢯⣯⣻⣘⣯⡟⢿⣿⢿⣿⣿⣷⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⡭⣿⣿⣿⣿⣿⣿⣯⣾⣟⡋⡓⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡌⢀⣀⠘⠳⠙⣽⣿⣿⣿⣧⣋⣙⢾⡷⠦⡄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⠉⠈⠃⠿⠟⠉⢹⠟⠛⠻⡞⠿⠏⠀⠘⠄⠀⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        

Password Generator v1.0
Author: Ako
"""

print(banner)

def wp_generate_password(length=8, special_chars=True, extra_special_chars=False):
    """
    This method generates a password of a specified length and with or without special characters.
    
    :param length: The length of the password to generate (default=8)
    :type length: int
    :param special_chars: Whether to include standard special characters in the password (default=True)
    :type special_chars: bool
    :param extra_special_chars: Whether to include other special characters in the password (default=False)
    :type extra_special_chars: bool
    :return: The generated password
    :rtype: str
    """

    # All possible characters to include in the password
    chars = string.ascii_letters + string.digits
    
    # Add special characters if specified
    if special_chars:
        chars += '!@#$%^&*()'
    if extra_special_chars:
        chars += '-_ []{}<>~`+=,.;:/?|'

    # Generate the password by selecting random characters from the possible characters
    password = ''.join(random.choice(chars) for i in range(length))
    
    return password

try:
    n = int(input("Enter the number of passwords you want to generate: "))
    min_length = int(input("Enter the minimum length for the password (default=8): ") or 8)
    max_length = int(input("Enter the maximum length for the password (default=8): ") or 8)
    extra_special = input("Do you want to include extra special characters in the password (y/n)? (default=n) ").lower() == 'y'
except ValueError:
    print("Invalid input. Exiting program.")
    exit()
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting.")
	
try:
    passwords = {wp_generate_password(length=random.randint(min_length, max_length), extra_special_chars=extra_special) for i in range(n)}

    with open("passwords.txt", "w") as f:
        for password in passwords:
            f.write(password + "\n")

    print("Passwords generated and written to passwords.txt")
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting.")
except:
    exit()

