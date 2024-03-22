from modules import color
from modules import banner
import os
import platform


def exit_Android_cracker():
    global run_Android_cracker
    run_Android_cracker = False
    print("\nExiting...\n")


def display_menu():
    """Displays banner and menu"""
    print(selected_banner, page)


def clear_screen():
    """Clears the screen and display menu"""
    os.system(clear)
    display_menu()


def start():
    operating_system = platform.system()
    if operating_system == "Windows":
        windows_config()


def windows_config():
    global clear
    clear = "cls"


def change_page(name):
    global page, page_number, selected_banner
    if name == "p":
        if page_number > 0:
            page_number = page_number - 1
    elif name == "n":
        if page_number < 2:
            page_number = page_number + 1
    if page_number == 0:
        selected_banner = color.RED + banner.banner6
    elif page_number == 1:
        selected_banner = color.CYAN + banner.banner11
    elif page_number == 2:
        selected_banner = color.YELLOW + banner.banner2
    page = banner.menu[page_number]
    clear_screen()


def main():
    print(f"\n {color.CYAN}99 : Clear Screen                0 : Exit")
    option = input(f"\n{color.RED}[Main Menu] {color.WHITE}Enter selection > ").lower()
    match option:
        case "p":
            change_page("p")
        case "n":
            change_page("n")
        case "0":
            exit_Android_cracker()
        case "99":
            clear_screen()


clear = "clear"
page_number = 0
page = banner.menu[page_number]


selected_banner = color.RED + banner.banner6

start()
run_Android_cracker = True
if run_Android_cracker:
    clear_screen()
    while run_Android_cracker:
        try:
            main()
        except KeyboardInterrupt:
            exit_Android_cracker()
