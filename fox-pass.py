
try:
    import string , random
    from pyfiglet import Figlet
    from colorama import Fore
except:
    print ("[-] Missing Libraries , Try Installing Required Libraries !")

    import sys , os
    
    if "win" in sys.platform:
        os.system("pip install pyfiglet colorama")
        os.system("cls")
    else:
        os.system("pip3 install colorama pyfiglet")
        os.system("clear")
    from pyfiglet import Figlet
    from colorama import Fore


def banner():
    figlet = Figlet(font="small").renderText("Fox Pass Generator")
    return (Fore.MAGENTA + figlet)

print (banner())
print (Fore.BLUE + "\t[-] Provided By Black Fox Security Team")
print (Fore.GREEN + "\t[+] Author : MaximumRadikali")
print (Fore.CYAN + "\t[=] Telegram Channel : @BlackFoSecurityTeam")

mode = input(Fore.RED + "[1] Generate With Length Character\n[2] Generate with mix 2 lists \n[-] Enter An Option : ")
if mode == "1":
    min_len = int(input(Fore.YELLOW + "[+] Enter Length , Ex : (2) ~ >  "))
    num_pass = int(input(Fore.RED + "[+] Enter Number of Password List to be generate ~ >  "))
    for i in range(num_pass):
        letter = string.ascii_letters + string.digits
        finaly = ''.join(random.choice(letter) for i in range(min_len))
        open("wordlist_generated.txt","a").write(finaly + "\n")
    print (Fore.GREEN + "[+] Saved as wordlist_generated.txt ! ")
elif mode == "2":
    first_file = input(Fore.BLUE + "[-] Please Enter First List Name ~ > ")
    second_file = input(Fore.MAGENTA + "[$] Pleaes Enter Second List Name ~ > ")

    fi_f = open(first_file , "r").readlines()
    se_f = open(second_file , "r").readlines()
    for kh in fi_f:
        for se in se_f:
            open("generated_pass.txt","a").write(kh.strip() + se.strip() + "\n")
    print (Fore.GREEN + "Saved As generated_pass.txt")
    print (Fore.WHITE)

else:
    print (Fore.RED + "Error ! , Enter Correct Number ! ")
    print (Fore.WHITE)