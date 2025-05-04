from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    # Create the XML-RPC server
    server = SimpleXMLRPCServer(("localhost", 8000))
    print("Server is running on port 8000...")

    # Register the factorial function
    server.register_function(factorial, "factorial")

    # Start the server
    server.serve_forever()

if __name__ == "__main__":
    main()
