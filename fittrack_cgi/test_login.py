#!/usr/bin/env python3

print("Content-Type: text/html")
print("Set-Cookie: test_cookie=test_value; Path=/; Max-Age=3600")
print()

print("""<!DOCTYPE html>
<html>
<head><title>Cookie Test</title></head>
<body>
<h1>Cookie Test</h1>
<p>If you see a cookie called 'test_cookie' in your browser dev tools, cookies are working.</p>
<script>
document.write('<p>Cookies from JavaScript: ' + document.cookie + '</p>');
</script>
<p><a href="maintenance.html">Go to Maintenance</a></p>
</body>
</html>""")
