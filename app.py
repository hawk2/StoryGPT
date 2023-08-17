import openai
import time

openai.api_key = 'Your API key here'

print("Welcome to StoryGPT!")
time.sleep(2)
print("I will need a key inputs about yourself.")
time.sleep(2)
name = input("What is your name?")
time.sleep(2)
hobbies = input("What do you like to do?")
time.sleep(3)
friends = input("What are/is the names of your friend(s)?")
time.sleep(3)
print("Generating...")
time.sleep(5)
print("An exiting story takes hard work")
time.sleep(5)
print("Any minute now")
time.sleep(10)
print("Almost done")



story_response = openai.ChatCompletion.create(
  model="gpt-4",  
  messages=[
        {"role": "system", "content": "You are a children story teller. You write in standard English. You use perfect grammar. You must use capital letters at the beginning of each sentence."},
        {"role": "user", "content": f"Write a story about {name}. {name} likes to {hobbies}. {name}'s best friends are/is {friends}."},
    ]
)

story = story_response['choices'][0]['message']['content']
print("...and ")
time.sleep(1)
print("Done")
print(story)
# Generate a DALL·E prompt
prompt_response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
        {"role": "system", "content": "You read stories and then generate a prompt for DALL·E about the stories. Must be kid friendly. Specify no text. Use a cartoon style."},
        {"role": "user", "content": f"Make a DALL·E prompt for this story: {story}"},
    ]
)

iprompt = prompt_response['choices'][0]['message']['content']

# Generate an image
image_response = openai.Image.create(
  prompt=iprompt,
  n=1,
  size="1024x1024"
)

# Save the URL of the generated image
image_url = image_response['data'][0]['url']

print(f"Generated image URL: {image_url}\nPrompt used for DALL·E: {iprompt}")
