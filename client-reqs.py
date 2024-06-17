from openai import AzureOpenAI

deployment_name = '<YOUR_DEPLOYMENT_NAME>'

client = AzureOpenAI(
    azure_endpoint = '<YOUR_ENDPOINT_NAME>',
    api_key = '<YOUR_API_KEY>',
    api_version = '2021-09-01' # Target version
        )

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Azure OpenAI?"}
    ]
)
generated_text = response.choices[0].message.content

# Print the response
print("Response: " + generated_text + "\n")