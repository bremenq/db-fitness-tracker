#!/usr/bin/python3
"""
test_geolocation.py

Simple test runner for Assignment 10 – Linked Services.
Checks:
- get_client_info.py returns an IP and timestamp
- geolocation.py returns coordinates and location data
- location_map.html and location_widget.html contain map placeholders
"""

import urllib.request
import urllib.error
import json
import sys

USERNAME = "YOUR_USERNAME"
BASE_URL = f"https://clabsql.clamv.constructor.university/~{USERNAME}"

def fetch(path):
    url = f"{BASE_URL}/{path}"
    print(f"Requesting: {url}")
    try:
        with urllib.request.urlopen(url) as resp:
            content_type = resp.headers.get("Content-Type", "")
            body = resp.read()
            return content_type, body
    except urllib.error.HTTPError as e:
        print(f"HTTP error for {url}: {e.code} {e.reason}")
        raise
    except urllib.error.URLError as e:
        print(f"URL error for {url}: {e.reason}")
        raise

def fetch_json(path):
    ctype, body = fetch(path)
    return json.loads(body.decode("utf-8"))

def test_client_info():
    print("\n=== Testing get_client_info.py ===")
    data = fetch_json("get_client_info.py")
    assert "ip" in data, "Response missing 'ip'"
    assert "timestamp" in data, "Response missing 'timestamp'"
    print(f"Detected IP: {data['ip']}")
    return data["ip"]

def test_geolocation(ip):
    print("\n=== Testing geolocation.py ===")
    data = fetch_json(f"geolocation.py?ip={ip}")
    for key in ("ip", "lat", "lng", "city", "country"):
        assert key in data, f"geolocation.py missing '{key}'"
    print(f"Location: {data['city']}, {data['country']}")

def test_location_pages():
    print("\n=== Testing HTML pages ===")

    # Full map page
    _, body = fetch("forms/location_map.html")
    html = body.decode("utf-8")
    assert "leaflet" in html.lower(), "location_map.html missing Leaflet"
    assert "map" in html, "location_map.html missing #map div"
    print("location_map.html OK")

    # Widget page
    _, body = fetch("forms/location_widget.html")
    html = body.decode("utf-8")
    assert "mini-map" in html, "location_widget.html missing #mini-map"
    print("location_widget.html OK")

def main():
    try:
        ip = test_client_info()
        test_geolocation(ip)
        test_location_pages()
        print("\nAll tests passed.")
    except Exception as e:
        print("\nTest failed:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
