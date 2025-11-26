#!/usr/bin/python3
import cgi
import json
import urllib.request
import sys

def get_geolocation(ip_address):
    """
    Fetches geolocation data for a given IP address from ipinfo.io.
    """
    # Use a default for local/private IPs for testing
    if ip_address.startswith("127.") or ip_address.startswith("192.168.") or ip_address.startswith("10."):
        return {
            "ip": ip_address,
            "city": "Bremen",
            "region": "Bremen",
            "country": "DE",
            "loc": "53.0793,8.8017", # Default to Bremen for local testing
            "org": "Private Network",
            "postal": "28359",
            "timezone": "Europe/Berlin",
            "readme": "https://ipinfo.io/missingauth"
        }
        
    try:
        # No API key is needed for the free tier up to 50k requests/month
        url = f"https://ipinfo.io/{ip_address}/json"
        with urllib.request.urlopen(url) as response:
            data = response.read()
            return json.loads(data)
    except Exception as e:
        return {"error": str(e)}

def main():
    """
    Main function to handle CGI request and return geolocation data.
    """
    print("Content-Type: application/json")
    print()  # End of headers

    form = cgi.FieldStorage()
    ip = form.getvalue('ip')

    if not ip:
        print(json.dumps({"error": "IP address parameter is missing."}, indent=2))
        return

    geo_data = get_geolocation(ip)
    
    # Restructure the data to match the plan's requirements (lat, lng)
    if "loc" in geo_data and "error" not in geo_data:
        lat, lng = geo_data["loc"].split(',')
        geo_data['lat'] = float(lat)
        geo_data['lng'] = float(lng)

    print(json.dumps(geo_data, indent=2))

if __name__ == "__main__":
    main()
