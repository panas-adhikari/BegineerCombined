from rich.console import Console
import rich.table as table
import os
import random
import string

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()
console = Console()
options = [{
                "id":1,
                "name":"Number Guessing Game"},
            {
                "id":2,
                "name":"Rock Paper Scissors Game"},
            {
                "id":3,
                "name":"Password Generator"},
            {
                "id":4,
                "name":"Dice Roller"},
            {
                "id":5,
                "name":"Email Slicer"
            },
            {
                "id":6,
                "name":"Email Validator"
            },
            {
                "id":99,
                "name":"Exit"
            }    
                ]
def display_menu():
    console.print("\n[bold green]Begineer Combined Code BCC[/bold green]\n")
    t =table.Table(title="Choose a option",show_lines=True)
    t.add_column("ID", style="cyan", no_wrap=True)
    t.add_column("Name", style="magenta")
    for option in options:
        t.add_row(str(option["id"]), option["name"])
    console.print(t)


def Number_Guessing_Game():
    clear()
    console.print("[bold blue]Starting Number Guessing Game...[/bold blue]")
    level = input("Choose a level (easy, medium, hard): ").strip().lower()[0]
    if level == 'e':
        max = 10
        random.seed(32)
        number = random.randint(1, max)
        attempts = 3
    elif level == 'm':
        max = 75
        random.seed(42)
        number = random.randint(1, max)
        attempts = 5
    elif level == 'h':
        max = 500
        random.seed(99)
        number = random.randint(1, max)
        attempts = 7
    else:
        console.print("[bold red]Invalid level selected![/bold red]")
        return
    console.print(f"[bold green]You have {attempts} attempts to guess the number between 1 and {max}.[/bold green]")
    for lives in range(attempts):
        console.print(f"[bold yellow]Attempts left: {attempts - lives}[/bold yellow]")
        userguess = input("Enter your guess: ")
        if userguess.isdigit():
            userguess = int(userguess)
            if (userguess == number):
                console.print("[bold green]You Won ![/bold green]")
                return
            if(level=='e'):
                if (userguess < number):
                    console.print("[bold red]Your guess is too low![/bold red]")
                else:
                    console.print("[bold red]Your guess is too high![/bold red]")
            else:
                console.print(f"[bold red]Your guess is too {'low' if userguess < number else 'high'}![/bold red]")
    input("Press Enter to coninue...")
    clear()

def Rock_Paper_Scissors_Game():
    clear()
    choices = ["rock","paper","scissors"]
    scoreBord = [    {"name":"Player", "score":0},
                    {"name":"Computer", "score":0}]
    console.print("[bold blue]Starting Rock Paper Scissors Game...[/bold blue]")
    i = 0
    while True:
        console.print("\n[bold green]Choose your option:[/bold green]")
        console.print("[1] Rock  [2] Paper [3] Scissors [4] Exit")
        choice = input("Enter your choice (1-4): ")
        clear()
        
        if choice == '4':
            console.print("[bold red]Exiting the game...[/bold red]")
            break
        
        if choice not in ['1', '2', '3']:
            console.print("[bold red]Invalid choice, please try again.[/bold red]")
            continue
        
        player_choice = choices[int(choice) - 1]
        computer_choice = random.choice(choices)
        
        console.print(f"[bold yellow]Player chose: {player_choice}[/bold yellow]")
        console.print(f"[bold yellow]Computer chose: {computer_choice}[/bold yellow]")
        
        if player_choice == computer_choice:
            console.print("[bold blue]It's a tie![/bold blue]")

        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            scoreBord[0]["score"] += 1
            console.print("[bold green]You win this round![/bold green]")
            i += 1
        else:
            scoreBord[1]["score"] += 1
            console.print("[bold red]Computer wins this round![/bold red]")
            i += 1
        
        console.print(f"\n[bold cyan]Score after round {i}:[/bold cyan]")
        for player in scoreBord:
            console.print(f"{player['name']}: {player['score']}")
        if scoreBord[0]["score"] >= 3:
            console.print("[bold green]Congratulations! You won the game![/bold green]")
            break
    input("Press Enter to continue...")
    clear()

