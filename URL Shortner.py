import  pyshorteners
url = input("Enter your URL :\n")
s = pyshorteners.Shortener().tinyurl.short(url)
print(f"Your shorted URL is {s}" )        