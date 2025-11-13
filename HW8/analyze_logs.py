#!/usr/bin/env python3
"""
Apache Log Analyzer for FitTrack Pro - HW8
Analyzes Apache access.log and error.log to generate statistics and timeline diagrams
Team: Aleksandr Zinovev, Lee Sewoo, Arslan
"""

import os
import re
from datetime import datetime
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Configuration - Change this to your username
USERNAME = "azinovev"
USER_FILTER = f"/~{USERNAME}/"
CGI_FILTER = f"/cgi-bin/{USERNAME}/"

def create_sample_logs():
    """Create sample Apache access and error logs if they do not exist. For testing only."""
    if not os.path.exists("access.log"):
        with open("access.log", "w") as f:
            f.write(
                f'192.168.0.2 - - [12/Nov/2025:09:30:15 +0000] "GET /~{USERNAME}/index.html HTTP/1.1" 200 2326 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0"\n'
                f'10.0.0.5 - - [12/Nov/2025:10:15:23 +0000] "GET /~{USERNAME}/index.html HTTP/1.1" 200 2100 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Firefox/117.0"\n'
                f'192.168.0.2 - - [12/Nov/2025:10:45:00 +0000] "GET /~{USERNAME}/imprint.html HTTP/1.1" 200 2326 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0"\n'
                f'10.0.0.5 - - [12/Nov/2025:11:05:02 +0000] "GET /cgi-bin/{USERNAME}/maintenance.html HTTP/1.1" 200 1780 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) Safari/605.1.15"\n'
                f'172.16.0.10 - - [12/Nov/2025:11:30:45 +0000] "GET /cgi-bin/{USERNAME}/search_user_activity.py HTTP/1.1" 200 3456 "-" "Mozilla/5.0 (X11; Linux x86_64) Chrome/120.0"\n'
                f'192.168.0.2 - - [12/Nov/2025:12:00:00 +0000] "GET /~{USERNAME}/index.html HTTP/1.1" 200 2326 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0"\n'
                f'10.0.0.5 - - [12/Nov/2025:13:15:30 +0000] "GET /cgi-bin/{USERNAME}/login.html HTTP/1.1" 200 5678 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1"\n'
            )

    if not os.path.exists("error.log"):
        with open("error.log", "w") as f:
            f.write(
                f'[Wed Nov 12 11:12:02.123456 2025] [core:error] [pid 1234] [client 192.168.0.2:54321] File does not exist: /home/{USERNAME}/public_html/missing.html\n'
                f'[Wed Nov 12 11:22:10.654321 2025] [core:error] [pid 1250] [client 10.0.0.5:43210] AH00123: Internal Server Error: /cgi-bin/{USERNAME}/broken_script.py\n'
                f'[Wed Nov 12 14:30:15.789012 2025] [authz_core:error] [pid 1260] [client 172.16.0.10:12345] AH01630: client denied by server configuration: /cgi-bin/{USERNAME}/admin.py\n'
            )

def parse_access_log(log_file_path):
    """
    Extract statistics from Apache access log.
    Only includes entries for our specific user pages.
    """
    stats = defaultdict(list)
    timeline_data = []
    ip_counter = Counter()
    browser_counter = Counter()
    
    # Apache Combined Log Format pattern
    pattern = r'(\S+) - - \[(.*?)\] "(\S+) (.*?) HTTP/.*?" (\d+) (\d+) "(.*?)" "(.*?)"'

    try:
        with open(log_file_path, "r") as log_file:
            for line in log_file:
                match = re.search(pattern, line)
                if match:
                    ip = match.group(1)
                    timestamp_str = match.group(2)
                    method = match.group(3)
                    page = match.group(4)
                    status = match.group(5)
                    size = match.group(6)
                    referer = match.group(7)
                    user_agent = match.group(8)

                    # Filter: only include our pages
                    if USER_FILTER in page or CGI_FILTER in page:
                        # Extract browser name from user agent
                        browser = extract_browser(user_agent)
                        
                        # Parse timestamp
                        try:
                            timestamp = datetime.strptime(timestamp_str.split()[0], '%d/%b/%Y:%H:%M:%S')
                        except:
                            timestamp = None
                        
                        entry = {
                            "ip": ip,
                            "timestamp": timestamp_str,
                            "timestamp_obj": timestamp,
                            "method": method,
                            "status": status,
                            "size": size,
                            "browser": browser,
                            "user_agent": user_agent
                        }
                        
                        stats[page].append(entry)
                        
                        if timestamp:
                            timeline_data.append((timestamp, page, ip))
                        
                        ip_counter[ip] += 1
                        browser_counter[browser] += 1
    
    except FileNotFoundError:
        print(f"Warning: Access log file not found at {log_file_path}")
        print("Using sample data instead...")
    
    return dict(stats), timeline_data, dict(ip_counter), dict(browser_counter)

