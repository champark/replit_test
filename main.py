from requests import get

websites = ("google.com", "https://httpstat.us/502", "https://httpstat.us/404",
            "https://httpstat.us/300", "https://httpstat.us/200",
            "https://httpstat.us/101")

results = {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  code = get(website).status_code
  if code >= 500:
    results[website] = "SERVER ERROR"
  elif code >= 400:
    results[website] = "CLIENT ERROR"
  elif code >= 300:
    results[website] = "REDIRECTION"
  elif code >= 200:
    results[website] = "SUCCESS"
  elif code >= 100:
    results[website] = "INFORMATIONAL RESPONSE"
  else:
    results[website] = "UNKNOWN ERROR"

print(results)
