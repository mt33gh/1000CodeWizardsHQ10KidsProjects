"""
This program is an example of "urllib.request.urlopen()".
It reads the contents of a URL, and prints it out.
"""


import urllib.request

url = "https://school.lingcslaw.com/projects/"  # Replace with the URL you want to access
response = urllib.request.urlopen(url)

# Read and decode the response
html = response.read().decode("utf-8")
#print(response.read())
#print(response.decode("utf-8"))
print(html)  # Print the webpage content