def password_generator():
    clear()
    console.print("[bold blue]Starting Password Generator...[/bold blue]")
    minLength = int(input("\nEnter minimum password length: "))
    maxLength = int(input("Enter maximum password length: "))
    if minLength < 1 or maxLength < minLength:
        console.print("[bold red]Invalid length range![/bold red]")
        return
    length = random.randint(minLength, maxLength)
    characters = string.ascii_letters + string.digits + "@#$%&"
    password = ''.join(random.choice(characters) for _ in range(length))
    console.print(f"\n[bold green]Generated Password: {password}[/bold green]\n")
    input("Press Enter to continue...")
    clear()

def email_slicer():
    clear()
    console.print("[bold blue]Starting Email Slicer...[/bold blue]")
    email = input("Enter your email address: ").strip()
    if '@' not in email or '.' not in email:
        console.print("[bold red]Invalid email format![/bold red]")
        return
    username, domain = email.split('@')
    console.print(f"\n[bold green]Username: {username}[/bold green]")
    console.print(f"[bold green]Domain: {domain}[/bold green]\n")
    input("Press Enter to continue...")
    clear()

def dice_roller():
    clear()
    console.print("[bold blue]Starting Dice Roller...[/bold blue]")
    while True:
        try:
            sides = int(input("Enter the number of sides on the dice (6, 10, 20, etc.): "))
            if sides < 1:
                console.print("[bold red]Number of sides must be at least 1![/bold red]")
                continue
            roll = random.randint(1, sides)
            console.print(f"[bold green]You rolled a {roll} on a {sides}-sided dice![/bold green]")
            break
        except ValueError:
            console.print("[bold red]Invalid input, please enter a valid number.[/bold red]")
    input("Press Enter to continue...")
    clear()
def email_validator():
    console.clear()
    console.print("[bold blue]Starting Email Validator[/bold blue]")
    email = input("\nEnter your email address: ").strip()
    if email.count('@') != 1 or '.' not in email:
        console.print("[bold red]Invalid email format![/bold red]")
        input("Press Enter to continue...")
        clear()
        return

    username, domain = email.split('@', 1)
    if len(username) == 0 or len(domain) < 3 or '.' not in domain:
        console.print("[bold red]Invalid email structure![/bold red]")
        input("Press Enter to continue...")
        clear()
        return
    allowed_username_chars = string.ascii_letters + string.digits + "._-"
    allowed_domain_chars = string.ascii_letters + string.digits + ".-"

    if not all(c in allowed_username_chars for c in username):
        console.print("[bold red]Invalid characters in username![/bold red]")
        input("Press Enter to continue...")
        clear()
        return

    if not all(c in allowed_domain_chars for c in domain):
        console.print("[bold red]Invalid characters in domain![/bold red]")
        input("Press Enter to continue...")
        clear()
        return
    console.print(f"\n[bold green]Email is valid![/bold green]")
    input("Press Enter to continue...")
    clear()
if __name__ == "__main__":
    while True:
        try:
            display_menu()
            choice = input("\nEnter your choice (1-4) or 'q' to quit: ")
            if choice.lower() == 'q' or (choice.isdigit() and int(choice)==99):
                console.print("[bold red]Exiting the menu...[/bold red]")
                clear()
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(options):
                console.print(f"You selected option {choice}: {options[int(choice)-1]['name']}")
            else:
                console.print("[bold red]Invalid choice, please try again.[/bold red]")
            if choice == '1':
                Number_Guessing_Game()
            elif choice == '2':
                Rock_Paper_Scissors_Game()
            elif choice == '3':
                password_generator()
            elif choice == '4':
                dice_roller()
            elif choice == '5':
                email_slicer()
            elif choice == '6':
                email_validator()
            else:
                console.print("[bold red]Invalid option selected![/bold red]")
        except ValueError as e:
            console.print(f"[bold red]Error: {e}[/bold red]")
        except KeyboardInterrupt:
            console.print("\n Exiting the program...")
            exit(0)