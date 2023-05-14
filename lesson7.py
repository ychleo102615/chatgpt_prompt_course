import getCompletion as GetCompletion

get_completion = GetCompletion.get_completion
get_completion_from_messages = GetCompletion.get_completion_from_messages


def context1():
    messages =  [
            {'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},
            {'role':'user', 'content':'tell me a joke'},
            {'role':'assistant', 'content':'Why did the chicken cross the road'},
            {'role':'user', 'content':'I don\'t know'}  ]

    response = get_completion_from_messages(messages, temperature=1)
    print(response)

# context1()

def context2():
    messages =  [
    {'role':'system', 'content':'You are friendly chatbot.'},
    {'role':'user', 'content':'Hi, my name is Isa'}  ]
    response = get_completion_from_messages(messages, temperature=1)
    print(response)

# context2()

def context3():
    messages =  [
    {'role':'system', 'content':'You are friendly chatbot.'},
    {'role':'user', 'content':'Yes,  can you remind me, What is my name?'}  ]
    response = get_completion_from_messages(messages, temperature=1)
    print(response)

def context4():
    messages =  [
    {'role':'system', 'content':'You are friendly chatbot.'},
    {'role':'user', 'content':'Hi, my name is Isa'},
    {'role':'assistant', 'content': "Hi Isa! It's nice to meet you. \
    Is there anything I can help you with today?"},
    {'role':'user', 'content':'Yes, you can remind me, What is my name?'}  ]
    response = get_completion_from_messages(messages, temperature=1)
    print(response)

# context4()