def parse_error_log(log_file_path):
    """
    Extract statistics from Apache error log.
    Only includes errors related to our pages.
    """
    errors = []
    timeline_data = []
    error_type_counter = Counter()
    ip_counter = Counter()
    
    # Apache Error Log pattern
    pattern = r'\[(.*?)\] \[(.*?)\] \[pid (\d+)\] \[client ([\d\.:]+)\] (.*)'

    try:
        with open(log_file_path, "r") as log_file:
            for line in log_file:
                match = re.search(pattern, line)
                if match:
                    timestamp_str = match.group(1)
                    error_level = match.group(2)
                    pid = match.group(3)
                    client = match.group(4)
                    message = match.group(5)
                    
                    # Filter: only include errors related to our pages
                    if USERNAME in message or USER_FILTER in message or CGI_FILTER in message:
                        # Extract IP from client (format: IP:port)
                        ip = client.split(':')[0]
                        
                        # Parse timestamp
                        try:
                            # Format: "Wed Nov 12 11:12:02.123456 2025"
                            timestamp = datetime.strptime(timestamp_str.split('.')[0], '%a %b %d %H:%M:%S %Y')
                        except:
                            timestamp = None
                        
                        error_entry = {
                            "timestamp": timestamp_str,
                            "timestamp_obj": timestamp,
                            "error_level": error_level,
                            "ip": ip,
                            "message": message
                        }
                        
                        errors.append(error_entry)
                        
                        if timestamp:
                            timeline_data.append((timestamp, error_level, ip))
                        
                        error_type_counter[error_level] += 1
                        ip_counter[ip] += 1
    
    except FileNotFoundError:
        print(f"Warning: Error log file not found at {log_file_path}")
        print("Using sample data instead...")
    
    return errors, timeline_data, dict(error_type_counter), dict(ip_counter)

def extract_browser(user_agent):
    """Extract browser name from user agent string."""
    if "Chrome" in user_agent and "Edg" not in user_agent:
        return "Chrome"
    elif "Firefox" in user_agent:
        return "Firefox"
    elif "Safari" in user_agent and "Chrome" not in user_agent:
        return "Safari"
    elif "Edg" in user_agent:
        return "Edge"
    elif "MSIE" in user_agent or "Trident" in user_agent:
        return "Internet Explorer"
    elif "curl" in user_agent:
        return "curl"
    elif "wget" in user_agent:
        return "wget"
    else:
        return "Other"

def create_access_timeline(timeline_data, output_file="access_timeline.png"):
    """Create timeline diagram for access log."""
    if not timeline_data:
        print("No access data to plot.")
        return
    
    # Sort by timestamp
    timeline_data.sort(key=lambda x: x[0])
    
    # Extract data
    timestamps = [entry[0] for entry in timeline_data]
    pages = [entry[1] for entry in timeline_data]
    
    # Count accesses per hour
    hourly_counts = defaultdict(int)
    for ts in timestamps:
        hour_key = ts.replace(minute=0, second=0, microsecond=0)
        hourly_counts[hour_key] += 1
    
    # Sort by time
    sorted_hours = sorted(hourly_counts.keys())
    counts = [hourly_counts[h] for h in sorted_hours]
    
    # Create plot
    plt.figure(figsize=(12, 6))
    plt.plot(sorted_hours, counts, marker='o', linestyle='-', linewidth=2, markersize=8, color='#3498db')
    plt.fill_between(sorted_hours, counts, alpha=0.3, color='#3498db')
    
    plt.title(f'FitTrack Pro - Access Timeline for {USERNAME}', fontsize=16, fontweight='bold')
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Number of Requests', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Format x-axis
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m %H:%M'))
    plt.gcf().autofmt_xdate()
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Access timeline saved to {output_file}")
    plt.close()

