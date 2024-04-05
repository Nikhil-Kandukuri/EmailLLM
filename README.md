# LLM Chatbot with Email Sending Capability

## What you implemented?

I implemented an LLM chatbot based on the newly released Gemini-pro model by Google which achieves great performance on widely used Academic Benchmarks. The UI stores the chat history making it convenient for the user to interact with the LLM-based chatbot. The main feature that this bot will be able to do is send an email on behalf of the user. Typing "send mail to example@gmail.com" or "send email to example@gmail.com" prompts the LLM chatbot to send the previously drafted email message to the specified email-id. The same feature can be invoked by the initiate button as well. The application also does some checks on missing inputs and does regex pattern matching to validate the email address you provide. I wanted to implement the email feature because we often ask an LLM to generate drafts of emails and having the ability to actually send out the email would be greatly beneficial. Some of the issues were related to the privacy of the email we used to send out the email from as I was not using any secret manager as such and was using the passwords directly in the code.

## What you would do next?

If there was more time, it would make sense to authenticate a user logging into the application and then set up the email of that particular user. Right now, we have the configuration in the code and would have to be changed for each user.
It would also be a natural extension to deploy the application on the cloud using a container orchestration framework like Kubernetes which could horizontally scale our application, and if there are many users using our application, it could help load balance the application. Given more time, I would also explore chaining different commands together in the LLM and making the application more useful. Also, the current implementation of sending an email through conversation is through regex matching, a more broad set of rules would make the system more robust.

## Analysis of your features

The application provides two ways of sending an email. One method is initiated by a click where we fill in the details like receiver email, subject, and body from our conversation with the LLM. The other method is through conversation with the LLM, "send mail to xyz@gmail.com". The latency of our application is dependent on the network latency as there are two main API calls taking place. The first API call is the call to the Google server to get a response for their Gemini API. The second API call is to send the mail by logging in to the email and filling out the details like subject and body. The feature works as expected and is swiftly able to send emails, an important feature that an LLM-based chatbot could possess. However, in the case of conversing with the LLM and using the conversation history to send out the email automatically, there are a variety of ways that the email could have been framed. Regular expressions can only capture a fraction of these possibilities where subject and body are clearly demarcated. A limitation would be that we cannot send emails with attachments in this application. Accuracy in the case of sending out the email could be mentioned in terms of word error rate of the ideal message you wanted to send out versus the mail you receive through the LLM chatbot. The number of successfully sent emails in a given timespan could be another metric to measure accuracy. Contextual accuracy by the LLM to correctly draft emails and user satisfaction are other performance metrics that can be given merit.

## How to run the application?

You will need to pip install the following dependencies:

pip install -q -U google-generativeai
pip install Flask
pip install Flask-SocketIO

To run this application, you will need to get a Google API key at the following link https://ai.google.dev/ and replace the `YOUR_GOOGLE_API_KEY` with your API key.
You will need to replace `YOUR_EMAIL_ID` with the email id you want the emails to be sent from.
The password will not be your normal email password.
You will have to generate a Gmail app password at https://myaccount.google.com/. Go to the security tab and proceed to the 2-step verification section. Scroll to the bottom where you will see a section called app password. Generate your app password and replace the field `YOUR_EMAIL_APP_PASSWORD` in the code. Now you are all set to run the application!

python llm-chatbot.py

The `templates` directory contains the HTML code for the UI.
`llm-chatbot.py` is the Python Flask application, and you can start the application by entering the following command:
