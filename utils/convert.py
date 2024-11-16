import sample_pb2  # Import the generated module

# Create an instance of TextMessage
example = sample_pb2.Example()
text = open("sample.txt",'r').read()
print(text)

# Serialize the message to a binary format
binary_data = message.SerializeToString()

# Optionally, print the binary data as hex for inspection
print(binary_data.hex())
