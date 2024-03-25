import pyshorteners

# Initialize the Shortener object
s = pyshorteners.Shortener()

# Take the long URL as input
long_url = input("Enter the long URL: ")

# Get the shortened URL
short_url = s.tinyurl.short(long_url)

# Print the shortened URL
print("Shortened URL:", short_url)