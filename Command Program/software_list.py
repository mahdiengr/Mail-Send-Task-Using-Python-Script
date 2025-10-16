import os
def get_visited(data):
    if not data:
        data = input("Enter the filename for Network connections: ")
    try:
        with open(data, "r") as file:
            tempName=input("Pls Type the Network Connection name: ").upper()
            found = False
            print("\n[Network Connections Status:]")
            for line in file:
                words = line.split()
                if tempName in words:
                    found = True
                    print("  ➤", " ".join(words))
            print(f"\n[All {tempName} Connection Showed successfully!]")
            if not found:
                print(f" No {tempName} established connections found.")
    except FileNotFoundError:
        print(f"[Error] The {data} file was not found.")

def get_software_list(data):
    if not data:
        data = input("Enter the filename for software list: ")
    try:
        with open(data, "r") as file:
            found = False
            print("\n[-----Installed Software List-----]")
            for line in file:
                if "\\" not in line:
                    continue      # Just skip lines without backslash
                words = line.strip().split("\\")
                print("  ➤", words[-1])
                found = True
            if found:
                print("\n[ Show All Installed Software!]")
            else:
                print("Not found Software !")
    except FileNotFoundError:
        print(f"[Error] The file {data} name was not found. Pls Correct the File name")

def get_software(data):
    if not data:
        data = input("Enter the filename for software list: ")
    try:
        with open(data, "r") as file:
            found = False
            tempSoftName=input("Pls Type the Software name: ").lower()
            print("\n[-----Installed Software List-----]")
            for line in file:
                if "\\" not in line:
                    continue     
                words = line.strip().split("\\")
                if tempSoftName == words[-1].lower():
                    print("  ➤", words[-1])
                    found = True
            if found:
                print(f"\n[{tempSoftName.capitalize()} Software Installed!]")
            else:
                print(f"Not found {tempSoftName} Software !")
    except FileNotFoundError:
        print(f"[Error] The file {data} name was not found. Pls Correct the File name")



def getCommand():
    command = input("Enter your command: ")
    os.system(command)
    print("\n[Command executed successfully!]")
    file_name=None
    if ">" in command:
        file_name=command.split(">")[-1].strip()
    return file_name
        

def show_menu():
    print("\n" + "-"*12 + " You Are Welcome! " + "-"*12)
    print("Please select an option below:")
    print("  1. Run Custom Command")
    print("  2. Show Network Connections")
    print("  3. Show All Installed Software List")
    print("  4. Specific Installed Software")
    print("  0. Exit Program")

def main():
    fileName=None
    while True:  # Continuous loop
        show_menu()
        
        try:
            choice = int(input("\ncmd-->1  Visited-->2  Software List-->3 Specific Installed Software-->4  Exit-->0\nYour choice: "))
            
            if choice == 1:
                temFile=getCommand()
                if temFile:
                    fileName=temFile
            elif choice == 2:
                get_visited(fileName)
            elif choice == 3:
                get_software_list(fileName)
            elif choice == 4:
                get_software(fileName)
            elif choice == 0:
                print("\n[Goodbye! Exiting program...]")
                break  # Exit the loop
            else:
                print("\n[Invalid input! Please enter 0, 1, 2, 3, 4]")
                
        except ValueError:
            print("\n[Invalid input! Please enter a numeric value.]")
        
        # Optional: Add a pause before showing menu again
        input("\nPress Enter to continue...")

main()

