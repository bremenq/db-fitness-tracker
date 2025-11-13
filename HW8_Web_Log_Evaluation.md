# Assignment 8: Web Log Evaluation

**Course:** Databases Project 2025  
**Instructor:** Peter Baumann, Constructor University  
**Submission:** By team, through git repository  
**Deadline:** 2025-nov-13 23:59 (TODAY!)

---

## 📋 **Assignment Overview**

Analyze Apache web server logs to extract statistics about your FitTrack Pro website access patterns and errors.

---

## 🎯 **Requirements**

### **1. Access Statistics**

Write a server-side script to analyze Apache request logs and extract:

- **Page Access Frequency:** How often was each page accessed?
- **User Information:** Who accessed the pages (IP addresses)?
- **Timestamps:** When were the pages accessed?
- **Browser Information:** What browsers were used?
- **Timeline Diagram:** Create a visual timeline showing access patterns

### **2. Error Analysis**

Analyze Apache error logs to extract:

- **Error Types:** What errors occurred?
- **Error Origins:** Who triggered the errors (IP addresses)?
- **Error Timestamps:** When did errors occur?
- **Timeline Diagram:** Create a visual timeline showing error patterns

---

## 📊 **Deliverables**

### **Required Submissions:**

1. **PDF Report** containing:
   - Access statistics
   - Error statistics
   - Timeline diagrams (2 diagrams minimum)
   - Analysis and insights

2. **Script** (in repository):
   - Server-side script in your favorite language (Python recommended)
   - Must access Apache request and error logs
   - Should generate statistics and/or diagrams
   - Document the script location in submission email to TAs

---

## 📝 **Implementation Notes**

### **Log File Locations on ClamV Server:**

```bash
# Apache access log (request log)
/var/log/apache2/access.log
# or
/var/log/httpd/access_log

# Apache error log
/var/log/apache2/error.log
# or
/var/log/httpd/error_log
```

### **If Insufficient Traffic:**

> "if you find your service has not been called often enough (well, we did not do any advertisement) then simply generate a few clicktrails by invoking your own service from your PCs."

**Solution:** Generate test traffic by:
- Visiting your pages multiple times from different browsers
- Using different devices (phone, laptop, tablet)
- Asking team members to access the site
- Using `curl` or `wget` to simulate requests

---

## 🛠️ **Suggested Implementation Approach**

### **Option 1: Python Script (Recommended)**

```python
#!/usr/bin/env python3
"""
Apache Log Analyzer for FitTrack Pro
Analyzes access.log and error.log to generate statistics
"""

import re
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt

# Parse Apache access log
def parse_access_log(log_file):
    # Apache Combined Log Format:
    # IP - - [timestamp] "METHOD /path HTTP/1.1" status size "referer" "user-agent"
    pattern = r'(\S+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"'
    
    stats = {
        'pages': defaultdict(int),
        'ips': defaultdict(int),
        'browsers': defaultdict(int),
        'timeline': []
    }
    
    with open(log_file, 'r') as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                ip, timestamp, request, status, size, referer, user_agent = match.groups()
                
                # Extract page from request
                page = request.split()[1] if len(request.split()) > 1 else '/'
                
                # Filter for your pages only (e.g., /~azinovev/)
                if '/~azinovev/' in page or page.startswith('/cgi-bin/'):
                    stats['pages'][page] += 1
                    stats['ips'][ip] += 1
                    stats['browsers'][user_agent] += 1
                    stats['timeline'].append((timestamp, page, ip))
    
    return stats

# Parse Apache error log
def parse_error_log(log_file):
    # Apache Error Log Format:
    # [timestamp] [level] [client IP] message
    pattern = r'\[(.*?)\] \[(.*?)\] \[client (.*?)\] (.*)'
    
    errors = {
        'types': defaultdict(int),
        'ips': defaultdict(int),
        'timeline': []
    }
    
    with open(log_file, 'r') as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                timestamp, level, client_ip, message = match.groups()
                
                # Filter for your errors only
                if '/~azinovev/' in message or 'azinovev' in message:
                    errors['types'][level] += 1
                    errors['ips'][client_ip] += 1
                    errors['timeline'].append((timestamp, level, client_ip, message))
    
    return errors

# Generate timeline diagram
def create_timeline(data, title, output_file):
    # Create matplotlib timeline
    # ... implementation ...
    pass

if __name__ == '__main__':
    access_stats = parse_access_log('/var/log/apache2/access.log')
    error_stats = parse_error_log('/var/log/apache2/error.log')
    
    # Print statistics
    print("=== ACCESS STATISTICS ===")
    print(f"Total page views: {sum(access_stats['pages'].values())}")
    print(f"Unique visitors: {len(access_stats['ips'])}")
    print("\nTop 10 pages:")
    for page, count in sorted(access_stats['pages'].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {page}: {count} views")
    
    print("\n=== ERROR STATISTICS ===")
    print(f"Total errors: {sum(error_stats['types'].values())}")
    print("\nErrors by type:")
    for error_type, count in error_stats['types'].items():
        print(f"  {error_type}: {count}")
    
    # Generate diagrams
    create_timeline(access_stats['timeline'], "Access Timeline", "access_timeline.png")
    create_timeline(error_stats['timeline'], "Error Timeline", "error_timeline.png")
```

### **Option 2: Use Existing Tools**

You can use existing log analysis tools:

- **GoAccess** (real-time web log analyzer)
  ```bash
  goaccess /var/log/apache2/access.log -o report.html
  ```

- **AWStats** (advanced web statistics)
- **Webalizer** (web server log analysis)
- **Logwatch** (log analysis tool)

**Important:** If using an existing tool, you MUST:
- Indicate which tool you used in your PDF report
- Explain why you chose it
- Show how you configured it for your specific logs

---

## 📈 **Timeline Diagram Requirements**

### **Access Timeline Should Show:**
- X-axis: Time (date/hour)
- Y-axis: Number of requests
- Different colors for different pages or IPs
- Clear labels and legend

### **Error Timeline Should Show:**
- X-axis: Time (date/hour)
- Y-axis: Number of errors
- Different colors for different error types
- Clear labels and legend

### **Suggested Tools for Diagrams:**
- **Python:** matplotlib, seaborn, plotly
- **Excel/Google Sheets:** Import CSV data and create charts
- **Online tools:** Chart.js, D3.js, Google Charts

---

## 🚀 **Quick Start Guide**

### **Step 1: Access Server Logs**

```bash
# SSH to ClamV server
ssh azinovev@clabsql.clamv.constructor.university

# Check log file locations
ls -la /var/log/apache2/
# or
ls -la /var/log/httpd/

# View recent access log entries
tail -100 /var/log/apache2/access.log | grep azinovev

# View recent error log entries
tail -100 /var/log/apache2/error.log | grep azinovev
```

### **Step 2: Generate Test Traffic (if needed)**

```bash
# From your local machine, access your pages multiple times
curl https://clabsql.clamv.constructor.university/~azinovev/index.html
curl https://clabsql.clamv.constructor.university/~azinovev/imprint.html
curl https://clabsql.clamv.constructor.university/cgi-bin/azinovev/maintenance.html
curl https://clabsql.clamv.constructor.university/cgi-bin/azinovev/search_user_activity.py

# Use different user agents to simulate different browsers
curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0" https://...
curl -A "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0) Safari/604.1" https://...
```

### **Step 3: Download Logs (if analyzing locally)**

```bash
# Download access log
scp azinovev@clabsql.clamv.constructor.university:/var/log/apache2/access.log ./access.log

# Download error log
scp azinovev@clabsql.clamv.constructor.university:/var/log/apache2/error.log ./error.log
```

### **Step 4: Run Analysis Script**

```bash
# Run your Python script
python3 analyze_logs.py

# Or use GoAccess
goaccess access.log -o report.html --log-format=COMBINED
```

### **Step 5: Create PDF Report**

Include in your PDF:
1. **Introduction:** Brief description of your website
2. **Methodology:** How you analyzed the logs (script or tool)
3. **Access Statistics:**
   - Total page views
   - Unique visitors (IPs)
   - Most popular pages
   - Browser distribution
   - Access timeline diagram
4. **Error Statistics:**
   - Total errors
   - Error types and frequencies
   - IPs that triggered errors
   - Error timeline diagram
5. **Insights/Conclusions:** What did you learn from the data?

---

## ✅ **Submission Checklist**

- [ ] Script created and tested
- [ ] Script added to repository (e.g., `db1/HW8/analyze_logs.py`)
- [ ] Access statistics generated
- [ ] Error statistics generated
- [ ] Access timeline diagram created
- [ ] Error timeline diagram created
- [ ] PDF report created with all diagrams and statistics
- [ ] PDF committed to repository
- [ ] Email sent to TA with:
  - Subject: `HW8 - Web Log Evaluation - [Your Name]`
  - Script location in repository
  - Link to PDF in repository
  - Any special notes about implementation

---

## 📧 **Email Template for TA**

```
Subject: HW8 - Web Log Evaluation - Aleksandr Zinovev

Dear [TA Name],

Please find my HW8 submission for Web Log Evaluation:

Repository: https://github.com/[your-repo]/db-fitness-tracker
Branch: main (or HW8)

Files:
- Script: db1/HW8/analyze_logs.py
- PDF Report: db1/HW8/HW8_Web_Log_Evaluation.pdf
- Timeline Diagrams: db1/HW8/access_timeline.png, db1/HW8/error_timeline.png

Implementation notes:
- Used Python script to parse Apache logs
- Generated test traffic by accessing pages from multiple browsers
- Created timeline diagrams using matplotlib

Best regards,
Aleksandr Zinovev
```

---

## 🔍 **Tips & Best Practices**

1. **Filter Your Logs:** Focus only on your pages (e.g., `/~azinovev/` or `/cgi-bin/azinovev/`)
2. **Handle Large Logs:** If logs are huge, use `grep` to filter first:
   ```bash
   grep 'azinovev' /var/log/apache2/access.log > my_access.log
   ```
3. **Test Your Script:** Run on a small sample first before processing full logs
4. **Document Everything:** Comment your code, explain your approach in the PDF
5. **Make Diagrams Clear:** Use proper labels, legends, and titles
6. **Analyze Patterns:** Don't just show numbers - explain what they mean

---

## ⏰ **DEADLINE: TODAY (2025-nov-13 23:59)**

This assignment is due **TONIGHT**! Prioritize:
1. Get the script working (even if simple)
2. Generate basic statistics
3. Create at least 2 timeline diagrams
4. Write a concise PDF report
5. Submit to repository and email TA

---

**Good luck!** 🚀