def create_error_timeline(timeline_data, output_file="error_timeline.png"):
    """Create timeline diagram for error log."""
    if not timeline_data:
        print("No error data to plot.")
        return
    
    # Sort by timestamp
    timeline_data.sort(key=lambda x: x[0])
    
    # Extract data
    timestamps = [entry[0] for entry in timeline_data]
    error_levels = [entry[1] for entry in timeline_data]
    
    # Count errors per hour by type
    hourly_errors = defaultdict(lambda: defaultdict(int))
    for ts, level, ip in timeline_data:
        hour_key = ts.replace(minute=0, second=0, microsecond=0)
        hourly_errors[hour_key][level] += 1
    
    # Get unique error levels
    unique_levels = list(set(error_levels))
    
    # Sort by time
    sorted_hours = sorted(hourly_errors.keys())
    
    # Create plot
    plt.figure(figsize=(12, 6))
    
    # Plot each error level as a separate line
    colors = ['#e74c3c', '#f39c12', '#9b59b6', '#1abc9c']
    for i, level in enumerate(unique_levels):
        counts = [hourly_errors[h][level] for h in sorted_hours]
        plt.plot(sorted_hours, counts, marker='o', linestyle='-', linewidth=2, 
                markersize=8, label=level, color=colors[i % len(colors)])
    
    plt.title(f'FitTrack Pro - Error Timeline for {USERNAME}', fontsize=16, fontweight='bold')
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Number of Errors', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Format x-axis
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m %H:%M'))
    plt.gcf().autofmt_xdate()
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Error timeline saved to {output_file}")
    plt.close()

