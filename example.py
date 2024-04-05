import os

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)


class ChatSession:
    llm: ChatOpenAI
    prompt: ChatPromptTemplate
    memory: ConversationBufferMemory
    conversation: LLMChain

    def __init__(self) -> None:
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo"
        )  # gpt-3.5-turbo you can use any model you want but bigger isn't always better
        self.prompt = ChatPromptTemplate.from_messages(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    "You are a nice chatbot having a conversation with a human."  # You can change this to whatever you want
                ),
                # The `variable_name` here is what must align with memory
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{question}"),
            ]
        )
        self.memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        self.conversation = LLMChain(
            llm=self.llm, prompt=self.prompt, verbose=False, memory=self.memory
        )

    def chat(self, question: str) -> str:
        return self.conversation({"question": question})["text"]

    def get_conversation_string(self) -> str:
        return self.memory.buffer_as_str


def clear_term() -> None:
    os.system("cls||clear")


def main() -> None:
    chat_session = ChatSession()

    while True:
        clear_term()
        print(chat_session.get_conversation_string())
        user_query = input("Human: ")
        if user_query.lower().strip() in {"exit", "quit"}:
            break

        chat_session.chat(user_query)


if __name__ == "__main__":
    main()
