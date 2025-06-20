import requests
from pyfiglet import figlet_format
from termcolor import colored

def banner():
    title = "Santosh"
    subtitle = "Channel Master in White Devil"
    print(colored(figlet_format(title, font="slant"), "green"))
    print(colored(f"== {subtitle} ==", "cyan"))

def check_username(username):
    username = username.strip().replace(" ", "")

    platforms = {
        "Facebook": f"https://www.facebook.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Telegram": f"https://t.me/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "YouTube": f"https://www.youtube.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "WhatsApp": f"https://wa.me/{username}",
        "Threads": f"https://www.threads.net/@{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "WeChat": f"https://www.wechat.com/en/{username}",
        "Messenger": f"https://m.me/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Yahoo": f"https://www.yahoo.com/{username}"
    }

    for platform, url in platforms.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(colored(f"[+] Found on {platform}: {url}", "green"))
            elif response.status_code == 404:
                print(colored(f"[-] Not found on {platform}", "red"))
            else:
                print(colored(f"[?] {platform} returned status {response.status_code}", "yellow"))
        except requests.RequestException as e:
            print(colored(f"[!] Error accessing {platform}: {e}", "magenta"))

if __name__ == "__main__":
    banner()
    user_input = input(colored("Enter username to search: ", "cyan"))
    check_username(user_input)

