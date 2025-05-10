user_input = input("Enter your message to ceasher encode: ").lower()
shift_choice = int(input("Enter shift length for encoding: "))

alphs = 'abcdefghijklmnopqrstuvwxyz'

def encode(message,shift_choice):
    encoded_message = [""]*len(message)
    for i in range(len(user_input)):
        if user_input[i] in alphs:
            get_index = alphs.index(user_input[i])
            shifted_index = get_index + shift_choice
            if shifted_index > len(alphs):
                shifted_index = shifted_index - len(alphs)
            encoded_message[i] = alphs[shifted_index]
        else:
            encoded_message[i] = user_input[i]
    encoded_message = ''.join(encoded_message)
    return encoded_message

def decode(encoded_message, shift_choice):
    decoded_message = [""]*len(encoded_message)
    for i in range(len(encoded_message)):
        if encoded_message[i] in  alphs:
            get_index = alphs.index(encoded_message[i])
            shift_index = get_index - shift_choice
            if shift_index < 0:
                shift_index = len(alphs) - shift_index
            decoded_message[i] = alphs[shift_index]
        else:
            decoded_message[i] = encoded_message[i]
    decoded_message = ''.join(decoded_message)
    return decoded_message

encoded_message = encode(user_input,shift_choice)
decoded_message = decode(encoded_message,shift_choice)
print("Encoded message: ",encoded_message)
print("Decoded message: ",decoded_message)