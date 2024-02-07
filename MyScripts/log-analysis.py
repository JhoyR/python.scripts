import re

# Global constant for suspicious patterns
SUSPICIOUS_PATTERNS = [re.escape(pattern) for pattern in ["SQL injection", "cross-site scripting", "bruteforce"]]

def analyze_security_log(log_file):
    """
    Analyzes the security log file for suspicious patterns.
    """
    matches_found = {pattern: 0 for pattern in SUSPICIOUS_PATTERNS}

    try:
        with open(log_file, 'r') as file:
            log_data = file.read()

        for pattern in SUSPICIOUS_PATTERNS:
            matches = re.finditer(pattern, log_data, re.IGNORECASE)
            matches_found[pattern] = len(list(matches))
            for match in matches:
                print(f"Suspicious pattern '{pattern}' found at: {match.group()}")

    except FileNotFoundError:
        print(f"Error: The log file '{log_file}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the log file '{log_file}'.")

    print("Security log analysis complete.")
    print(f"Matches found: {matches_found}")

# Name of the log file to be analyzed
log_file = "server_log.txt"

# Call the function to analyze the log
analyze_security_log(log_file)