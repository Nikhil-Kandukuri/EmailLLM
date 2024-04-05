# Take Home Project

## Overview

This project is designed to give you a chance to show off your coding skills and give us a chance to see how you work. However, we're mostly concerned with your analytical ability and thoughtfulness. We don't expect you to have done anything like this before, but we do expect you to be able to learn new things and apply them to your work. Please don't spend more than 4 hours on this project. If you don't finish everything you planned on doing, that's ok, you can tell us what you would have done if you had more time. Just try to have something working that we can run. This role is as much about thinking deeply about a problem as it is about coding up a solution. There are no right or wrong answers and no trick questions. If you try something and it doesn't work, that's ok, just tell us what you tried and why you think it didn't work. We're looking for people who are thoughtful and curious.

## The Problem

Build a chatbot! This is the easy part. There are TONS of tutorials on the web, in fact, we've included a little example for you in `example.py`. We made the example using [LangChain](https://python.langchain.com/docs/get_started/introduction) which is a Python library for building LLM systems but you can use whatever you want if you think it will make your life easier. Your task is to add features to a simple chat bot. What those features are is totally up to you but we've included some ideas below. You can use the example as a starting point or you can start from scratch. If you do use the example, you'll need to install the requirements in `requirements.txt` and use a python version `>=3.10` (or just modify some of the typing annotations). You'll also need to set the `OPENAI_API_KEY` environment variable (we'll provide you one for this exercise). If you've used type annotations in python before, great but if not, there's no need to worry about typing your code.

## Feature ideas

- Have the LLM do something on behalf of the user like send an email, make an API call, etc. (Hint: having the LLM respond in a structured way will make this easier)
- Chain a few LLM calls together to do more complex things. Maybe you want to ask the LLM to do something, and then ask it to do something else based on the result of the first thing.
- Do some type of validation on the user input before sending it to the LLM or maybe do some validation on the LLM response before sending it to the user. If you want an LLM to do something like send an email, you might want to validate that the email address is valid and return the error to the LLM if it's not before responding back to the user.
- Extend memmory in some way. It might not be the best practice to pass everything to the LLM as chat history. For example, how might I store an API response in memmory and use it later in the conversation without just passing the whole thing to the LLM each time?
- Literally anything else you can think of! We're not looking for anything in particular, just do something that you think is interesting.

## Write up

Please don't use an LLM to write your writeup. We look at LLM generated text all day. We're not looking for a novel, just a few sentences for each section is fine. Communicating your thinking effectively is more important than the length, format, or style of your writeup.

### What you implemented (2-5 sentences)

In addition to the code, we'd like you to write up a short description of what you actually implemented. What features did you add? Why did you choose those features? What challenges did you run into?

### What you would do next (2-5 sentences)

If you had more time, what would you do next? What features would you add? What would you change about your implementation? What would you do differently?

### Analysis of your features (4+ sentences)

How well do your features work? What are the limitations? What are some edge cases that might cause problems? How might you think about quantifying the performance of your features or the system at large? Some things are easier to measure like latency and token usage but other things like accuracy are harder to measure. How might you think about measuring accuracy? What are some other metrics you might want to measure and why would those metrics be useful?

## Deliverables

- A working chatbot that we can run and interact with. Don't waste time on a fancy UI, we just want to see the chatbot working.
- A WRITEUP.md file that explains how to run your chat bot and answers the questions above.
- If you want to make a private repo, you can add `@aidandonohue` as a collaborator. Otherwise, you can just send us a zip file with your code and writeup to `aidan@raylu.dev`.
