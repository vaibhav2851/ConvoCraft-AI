import google.generativeai as palm
question ='add two numbers'

# #
# # # Set the API key
#
palm.configure(api_key="AIzaSyCSoCxhyLtx4iKUtxCrdbL-U0dvtydeMKQ")
# #
# # # Generate text
# # promp = "Write code of prime number "
response = palm.chat(messages=question)
#
# # Print the response
result = response.last
print(result)
