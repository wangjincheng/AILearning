import aiml
# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.aiml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
    message = input("Enter your message >> ")
    if (message == 'quit'):
        exit(0)
    print(kernel.respond(message))