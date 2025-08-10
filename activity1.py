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
      f"or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    #check for commands
    if user_input.lower() == "exit":
       print(f"\n{Fore.BLUE}▮ Exciting Sentiment Spy. Farewell, Agent {user_name}! 🏁{Style.RESET_ALL}")
       break

    elif user_input.lower() =="reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}🎉 All conversation history cleared!{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation histoy:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                #Choose color and emoji based on sentiment
                if sentiment_type == "positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negitive":
                    color = Fore.RED
                    emoji = "🥺"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(f"{idx}. {color}{emoji} {text} "
                      f"(polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
        continue

    #Analyze sentiment
    polarity =TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity <-0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "🥺"
    else:
        sentiment_type = "Nuetral"
        color = Fore.YELLOW
        emoji = "😐"

    #Store in history
    conversation_history.append((user_input, polarity, sentiment_type))

    # Print result with color, emojis, and polarity
    print(f"{color}{emoji} {sentiment_type} Sentiment detected ! "
          f"(polarity: {polarity:.2f}){Style.RESET_ALL}")