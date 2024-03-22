"""
Script : 
Author : Tusshar Gurav (so called Mr.Hacker )
"""

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'




from modules import color

version = "v0"

menu1 = f"""

    {color.WHITE}1. {color.GREEN}Access Device Shell          {color.WHITE}6. {color.GREEN}Get Screenshot                       {color.WHITE}11. {color.GREEN}Install an APK  
    {color.WHITE}2. {color.GREEN}List Connected Devices       {color.WHITE}7. {color.GREEN}Screen Record                        {color.WHITE}12. {color.GREEN}Uninstall an App
    {color.WHITE}3. {color.GREEN}Disconnect All Devices       {color.WHITE}8. {color.GREEN}Download File/Folder from Device     {color.WHITE}13. {color.GREEN}List Installed Apps 
    {color.WHITE}4. {color.GREEN}Scan Network for Devices     {color.WHITE}9. {color.GREEN}Send File/Folder to Device           {color.WHITE}14. {color.GREEN}Connect a Device
    {color.WHITE}5. {color.GREEN}Mirror & Control Device     {color.WHITE}10. {color.GREEN}Run an App                           {color.WHITE}15. {color.GREEN}Hack Device {color.RED}(Using Metasploit)
    {color.WHITE}16. {color.GREEN}List All Folders/Files      {color.WHITE}21. {color.GREEN}Anonymous Screenshot                {color.WHITE}26. {color.GREEN}Play a Video on Device
    {color.WHITE}17. {color.GREEN}Send SMS                    {color.WHITE}22. {color.GREEN}Anonymous Screen Record             {color.WHITE}27. {color.GREEN}Get Device Information
    {color.WHITE}18. {color.GREEN}Copy WhatsApp Data          {color.WHITE}23. {color.GREEN}Open a Link on Device               {color.WHITE}28. {color.GREEN}Get Battery Information
    {color.WHITE}19. {color.GREEN}Copy All Screenshots        {color.WHITE}24. {color.GREEN}Display a Photo on Device           {color.WHITE}29. {color.GREEN}Restart Device
    {color.WHITE}20. {color.GREEN}Copy All Camera Photos      {color.WHITE}25. {color.GREEN}Play an Audio on Device             {color.WHITE}30. {color.GREEN}Advanced Reboot Options
    {color.WHITE}31. {color.GREEN}Unlock Device               {color.WHITE}36. {color.GREEN}Extract APK from Installed App      {color.WHITE}41. {color.GREEN}Record Mic Audio
    {color.WHITE}32. {color.GREEN}Lock Device                 {color.WHITE}37. {color.GREEN}Stop ADB Server                     {color.WHITE}42. {color.GREEN}Listen Device Audio
    {color.WHITE}33. {color.GREEN}Dump All SMS                {color.WHITE}38. {color.GREEN}Power Off Device                    {color.WHITE}43. {color.GREEN}Record Device Audio
    {color.WHITE}34. {color.GREEN}Dump All Contacts           {color.WHITE}39. {color.GREEN}Use Keycodes (Control Device)       {color.WHITE}44. {color.GREEN}Update Android_cracker
    {color.WHITE}35. {color.GREEN}Dump Call Logs              {color.WHITE}40. {color.GREEN}Listen Mic Audio                    {color.WHITE}45. {color.GREEN}Visit Android_cracker on GitHub


   {color.YELLOW} 
  """

menu = menu1

instruction = f"""

This attack will launch Metasploit-Framework    (msfconsole)

Use 'Ctrl + C' to stop at any point

1. Wait until you see:
    
    {color.GREEN}meterpreter >      {color.WHITE}

2. Then use 'help' command to see all meterpreter commands:

    {color.GREEN}meterpreter > {color.YELLOW}help       {color.WHITE}

3. To exit meterpreter enter 'exit' or To exit Metasploit enter 'exit -y':

    {color.GREEN}meterpreter > {color.YELLOW}exit       {color.WHITE}

    {color.GREEN}msf6 > {color.YELLOW}exit -y       {color.WHITE}
     
{color.RED}[Shiv]   {color.WHITE}Press 'Enter' to continue attack / '0' to Go Back to Main Menu
    """

