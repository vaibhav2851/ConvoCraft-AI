import google.generativeai as palm

# Set the API key
palm.configure(api_key="AIzaSyCSoCxhyLtx4iKUtxCrdbL-U0dvtydeMKQ")

# Generate text
promp = "Write code of prime number "
response = palm.chat(messages=promp)

# Print the response
print(response.last)