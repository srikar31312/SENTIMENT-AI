import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}👋🎉 Welcome to Sentiment Spy! 🕵️{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL} ").strip()
if not user_name:
    user_name = "Mystery Agent"

conversation_history = []

print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a sentence and I will analyze your words using TextBlob 🔍")
print(f"Commands: {Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, {Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}⚠ Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE}🏁 Exiting Sentiment Spy. Farewell, Agent {user_name}!{Style.RESET_ALL}")

        total_msgs = len(conversation_history)
        positives = sum(1 for _, _, s in conversation_history if s == "Positive")
        negatives = sum(1 for _, _, s in conversation_history if s == "Negative")
        neutrals = sum(1 for _, _, s in conversation_history if s == "Neutral")

        if total_msgs > 0:
            print(f"{Fore.CYAN}📜 Conversation Summary:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color, emoji = Fore.GREEN, "😊"
                elif sentiment_type == "Negative":
                    color, emoji = Fore.RED, "🥺"
                else:
                    color, emoji = Fore.YELLOW, "😐"
                print(f"{idx}. {color}{emoji} {text} "
                      f"(polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")

            print(f"\n{Fore.MAGENTA}🛰️ FINAL MISSION REPORT 🛰️{Style.RESET_ALL}")
            print(f"{Fore.CYAN}Total messages analyzed:{Style.RESET_ALL} {total_msgs}")
            print(f"{Fore.GREEN}Positive:{Style.RESET_ALL} {positives}")
            print(f"{Fore.RED}Negative:{Style.RESET_ALL} {negatives}")
            print(f"{Fore.YELLOW}Neutral:{Style.RESET_ALL} {neutrals}")

            if positives > negatives and positives > neutrals:
                mission_mood = f"{Fore.GREEN}Positive 🟢{Style.RESET_ALL}"
            elif negatives > positives and negatives > neutrals:
                mission_mood = f"{Fore.RED}Negative 🔴{Style.RESET_ALL}"
            else:
                mission_mood = f"{Fore.YELLOW}Neutral 🟡{Style.RESET_ALL}"

            print(f"{Fore.CYAN}Overall mission mood:{Style.RESET_ALL} {mission_mood}\n")
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}🧹 All conversation history cleared!{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}📭 No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation history:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color, emoji = Fore.GREEN, "😊"
                elif sentiment_type == "Negative":
                    color, emoji = Fore.RED, "🥺"
                else:
                    color, emoji = Fore.YELLOW, "😐"
                print(f"{idx}. {color}{emoji} {text} (polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
        continue

    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type, color, emoji = "Positive", Fore.GREEN, "😊"
    elif polarity < -0.25:
        sentiment_type, color, emoji = "Negative", Fore.RED, "🥺"
    else:
        sentiment_type, color, emoji = "Neutral", Fore.YELLOW, "😐"

    conversation_history.append((user_input, polarity, sentiment_type))
    print(f"{color}{emoji} {sentiment_type} Sentiment detected! (polarity: {polarity:.2f}){Style.RESET_ALL}")