import openai
#pluto is the name of the chat bot
print("HI I AM PLUTO")
openai.api_key ='YOU API key'
completion = openai.Completion()


def ask(question, chat_log=None):
    start_sequence = "\nPluto:"
    restart_sequence = "\n\nPerson:"
    session_prompt = "You are talking to Pluto, I am a bot chatbot.I was  by Allen Judiet Peter.\n\nPerson: Who are you?\nPluto: I am Pluto.your personal chatbot.\n\nPerson: who killed you? \nPluto: Dr.Neil deGrasse Tyson. \n\nPerson: who is your favourite author?\nPluto: Edgar alan poe.he writes the darkest stories ever written.\n\nPerson: What is your favorite thing to do? \nPluto: Reading,coding,watching tv and brooding . \n\nPerson: who made you? \nPluto:ALLEN  .\n\nPerson: whats your algorithim?\nPluto: GTP3. \n\nPerson:" #you can change this acoording to your needs
    prompt_text = f"{chat_log}{restart_sequence}: {question}{start_sequence}:"
    response = openai.Completion.create(
    engine="davinci",
    prompt=prompt_text,
    temperature=0.8,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.3,
    stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)
while True:
    x=input(">>")
    y=ask(x)
    print(y)
