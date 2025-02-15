import random
import string

adjectives = ["Cool", "Happy", "Fast", "Brave", "Clever", "Lucky", "Strong", "Mighty", "Swift", "Witty", "Bold", "Energetic", "Fearless", "Gentle", "Heroic", "Jolly", "Lively", "Noble", "Playful", "Vibrant"]
nouns = ["Tiger", "Dragon", "Eagle", "Panther", "Wolf", "Falcon", "Shark", "Phoenix", "Cheetah", "Griffin", "Lion", "Hawk", "Bear", "Leopard", "Raven", "Fox", "Cobra", "Jaguar", "Owl", "Stallion"]

def generate_username(length=10, include_numbers=True, include_special_chars=True):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun
    
    if include_numbers:
        username += str(random.randint(10, 99))
    
    if include_special_chars:
        username += random.choice(string.punctuation)
    
    # Trim or extend the username as needed
    if len(username) > length:
        username = username[:length]  # Trim to fit the length
    elif len(username) < length:
        while len(username) < length:
            username += random.choice(string.ascii_letters + string.digits + string.punctuation)
    
    return username

def save_usernames(usernames, filename="usernames.txt"):
    with open(filename, "a") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"Usernames saved to {filename}")

def main():
    print("Welcome to the Random Username Generator!")
    try:
        num_usernames = int(input("How many usernames would you like to generate? "))
        length = int(input("Enter desired username length: "))
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return
    
    usernames = [generate_username(length, include_numbers, include_special_chars) for _ in range(num_usernames)]
    
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)
    
    save_to_file = input("Would you like to save the usernames to a file? (yes/no): ").strip().lower()
    if save_to_file == "yes":
        save_usernames(usernames)

if __name__ == "__main__":
    main()
