#!/usr/bin/python3
import os
import json

def get_client_ip():
    """
    Extracts the client IP address from environment variables,
    considering common proxy headers.
    """
    # Order of preference for IP headers
    headers = [
        'HTTP_X_FORWARDED_FOR',
        'HTTP_X_REAL_IP',
        'REMOTE_ADDR'
    ]
    
    for header in headers:
        if header in os.environ:
            # X-Forwarded-For can contain a comma-separated list of IPs.
            # The client IP is typically the first one.
            ip_list = os.environ[header].split(',')
            client_ip = ip_list[0].strip()
            if client_ip:
                return client_ip
                
    return None

def main():
    """
    Main function to get the client IP and return it as JSON.
    """
    print("Content-Type: application/json")
    print()  # End of headers

    client_ip = get_client_ip()
    
    response = {
        'ip': client_ip,
        'error': None
    }
    
    if not client_ip:
        response['error'] = "Could not determine client IP address."

    print(json.dumps(response, indent=2))

if __name__ == "__main__":
    main()