head = E+H+"""
                        ```````````````````¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶```````````````````
                        ```````````````¶¶¶`````````````````¶¶¶```````````````
                        ````````````¶¶````````````````````````¶¶¶````````````
                        ```````````¶¶````````````````````````````¶¶```````````
                        `````````¶¶````````````````````````````````¶`````````
                        ````````¶¶`````````"""+W+'Android Hacking'+E+H+"""````````¶¶````````
                        ````````¶```````````"""+F+'TUSSHAR GURAV'+H+"""```````````¶¶````````
                        ```````¶¶```````````````````````````````````¶¶```````
                        ```````¶`````````````````````````````````````¶```````
                        ```````¶`````````````````````````````````````¶```````
                        ```````¶`````````````````````````````````````¶```````
                        ```````¶¶```````````````````````````````````¶¶```````
                        ```````¶¶``````¶¶¶¶¶````````````¶¶¶¶¶```````¶¶```````
                        ````````¶`¶``¶¶¶¶¶¶¶¶¶````````¶¶¶¶¶¶¶¶¶`````¶¶````````
                        ````````¶¶``¶¶"""+F+'Har Har'+H+"""¶¶¶``````¶¶¶"""+F+'Mahadev'+H+"""¶¶``¶¶¶````````
                        ````````¶¶``¶¶¶¶¶¶¶¶¶¶````````¶¶¶¶¶¶¶¶¶¶``¶¶````````
                        ````````¶`````¶¶¶¶```````````````¶¶¶¶¶`````¶¶`````
                        `````¶¶`¶¶``````````````¶`¶````````````````¶¶````````
                        ```¶¶```¶¶¶¶```````````¶¶`¶¶```````````````¶¶¶``¶¶```
                        ``¶¶`````¶`¶¶¶¶¶¶¶````````¶````````¶¶¶¶¶¶¶¶¶`````¶¶``
                        ```¶``````¶¶````¶¶````````````````¶``````¶¶`````¶¶```
                        ``¶¶````````¶¶¶`¶¶¶`¶`¶``¶``¶``¶``¶````¶¶```````¶¶``
                        ```¶¶¶``¶``````¶¶¶¶``````¶`````¶¶¶`¶¶¶``````````¶```
                        ``````````¶¶¶¶¶````¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶`````¶¶¶¶¶¶¶¶``````````
                        ```````````````¶¶¶````¶¶¶"""+W+'The'+H+"""¶¶`````¶¶¶¶```````````````
                        ``````````````````¶¶¶`"""+W+'Hacking'+H+"""``¶¶¶``````````````````
                        ````````````````````¶¶¶``````¶¶¶¶````````````````````¶
                        ````````````````¶¶¶`````¶¶¶¶¶````¶¶````````````````
                        ```````````¶```````¶¶¶¶``````¶¶¶```````¶¶```````````
                        ```````````¶¶````¶¶`````````````¶¶``````¶```````````
	"""+E

print(head)

banner1 = f"""
                     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄  
                    ▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ ▐░░░░░░░░░░▌ 
                    ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀  ▐░█▀▀▀▀▀▀▀█░▌
                    ▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌      ▐░▌       ▐░▌
                    ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌     ▐░▌      ▐░▌       ▐░▌
                    ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌      ▐░▌       ▐░▌
                    ▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌     ▐░▌      ▐░▌       ▐░▌
                    ▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌       ▐░▌     ▐░▌      ▐░▌       ▐░▌
                    ▐░▌       ▐░▌▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄  ▐░█▄▄▄▄▄▄▄█░▌
                    ▐░▌       ▐░▌▐░▌      ▐░░▌▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ ▐░░░░░░░░░░▌
                     ▀         ▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀   ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀ 
            
                     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄  ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄ 
                    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌ ▐░░░░░░░░░░░▌
                    ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌ ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀  ▐░█▀▀▀▀▀▀▀█░▌
                    ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌▐░▌  ▐░▌           ▐░▌       ▐░▌
                    ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌░▌   ▐░█▄▄▄▄▄▄▄▄▄  ▐░█▄▄▄▄▄▄▄█░▌
                    ▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░▌    ▐░░░░░░░░░░░▌ ▐░░░░░░░░░░░▌
                    ▐░▌          ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░▌░▌   ▐░█▀▀▀▀▀▀▀▀▀  ▐░█▀▀▀▀█░█▀▀
                    ▐░▌          ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌          ▐░▌▐░▌  ▐░▌           ▐░▌     ▐░▌
                    ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄  ▐░▌      ▐░▌
                    ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌ ▐░▌       ▐░▌
                     ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀  ▀▀▀▀▀▀▀▀▀▀▀   ▀         ▀ 

            {color.RED}{version}{color.WHITE}            {color.WHITE}by https://github.com/tushargurav28
"""

banner2 = f"""

                    ▄▖   ▌    ▘ ▌  ▄▖      ▌     
                    ▌▌▛▌▛▌▛▘▛▌▌▛▌  ▌ ▛▘▀▌▛▘▙▘█▌▛▘
                    ▛▌▌▌▙▌▌ ▙▌▌▙▌  ▙▖▌ █▌▙▖▛▖▙▖▌ 
            
                        {color.RED}{version}{color.WHITE}             {color.WHITE}by https://github.com/tushargurav28
"""

