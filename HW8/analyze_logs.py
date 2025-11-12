import os
import re
from datetime import datetime

def create_sample_logs():
    #Create sample Apache access and error logs if they do not exist. For testing only
    if not os.path.exists("access.log"):
        with open("access.log", "w") as f:
            f.write(
                '192.168.0.2 - - [12/Nov/2025:09:30:15] "GET /index.html HTTP/1.1" 200 2326 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0"\n'
                '10.0.0.5 - - [12/Nov/2025:10:15:23] "GET /index.html HTTP/1.1" 200 2100 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Firefox/117.0"\n'
                '192.168.0.2 - - [12/Nov/2025:10:45:00] "GET /index.html HTTP/1.1" 200 2326 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0"\n'
                '10.0.0.5 - - [12/Nov/2025:11:05:02] "GET /contact.html HTTP/1.1" 200 1780 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) Safari/605.1.15"\n'
            )

    if not os.path.exists("error.log"):
        with open("error.log", "w") as f:
            f.write(
                '[Wed Nov 12 11:12:02.123456 2025] [core:error] [pid 1234] [client 192.168.0.2:54321] File does not exist: /var/www/html/missing.html\n'
                '[Wed Nov 12 11:22:10.654321 2025] [core:error] [pid 1250] [client 10.0.0.5:43210] AH00123: Internal Server Error: /submit\n'
            )

def parse_access_log():
    #Extract statistics from Apache access log.
    stats = {}
    pattern = r'(\d+\.\d+\.\d+\.\d+).*\[(.*?)\] "GET (.*?) HTTP.*" \d+ \d+.*"(.*?)"$'

    with open("/var/log/apache2/access.log", "r") as log_file:
        for line in log_file:
            match = re.search(pattern, line)
            if match:
                ip = match.group(1)
                timestamp = match.group(2)
                page = match.group(3)
                user_agent = match.group(4)

                if page not in stats:
                    stats[page] = []
                stats[page].append({
                    "ip": ip,
                    "timestamp": timestamp,
                    "browser": user_agent
                })
    return stats

def parse_error_log():
    #Extract statistics from Apache error log.
    errors = []
    pattern = r'\[(.*?)\].*\[client (\d+\.\d+\.\d+\.\d+).*?\] (.*)'

    with open("/var/log/apache2/error.log", "r") as log_file:
        for line in log_file:
            match = re.search(pattern, line)
            if match:
                timestamp = match.group(1)
                ip = match.group(2)
                message = match.group(3)
                errors.append({
                    "timestamp": timestamp,
                    "ip": ip,
                    "message": message
                })
    return errors

def write_summary(access_data, error_data):
    #Write summary of log statistics to a text file.
    with open("web_log_summary.txt", "w") as output:
        output.write("========= ACCESS LOG STATISTICS =========\n\n")
        for page, entries in access_data.items():
            output.write(f"Page: {page}\n")
            output.write(f"  Accessed {len(entries)} times\n")
            output.write(f"  Visitors:\n")
            for entry in entries:
                output.write(f"    {entry['ip']} at [{entry['timestamp']}] using {entry['browser']}\n")
            output.write("\n")

        output.write("========= ERROR LOG STATISTICS =========\n\n")
        for err in error_data:
            output.write(f"[{err['timestamp']}] {err['ip']} - {err['message']}\n")

def main():
    create_sample_logs()
    access_data = parse_access_log()
    error_data = parse_error_log()
    write_summary(access_data, error_data)
    print("Web log summary generated successfully in 'web_log_summary.txt'.")

if __name__ == "__main__":
    main()
