import re
import argparse
from collections import Counter

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) - - \[(?P<timestamp>.*?)\] "(?P<method>\S+) (?P<resource>\S+) (?P<protocol>\S+)" '
    r'(?P<status>\d{3}) (?P<size>\S+) ".*?" ".*?"'
)

def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    if match:
        data = match.groupdict()
        data['size'] = int(data['size']) if data['size'].isdigit() else 0
        return data
    return None

def analyze_log_file(file_path):
    total_requests = 0
    total_data = 0
    resource_counter = Counter()
    host_counter = Counter()
    status_counter = Counter()
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            log_data = parse_log_line(line)
            if log_data:
                total_requests += 1
                total_data += log_data['size']
                resource_counter[log_data['resource']] += 1
                host_counter[log_data['ip']] += 1
                status_counter[log_data['status'][0] + 'xx'] += 1
    
    most_requested_resource, resource_count = resource_counter.most_common(1)[0]
    most_active_host, host_count = host_counter.most_common(1)[0]
    
    print(f"Total number of requests: {total_requests}")
    print(f"Total data transmitted: {total_data} bytes")
    print(f"Most requested resource: {most_requested_resource} ({resource_count} requests, {resource_count/total_requests:.2%})")
    print(f"Remote host with most requests: {most_active_host} ({host_count} requests, {host_count/total_requests:.2%})")
    
    print("\nHTTP Status Code Distribution:")
    for status_class in ['1xx', '2xx', '3xx', '4xx', '5xx']:
        percentage = (status_counter[status_class] / total_requests) * 100 if total_requests else 0
        print(f"{status_class}: {percentage:.2f}%")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze an Apache web server log file in Combined Log Format.")
    parser.add_argument("file", help="Path to the log file")
    args = parser.parse_args()
    analyze_log_file(args.file)