banner3 = f"""
                         ██                   ██                 ██      ██
                        ████                 ░██                ░░      ░██
                       ██░░██   ███████      ░██ ██████  ██████  ██     ░██
                      ██  ░░██ ░░██░░░██  ██████░░██░░█ ██░░░░██░██  ██████
                     ██████████ ░██  ░██ ██░░░██ ░██ ░ ░██   ░██░██ ██░░░██
                    ░██░░░░░░██ ░██  ░██░██  ░██ ░██   ░██   ░██░██░██  ░██
                    ░██     ░██ ███  ░██░░██████░███   ░░██████ ░██░░██████
                    ░░      ░░ ░░░   ░░  ░░░░░░ ░░░     ░░░░░░  ░░  ░░░░░░ 
                       ██████                           ██                   
                      ██░░░░██                         ░██                   
                     ██    ░░  ██████  ██████    █████ ░██  ██  █████  ██████
                    ░██       ░░██░░█ ░░░░░░██  ██░░░██░██ ██  ██░░░██░░██░░█
                    ░██        ░██ ░   ███████ ░██  ░░ ░████  ░███████ ░██ ░ 
                    ░░██    ██ ░██    ██░░░░██ ░██   ██░██░██ ░██░░░░  ░██   
                     ░░██████ ░███   ░░████████░░█████ ░██░░██░░██████░███   
                      ░░░░░░  ░░░     ░░░░░░░░  ░░░░░  ░░  ░░  ░░░░░░ ░░░    
            
                        {color.RED}{version}{color.WHITE}                            {color.WHITE}by https://github.com/tushargurav28

"""

banner4 = f"""
                     ▄▄▄       ███▄    █ ▓█████▄  ██▀███   ▒█████   ██▓▓█████▄ 
                    ▒████▄     ██ ▀█   █ ▒██▀ ██▌▓██ ▒ ██▒▒██▒  ██▒▓██▒▒██▀ ██▌
                    ▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌▓██ ░▄█ ▒▒██░  ██▒▒██▒░██   █▌
                    ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌▒██▀▀█▄  ▒██   ██░░██░░▓█▄   ▌
                     ▓█   ▓██▒▒██░   ▓██░░▒████▓ ░██▓ ▒██▒░ ████▓▒░░██░░▒████▓ 
                     ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▓   ▒▒▓  ▒ 
                      ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒   ░▒ ░ ▒░  ░ ▒ ▒░  ▒ ░ ░ ▒  ▒ 
                      ░   ▒      ░   ░ ░  ░ ░  ░   ░░   ░ ░ ░ ░ ▒   ▒ ░ ░ ░  ░ 
                          ░  ░         ░    ░       ░         ░ ░   ░     ░    
                                          ░                             ░      
                     ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  
                    ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
                    ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
                    ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
                    ▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
                    ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
                      ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
                    ░          ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ 
                    ░ ░         ░           ░  ░░ ░      ░  ░      ░  ░   ░     
                    ░                           ░                           

"""
banner_list = [
    banner1,
    banner3,
    banner4
]

instructions_banner = f"""{color.CYAN}
        ____           __                  __  _                 
       /  _/___  _____/ /________  _______/ /_(_)___  ____  _____
       / // __ \/ ___/ __/ ___/ / / / ___/ __/ / __ \/ __ \/ ___/
     _/ // / / (__  ) /_/ /  / /_/ / /__/ /_/ / /_/ / / / (__  ) 
    /___/_/ /_/____/\__/_/   \__,_/\___/\__/_/\____/_/ /_/____/  
        {color.WHITE}                                                        
"""

hacking_banner = f"""{color.GREEN}
    
    █░█ ▄▀█ █▀▀ █▄▀ █ █▄░█ █▀▀ ░ ░ ░
    █▀█ █▀█ █▄▄ █░█ █ █░▀█ █▄█ ▄ ▄ ▄
    {color.WHITE}
"""

keycode_menu = f"""
    {color.WHITE}1. {color.GREEN}Keyboard Text Input                {color.WHITE}11. {color.GREEN}Enter
    {color.WHITE}2. {color.GREEN}Home                               {color.WHITE}12. {color.GREEN}Volume Up
    {color.WHITE}3. {color.GREEN}Back                               {color.WHITE}13. {color.GREEN}Volume Down          
    {color.WHITE}4. {color.GREEN}Recent Apps                        {color.WHITE}14. {color.GREEN}Media Play           
    {color.WHITE}5. {color.GREEN}Power Button                       {color.WHITE}15. {color.GREEN}Media Pause
    {color.WHITE}6. {color.GREEN}DPAD Up                            {color.WHITE}16. {color.GREEN}Tab 
    {color.WHITE}7. {color.GREEN}DPAD Down                          {color.WHITE}17. {color.GREEN}Esc
    {color.WHITE}8. {color.GREEN}DPAD Left           
    {color.WHITE}9. {color.GREEN}DPAD Right
   {color.WHITE}10. {color.GREEN}Delete/Backspace
"""
