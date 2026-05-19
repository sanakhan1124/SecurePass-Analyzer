from colorama import Fore, Style, init
import re

# Start colorama
init(autoreset=True)

# Heading
print(Fore.CYAN + "===================================")
print(Fore.GREEN + "     SecurePass Analyzer")
print(Fore.YELLOW + " Cyber Security Password Checker")
print(Fore.CYAN + "===================================\n")


def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("⚠️ Password should be at least 8 characters long.")

    # Uppercase and lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("🔠 Use both uppercase and lowercase letters.")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("🔢 Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("✨ Add at least one special character.")

    return score, suggestions


# User input
password = input(Fore.WHITE + "🔑 Enter your password: ")

score, suggestions = check_password_strength(password)

# Result
print("\n" + Fore.CYAN + "========= RESULT =========")

if score == 4:
    print(Fore.GREEN + "✅ Password Strength: STRONG 💪")
    print(Fore.GREEN + "🎉 Excellent! Your password is secure.")

elif score == 3:
    print(Fore.YELLOW + "⚠️ Password Strength: MEDIUM")
    print(Fore.YELLOW + "💡 Your password is good, but can be improved.")

else:
    print(Fore.RED + "❌ Password Strength: WEAK")
    print(Fore.RED + "🚨 Your password is vulnerable to attacks.")

# Suggestions
if suggestions:
    print(Fore.MAGENTA + "\n🔧 Suggestions to Improve Password:")
    for suggestion in suggestions:
        print(Fore.WHITE + "- " + suggestion)

print(Fore.CYAN + "\n===================================")
print(Fore.GREEN + " Thank you for using SecurePass!")
print(Fore.CYAN + "===================================")