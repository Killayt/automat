import os

def main():
    def upgade():
        os.system('sudo apt autoremove -y')
        os.system('sudo apt upgrade -y')
        os.system('sudo apt full-upgrade -y')
        os.system('sudo apt dist-upgrade -y')
    def change_mac():
        os.system('sudo ifconfig wlan0 down')
        os.system('sudo macchanger -r wlan0')
        os.system('sudo ifconfig wlan0 up')

    print(
        '1. Upgrade system\n'
        '2. Change mac-addres\n'
        )

    boot = int( input('\n\nChoose the func to automatization:\n(set num here_:)') )
    if boot == 1:
        upgade()
    elif boot == 2:
        change_mac()
    else:
        'You chosed encorrect nums'

if __name__ == '__main__':
    main()
