import os
import sys
import time
import requests
import argparse
import re

# ---------------------------------------------------------------------------#
# Colors
class Colors:
    R = '\033[1;31m'
    G = '\033[1;32m'
    Y = '\033[1;33m'
    W = '\033[1;37m'
    C = '\033[1;36m'
    B = '\033[1;34m'
    P = '\033[1;35m'
    NC = '\033[00m'

# ---------------------------------------------------------------------------#
# --- دالة لإزالة أكواد الألوان ---
def remove_ansi_colors(text):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

# ---------------------------------------------------------------------------#
# Message Prefixes
info = f"{Colors.C}[{Colors.W}+{Colors.C}] {Colors.Y}"
ask = f"{Colors.C}[{Colors.W}?{Colors.C}] {Colors.P}"
bad = f"{Colors.C}[{Colors.W}!{Colors.C}] {Colors.R}"
good = f"{Colors.C}[{Colors.W}√{Colors.C}] {Colors.G}"
# ---------------------------------------------------------------------------#

# GitHub Repository Details
GH_USER = "blue24bluer"
GH_REPO = "DB_BlueSky"
API_URL = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/"

# التحقق إذا كان يعمل من خلال الويب
IS_WEB_CONTEXT = not sys.stdout.isatty()

def web_print(message):
    """
    Prints messages, flushes them to stdout, and removes color codes in web context.
    """
    if IS_WEB_CONTEXT:
        print(remove_ansi_colors(message), flush=True)
    else:
        print(message)

def banner():
    """Prints the script's banner."""
    if not IS_WEB_CONTEXT:
        os.system('clear' if os.name == 'posix' else 'cls')
    banner_text = f"""
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│{Colors.W} ▄▄▄▄▄▄    ▄▄▄▄                         {Colors.B}   ▄▄▄▄  {Colors.W}  ▄▄                 │
│{Colors.W} ██▀▀▀▀██  ▀▀██                         {Colors.B} ▄█▀▀▀▀█ {Colors.W}  ██                 │
│{Colors.W} ██    ██    ██      ██    ██   ▄████▄  {Colors.B} ██▄      {Colors.W} ██ ▄██▀   ▀██  ███ │
│{Colors.W} ███████     ██      ██    ██  ██▄▄▄▄██  {Colors.B} ▀████▄  {Colors.W} ██▄██      ██▄ ██  │
│ {Colors.W}██    ██    ██      ██    ██  ██▀▀▀▀▀▀  {Colors.B}     ▀██  {Colors.W}██▀██▄      ████▀  │
│{Colors.W} ██▄▄▄▄██    ██▄▄▄   ██▄▄▄███  ▀██▄▄▄▄█  {Colors.B}█▄▄▄▄▄█▀  {Colors.W}██  ▀█▄      ███   │
│ {Colors.W}▀▀▀▀▀▀▀      ▀▀▀▀    ▀▀▀▀ ▀▀    ▀▀▀▀▀   {Colors.B} ▀▀▀▀▀    {Colors.W}▀▀   ▀▀▀     ██    │
│                                                            {Colors.W}  ███     │
│{Colors.G}@${Colors.B}blue24bluer{Colors.W}                                                          │
└──────────────────────────────────────────────────────────────────────┘
{Colors.NC}
"""
    web_print(banner_text)

def print_summary(results):
    """Prints a formatted summary of found results."""
    if results:
        web_print("\n" + "=" * 25 + " Summary of Found Results " + "=" * 25)
        for result in results:
            web_print(f"{good} {result}{Colors.NC}")
        web_print("=" * 72)

def search_in_databases(target):
    """Searches for a target string in all .txt files in the GitHub repository."""
    banner()
    web_print(f"{info}Fetching database list from GitHub...")

    db_urls = []
    try:
        response = requests.get(API_URL, timeout=15)
        response.raise_for_status()
        files = response.json()
        db_urls = [
            item['download_url'] for item in files
            if isinstance(item, dict) and item.get('type') == 'file' and item.get('name', '').endswith('.txt')
        ]
    except requests.RequestException as e:
        web_print(f"{bad}Error fetching file list from GitHub: {e}")
        sys.exit(1)
    except ValueError:
        web_print(f"{bad}Could not decode the response from GitHub. API rate limit might be exceeded.")
        sys.exit(1)

    if not db_urls:
        web_print(f"{bad}Could not retrieve a valid list of .txt database files.")
        return

    web_print(f"{good}Database list fetched. Starting search for: {Colors.Y}{target}{Colors.NC}")
    web_print("======================================================================")

    found_results = []
    try:
        for url in db_urls:
            db_name = os.path.basename(url)
            web_print(f"\n{Colors.C}[SEARCHING]{Colors.NC} in database: {Colors.P}{db_name}{Colors.NC}")

            line_count = 0
            try:
                with requests.get(url, stream=True, timeout=15) as r:
                    r.raise_for_status()
                    
                    # ====> التعديل الرئيسي هنا <====
                    # سنقرأ السطور كـ bytes ثم نحولها إلى نص يدويًا لتجنب الأخطاء
                    for line_bytes in r.iter_lines(chunk_size=8192):
                        if not line_bytes:
                            continue

                        # تحويل البايتات إلى نص مع تجاهل الأحرف الخاطئة
                        line = line_bytes.decode('utf-8', errors='ignore')
                        
                        # الآن المقارنة آمنة لأن كلا الطرفين من نوع نص
                        if target.lower() in line.lower():
                            web_print(f"{good}[FOUND]{Colors.NC} {line}")
                            found_results.append(line)
                        
                        line_count += 1
                        
                        if line_count % 1000 == 0:
                            if not IS_WEB_CONTEXT:
                                web_print(f"{Colors.Y}---> Processed {line_count} lines. Pausing for 3 seconds...{Colors.NC}")
                                time.sleep(3)
                            else:
                                web_print(f"---> Processed {line_count} lines...")
            
            except requests.RequestException as e:
                web_print(f"{bad}Could not read {db_name}. Error: {e}")
                continue

            web_print(f"{good}[DONE]{Colors.NC} Finished searching in {Colors.P}{db_name}{Colors.NC}")

    except KeyboardInterrupt:
        web_print(f"\n\n{bad}Search interrupted by user.{Colors.NC}")
        web_print(f"{info}Displaying results found before interruption...{Colors.NC}")
        print_summary(found_results)
        sys.exit(0)

    web_print("======================================================================")
    web_print(f"{good}All databases searched. Total results found: {Colors.Y}{len(found_results)}{Colors.NC}")
    print_summary(found_results)

def main():
    parser = argparse.ArgumentParser(
        description=f"USAGE OF {Colors.W}Blue{Colors.B}S{Colors.W}kay{Colors.NC}: Search for data.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-s', '--search', metavar='<term>', type=str, help="Search for a term (phone, email, name, etc.).")
    parser.add_argument('-i', '--install', action='store_true', help="Show instructions to install required tools.")
    args = parser.parse_args()
    
    if args.install:
        install_dependencies() # This needs a definition if you use it
    elif args.search:
        search_in_databases(args.search)
    else:
        banner()
        parser.print_help()

if __name__ == "__main__":
    main()
