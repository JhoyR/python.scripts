import re

log_entry = "2023-11-07 12:30:45 [INFO] Conexão estabelecida com o servidor 192.168.1.100"

# Expression pattern for log entry
pattern = r"(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[" \
           r"(?P<log_level>\w+)\] (?P<message>.+)"

# Search for the pattern in the log entry
match = re.search(pattern, log_entry)

if match:
    print(f"Date/Time: {match.group('datetime')}")
    print(f"Log Level: {match.group('log_level')}")
    print(f"Message: {match.group('message')}")
else:
    print("Log entry does not match the expected pattern.")