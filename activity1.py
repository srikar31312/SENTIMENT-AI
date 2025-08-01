import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize coloroma for colored output
colorama.init()

# Emojis for the start of the progress
print(f"{Fore.CYAN}👋🎉 Welcome to Sentiment Spy! 🕵️{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please ener your name : {Style.RESET_ALL} ").strip()
if not user_name:
    user_name = "Mystery Agent" #Fall back if user doesnt provide a name

# Store coversation as a list of tuples: (text, polarity, sentiment_type)
conversation_history = []

print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a sentence and I will analyze your sentences with TextBlob and show you the sentiment 🔍")
print(f"Type{Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, "
      f"or{Fore.YELLOW},'exit'{Fore.CYAN} to quit.{Style.Reset_ALL}\n")