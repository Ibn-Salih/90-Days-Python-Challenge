# - Topics:
# - Learn how intrusion detection systems work.
# - Project:
# - Build a basic IDS that scans logs 
# - for failed login attempts and potential SQL injection patterns.


import re
from collections import defaultdict
from datetime import datetime, timedelta

# Regex patterns for failed logins and SQLi
FAILED_LOGIN_PATTERN = r"Failed password|401 Unauthorized|403 Forbidden"
SQLI_PATTERN = r"'.*--|UNION.*SELECT|1=1|OR\s+'1'='1'"

# Thresholds for alerts
FAILED_LOGIN_THRESHOLD = 5  # Max failed attempts per IP
TIME_WINDOW = timedelta(minutes=5)  # Time window for counting events

def parse_log(log_file):
    failed_logins = defaultdict(list)  # Track failed logins per IP
    sqli_attempts = []  # Track SQLi attempts

    with open(log_file, 'r') as file:
        for line in file:
            # Check for failed logins
            if re.search(FAILED_LOGIN_PATTERN, line, re.IGNORECASE):
                ip_match = re.search(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)
                if ip_match:
                    ip = ip_match.group()
                    failed_logins[ip].append(datetime.now())

            # Check for SQLi patterns
            if re.search(SQLI_PATTERN, line, re.IGNORECASE):
                sqli_attempts.append(line.strip())

    return failed_logins, sqli_attempts


def check_for_alerts(failed_logins, sqli_attempts):
    # Alert for failed logins
    for ip, timestamps in failed_logins.items():
        recent_failures = [t for t in timestamps if datetime.now() - t <= TIME_WINDOW]
        if len(recent_failures) >= FAILED_LOGIN_THRESHOLD:
            print(f"ALERT: {ip} has {len(recent_failures)} failed logins in the last {TIME_WINDOW}.")

    # Alert for SQLi attempts
    if sqli_attempts:
        print(f"ALERT: Detected {len(sqli_attempts)} SQL injection attempts:")
        for attempt in sqli_attempts:
            print(f"- {attempt}")


def main(log_file):
    failed_logins, sqli_attempts = parse_log(log_file)
    check_for_alerts(failed_logins, sqli_attempts)

if __name__ == "__main__":
    log_file = r"C:/Users/pc/Desktop/sample.log"  # Replace with your log file path
    main(log_file)