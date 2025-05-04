import xmlrpc.client #provides tools to call remote procedures 

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Input from user
n = int(input("Enter an integer to compute its factorial: "))

# Call the remote function
result = proxy.factorial(n)

# Show result
print(f"Factorial of {n} is: {result}")