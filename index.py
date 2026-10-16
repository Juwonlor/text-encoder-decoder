#To decode a message, you can use the following code:#
import base64
message = input("Enter your message : ")
encoded_message = base64.b64encode(message.encode("utf-8"))
print("Encoded message:", encoded_message.decode("utf-8"))
#to decode and Encode the message, you can use the following code:#
import base64
print("=== Text Encoder and Decoder ===")
print("1. Encode a message")
print("2. Decode a message")

choice = input("choose an option (1 or 2): ")
if choice == "1":
     message = input("Enter your message to encode: ")
     encoded_message = base64.b64encode(message.encode("utf-8"))
     print("Encoded message:", encoded_message.decode("utf-8"))
elif choice == "2":
     message = input("Enter your message to decode: ")
     decoded_message = base64.b64decode(message.encode("utf-8")).decode("utf-8")
     print("Decoded message:", decoded_message)
else:
     print("Invalid choice. Please select 1 or 2.")
     #lets make the code more user-friendly by adding a loop to allow multiple encodings and decodings without restarting the program.#
     while True:
          print("Welcome to a simple Encoder and Decoder Software")
          choice = input("Type 'exit' to quit or stop: ")
if choice.lower() == "exit":
          print("Exiting the program. Welldone!!")
          break
#complete Program#
while True:
      print(\n=== Text Encoder and Decoder ===")
            print("1. Encode a message")
            print("2. Decode a message")
            print("3. Exit")

            choice = input("choose an option (1, 2, or 3):")
            if choice == "1":
                message = input ("Enter your message to encode: ")
                encoded_message = base64.b64encode(message.encode("utf-8"))
                print("Encoded message:", encoded_message.decode("utf-8"))
            elif choice == "2":
                message = input("Enter your message to decode: ")
                decoded_message = base64.b64decode(message.encode("utf-8")).decode("utf-8")
                print("Decoded message:", decoded_message)

             try:
            decoded_bytes = base64.b64decode(
                message, validate=True
            )
            decoded_message = decoded_bytes.decode("utf-8")
            print("Decoded message:", decoded_message)

        except (binascii.Error, UnicodeDecodeError, ValueError):
            print("Error: Invalid Base64 input or text format.")

    elif choice == "3":
        print("Program closed. Goodbye!, Welldone na woman you be.")
        break

    else:
        print("Invalid choice. Please select 1, 2 or 3.")

      

