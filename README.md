LLM Chatbot with Email Integration
Overview
I have implemented an LLM chatbot based on the newly released Gemini-pro model by Google, which achieves great performance on widely used Academic Benchmarks. The UI stores the chat history, making it convenient for the user to interact with the LLM-based chatbot. The main feature of this bot is the ability to send an email on behalf of the user. Typing "send mail to example@gmail.com" or "send email to example@gmail.com" prompts the LLM chatbot to send the previously drafted email message to the specified email-id. The same feature can be invoked by the initiate button as well. The application also performs checks on missing inputs and does regex pattern matching to validate the email address provided.
Next Steps
If there was more time, it would make sense to authenticate a user logging into the application and then set up the email of that particular user. Right now, the configuration is in the code and would have to be changed for each user.
It would also be a natural extension to deploy the application on the cloud using a container orchestration framework like Kubernetes, which could horizontally scale our application and help load balance if there are many users using our application. Given more time, I would also explore chaining different commands together in the LLM and making the application more useful. Additionally, the current implementation of sending an email through conversation is through regex matching, and a more broad set of rules would make the system more robust.
Analysis of Features
The application provides two ways of sending an email. One method is initiated by a click, where we fill in the details like receiver email, subject, and body from our conversation with the LLM. The other method is through conversation with the LLM, "send mail to xyz@gmail.com".
The latency of our application is dependent on the network latency, as there are two main API calls taking place. The first API call is the call to the Google server to get a response for their Gemini API. The second API call is to send the mail by logging in to the email and filling out the details like subject and body.
The feature works as expected and is swiftly able to send emails, an important feature that an LLM-based chatbot could possess. However, in the case of conversing with the LLM and using the conversation history to send out the email automatically, there are a variety of ways that the email could have been framed. Regular expressions can only capture a fraction of these possibilities where the subject and body are clearly demarcated. A limitation would be that we cannot send emails with attachments in this application.
Accuracy in the case of sending out the email could be measured in terms of the word error rate of the ideal message you wanted to send out versus the mail you receive through the LLM chatbot. The number of successfully sent emails in a given timespan could be another metric to measure accuracy. Contextual accuracy by the LLM to correctly draft emails and user satisfaction are other performance metrics that can be given merit.
How to Run the Application
You will need to install the following dependencies:
pip install -q -U google-generativeai
pip install Flask
pip install Flask-SocketIO

To run this application, you will need to get a Google API key at the following link https://ai.google.dev/ and replace the YOUR_GOOGLE_API_KEY with your API key.
You will need to replace YOUR_EMAIL_ID with the email ID you want the emails to be sent from. The password will not be your normal email password. You will have to generate a Gmail app password at https://myaccount.google.com/. Go to the security tab and proceed to the 2-step verification section. Scroll to the bottom where you will see a section called "app password". Generate your app password and replace the field YOUR_EMAIL_APP_PASSWORD in the code.
Now you are all set to run the application!
llm-chatbot.py is the Python Flask application, and you can start the application by entering the following command:
python llm-chatbot.py

The templates directory contains the HTML code for the UI.