def create_browser_chart(browser_data, output_file="browser_distribution.png"):
    """Create pie chart for browser distribution."""
    if not browser_data:
        print("No browser data to plot.")
        return
    
    browsers = list(browser_data.keys())
    counts = list(browser_data.values())
    
    plt.figure(figsize=(10, 8))
    colors = ['#3498db', '#e74c3c', '#f39c12', '#2ecc71', '#9b59b6', '#95a5a6']
    plt.pie(counts, labels=browsers, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title(f'Browser Distribution for {USERNAME}', fontsize=16, fontweight='bold')
    plt.axis('equal')
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Browser distribution chart saved to {output_file}")
    plt.close()

def write_summary(access_data, error_data, access_ips, access_browsers, error_types, error_ips):
    """Write summary of log statistics to a text file."""
    with open("web_log_summary.txt", "w") as output:
        output.write("=" * 60 + "\n")
        output.write(f"FitTrack Pro - Web Log Analysis for {USERNAME}\n")
        output.write("=" * 60 + "\n\n")
        
        # Access Log Statistics
        output.write("========= ACCESS LOG STATISTICS =========\n\n")
        
        total_requests = sum(len(entries) for entries in access_data.values())
        output.write(f"Total Requests: {total_requests}\n")
        output.write(f"Unique Pages: {len(access_data)}\n")
        output.write(f"Unique Visitors (IPs): {len(access_ips)}\n\n")
        
        # Top pages
        output.write("Top Pages by Access Count:\n")
        sorted_pages = sorted(access_data.items(), key=lambda x: len(x[1]), reverse=True)
        for i, (page, entries) in enumerate(sorted_pages[:10], 1):
            output.write(f"  {i}. {page}: {len(entries)} requests\n")
        output.write("\n")
        
        # Visitor IPs
        output.write("Visitors by IP Address:\n")
        sorted_ips = sorted(access_ips.items(), key=lambda x: x[1], reverse=True)
        for ip, count in sorted_ips:
            output.write(f"  {ip}: {count} requests\n")
        output.write("\n")
        
        # Browser distribution
        output.write("Browser Distribution:\n")
        sorted_browsers = sorted(access_browsers.items(), key=lambda x: x[1], reverse=True)
        for browser, count in sorted_browsers:
            percentage = (count / total_requests) * 100 if total_requests > 0 else 0
            output.write(f"  {browser}: {count} requests ({percentage:.1f}%)\n")
        output.write("\n")
        
        # Detailed page access
        output.write("Detailed Page Access Information:\n")
        for page, entries in sorted_pages:
            output.write(f"\nPage: {page}\n")
            output.write(f"  Accessed {len(entries)} times\n")
            output.write(f"  Visitors:\n")
            for entry in entries[:10]:  # Show first 10 entries
                output.write(f"    {entry['ip']} at [{entry['timestamp']}] using {entry['browser']}\n")
            if len(entries) > 10:
                output.write(f"    ... and {len(entries) - 10} more\n")
        
        output.write("\n\n")
        
        # Error Log Statistics
        output.write("========= ERROR LOG STATISTICS =========\n\n")
        
        total_errors = len(error_data)
        output.write(f"Total Errors: {total_errors}\n")
        output.write(f"Unique Error Types: {len(error_types)}\n")
        output.write(f"IPs Triggering Errors: {len(error_ips)}\n\n")
        
        # Error types
        if error_types:
            output.write("Errors by Type:\n")
            sorted_error_types = sorted(error_types.items(), key=lambda x: x[1], reverse=True)
            for error_type, count in sorted_error_types:
                percentage = (count / total_errors) * 100 if total_errors > 0 else 0
                output.write(f"  {error_type}: {count} errors ({percentage:.1f}%)\n")
            output.write("\n")
        
        # IPs causing errors
        if error_ips:
            output.write("IPs Causing Errors:\n")
            sorted_error_ips = sorted(error_ips.items(), key=lambda x: x[1], reverse=True)
            for ip, count in sorted_error_ips:
                output.write(f"  {ip}: {count} errors\n")
            output.write("\n")
        
        # Detailed errors
        if error_data:
            output.write("Detailed Error Information:\n")
            for err in error_data[:20]:  # Show first 20 errors
                output.write(f"  [{err['timestamp']}] [{err['error_level']}] {err['ip']}\n")
                output.write(f"    {err['message']}\n")
            if len(error_data) > 20:
                output.write(f"  ... and {len(error_data) - 20} more errors\n")

def main():
    """Main function to run log analysis."""
    print("=" * 60)
    print(f"FitTrack Pro - Apache Log Analyzer for {USERNAME}")
    print("=" * 60)
    print()
    
    # Determine log file paths
    access_log_paths = [
        "/var/log/apache2/access.log",
        "/var/log/httpd/access_log",
        "access.log"  # Local sample
    ]
    
    error_log_paths = [
        "/var/log/apache2/error.log",
        "/var/log/httpd/error_log",
        "error.log"  # Local sample
    ]
    
    # Find existing log files
    access_log = None
    for path in access_log_paths:
        if os.path.exists(path):
            access_log = path
            break
    
    error_log = None
    for path in error_log_paths:
        if os.path.exists(path):
            error_log = path
            break
    
    # Create sample logs if no real logs found
    if not access_log or not error_log:
        print("Real log files not found. Creating sample logs for testing...")
        create_sample_logs()
        access_log = "access.log"
        error_log = "error.log"
    
    print(f"Analyzing access log: {access_log}")
    print(f"Analyzing error log: {error_log}")
    print()
    
    # Parse logs
    print("Parsing access log...")
    access_data, access_timeline, access_ips, access_browsers = parse_access_log(access_log)
    
    print("Parsing error log...")
    error_data, error_timeline, error_types, error_ips = parse_error_log(error_log)
    
    print()
    
    # Generate summary
    print("Generating summary report...")
    write_summary(access_data, error_data, access_ips, access_browsers, error_types, error_ips)
    print("✓ Summary saved to web_log_summary.txt")
    print()
    
    # Generate diagrams
    print("Generating timeline diagrams...")
    create_access_timeline(access_timeline, "access_timeline.png")
    create_error_timeline(error_timeline, "error_timeline.png")
    create_browser_chart(access_browsers, "browser_distribution.png")
    
    print()
    print("=" * 60)
    print("Analysis complete!")
    print("=" * 60)
    print()
    print("Generated files:")
    print("  - web_log_summary.txt (text statistics)")
    print("  - access_timeline.png (access timeline diagram)")
    print("  - error_timeline.png (error timeline diagram)")
    print("  - browser_distribution.png (browser pie chart)")
    print()
    print("Next steps:")
    print("  1. Review the summary and diagrams")
    print("  2. Create PDF report with these diagrams")
    print("  3. Submit to repository and email TA")

if __name__ == "__main__":
    main()
