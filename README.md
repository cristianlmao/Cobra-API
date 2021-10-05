# Cobra-API
Makes writing in python easier.

# HOW TO USE:

1. Download "cobra.py"
2. Put "cobra.py" in the same folder with your main python file
3. In you python file, write "from cobra import *"
4. Done!

# Commands:

    Console.write(Message)                              | Just prints the message
    Console.prefix_write(Prefix, message)               | Prints a message with a prefix (ex. "[MyPrefix] MyMessage")
    
    Debug.error(Message)                                | Prints a message with a red color
    Debug.prefix_error(Prefix, message)                 | Prints a message with a red color and a prefix
    Debug.warning(Message)                              | Prints a message with a yellow color
    Debug.prefix_warning(Prefix, message)               | Prints a message with a yellow color and a prefix
    
    openurl(url)                                        | Opens a url, on your favorite browser
    stop()                                              | Pauses the code 4ever (useful if you don't need to close the console)
    delay(seconds)                                      | Adds a delay between line of codes
    
    Cobra.version()                                     | Prints the version of cobra
    Cobra.test()                                        | Tests some functions of cobra
