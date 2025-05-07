from xmlrpc.server import SimpleXMLRPCServer

# Factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Set up server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is running on port 8000...")

# Register the factorial function
server.register_function(factorial, "compute_factorial")

# Run the server
server.serve_forever()


#Krutika Pawar    ROllno 30
#OUTPUT
#Server
# Server is running on port 8000...
# Client
#Enter an integer to compute factorial: 5
# Factorial of 5 is: 120