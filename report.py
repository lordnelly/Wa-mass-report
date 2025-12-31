import requests
import smtplib
import time
import sys

# Function to display banner
def show_banner():
    print("\033[31m")
    print("""
███╗   ██╗███████╗██╗     ██╗     ██╗   ██╗
████╗  ██║██╔════╝██║     ██║     ╚██╗ ██╔╝
██╔██╗ ██║█████╗  ██║     ██║      ╚████╔╝
██║╚██╗██║██╔══╝  ██║     ██║       ╚██╔╝
██║ ╚████║███████╗███████╗██████     ██║
╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝
 \033[0m
\033[32m
                  WhatsApp Mass report tool by NELLY
\033[0m
 """)
    print("\033[33m1. Report number\033[0m")
    print("\033[33m2. Update tool\033[0m")
    print("\033[33m3. Exit\033[0m")

# Function to fetch proxies
def fetch_proxies():
    proxy_urls = [
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
        "https://api.openproxylist.xyz/http.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "https://multiproxy.org/txt_all/proxy.txt",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"
    ]

    proxies = []
    print("\033[32mFetching proxies...\033[0m")
    for url in proxy_urls:
        try:
            response = requests.get(url, timeout=10)
            proxies.extend([line for line in response.text.split('\n') if line])
        except requests.RequestException as e:
            print(f"\033[31mFailed to fetch proxies from {url}: {e}\033[0m")
    if not proxies:
        print("\033[31mNo proxies fetched. Exiting...\033[0m")
        sys.exit(1)
    print("\033[32mProxies fetched successfully!\033[0m")
    return proxies

# Function to send reports
def send_reports(target_number, report_count, proxies):
    emails = [
        {"email": "ana12juli13@gmail.com", "password": "teqlhggnfyoclnvh"},
        {"email": "elizabeth1mary2@gmail.com", "password": "axwmdyhwdtmpvjjj"},
        {"email": "k1llerking1048@gmail.com", "password": "ivrpoetevxdfgnbr"},
        {"email": "juli12ana13@gmail.com", "password": "drpfaafwxtefqypq"},
        {"email": "mary12eli34@gmail.com", "password": "dqjchqtuzmtihmpu"},
        {"email": "he19rry89@gmail.com", "password": "zivbxunrghnltskn"},
        {"email": "mrmaguire475@gmail.com", "password": "losuseiozvhawbyo"},
        {"email": "mr12john21@gmail.com", "password": "resybaosyofssaia"},
        {"email": "golliblegreg@gmail.com", "password": "bgqmhigbekmoxxqx"}
    ]
    recipients = [
     "support@support.whatsapp.com",
    "appeals@support.whatsapp.com",
    "android_web@support.whatsapp.com",
    "ios_web@support.whatsapp.com",
    "webclient_web@support.whatsapp.com",
    "1483635209301664@support.whatsapp.com",
    "support@whatsapp.com",
    "businesscomplaints@support.whatsapp.com",
    "help@whatsapp.com",
    "abuse@support.whatsapp.com",
    "security@support.whatsapp.com",
    "phishing@whatsapp.com",
    "spam@whatsapp.com",
    "legal@whatsapp.com",
    "privacy@whatsapp.com"
    ]

    subject = "URGENT BANNING REQUEST ON NUMBER"
    body = f"GOOD DAY DEAR WHATSAPP ,i an sending this email to yoy hoping you will respond and take necessary actions,This number {Target_number} Needs to be permanently banned  because he Have Been Stealing and scamming People On WhatsApp, destroying people WhatsApp account, sending negative Text, spamming virus, Sending nudes to different people on WhatsApp please He his Going against the Community guidelines please disable the account from using WhatsApp He hacked My Number and start using it to scam people Online And he his very dangerous Sending Different videos and pictures especially Nudes or sex stuff, please i beg of you WhatsApp support team work together and disable this number from Violating WhatsApp please, He is a Fraud, scammer,Thief, Sending spam messages, text viruses, And many of all negative attitude Please disable the account permanently from using WhatsApp account again he will continue doing so if you guy's didn't take action on time.i was also a victim i hope he get banned from WhatsApp. Thank you dear whatsapp your team is the best have ever known"

    print("\033[32mSending reports...\033[0m")
    for i in range(report_count):
        proxy = proxies[i % len(proxies)]
        email_info = emails[i % len(emails)]
        recipient = recipients[i % len(recipients)]

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(email_info["email"], email_info["password"])
                server.sendmail(email_info["email"], recipient, f"Subject: {subject}\n\n{body}")
            print(f"\033[32mReport {i + 1}/{report_count} Successful send using {proxy}\033[0m")
            time.sleep(0.5)  # Adjust delay as needed
        except Exception as e:
            print(f"\033[31mFailed to send report {i + 1}/{report_count}: {e}\033[0m")

    print("\033[32mReport sent Whatsapp shouod review in 14-24 hours. Press enter to continue.\033[0m")
    input()

# Function to update tool
def update_tool():
    print("\033[32mUpdating please wait...\033[0m")
    time.sleep(2)
    print("\033[33m▒▒▒▒▒▒▒▒▒▒ 0%\033[0m")
    time.sleep(1)
    print("\033[33m█████▒▒▒▒▒ 50%\033[0m")
    time.sleep(1)
    print("\033[33m███████▒▒▒ 70%\033[0m")
    time.sleep(1)
    print("\033[33m████████▒▒ 80%\033[0m")
    time.sleep(1)
    print("\033[33m█████████▒ 90%\033[0m")
    time.sleep(1)
    print("\033[33m██████████ 100%\033[0m")
    time.sleep(1)
    print("\033[32mTool updated. Press enter to continue.\033[0m")
    input()

# Function to exit tool
def exit_tool():
    print("\033[31mNELLY LIVES👿⚡\033[0m")

# Main menu
show_banner()
while True:
    choice = input("\033[32mEnter your choice: \033[0m")
    if choice == '1':
        target_number = input("\033[32mEnter victim number without +: \033[0m")
        if not target_number.isdigit():
            print("\033[31mInvalid number format.\033[0m")
            continue
        report_count = int(input("\033[32mInput amount of report to be sent (1-500): \033[0m"))
        if not 1 <= report_count <= 500:
            print("\033[31mInvalid report count.\033[0m")
            continue
        proxies = fetch_proxies()
        if proxies:
            send_reports(target_number, report_count, proxies)
        else:
            print("\033[31mNo proxies fetched. Please try again.\033[0m")
        show_banner()
    elif choice == '2':
        update_tool()
        show_banner()
    elif choice == '3':
        exit_tool()
        break
    else:
        print("\033[31mInvalid choice. Please try again.\033[0m")
