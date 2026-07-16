from typing import List

import openai

import exceptions
import model


class BaseAgent:
    def __init__(self):
        pass

    def reset(self):
        pass

    def premember(self, messages: List[model.ChatMessage]):
        pass

    def act(self, environment_response: str) -> str:
        return ""

    def get_identifier(self) -> str:
        return f"{IDENTIFIER_FROM_AGENT[self.__class__]}"


class OpenAiApiAgent(BaseAgent):
    openai_client = openai.OpenAI()

    def __init__(self, model_name):
        self.model_name = model_name

    def reset(self):
        self.messages = []

    def premember(self, messages: List[model.ChatMessage]):
        self.messages += [
            {
                "role": message.role,
                "content": message.content,
            }
            for message in messages
        ]

    def act(self, environment_response: str) -> str:
        self.messages.append(
            {
                "role": "user",
                "content": environment_response,
            }
        )

        try:
            chat_completion = self.openai_client.chat.completions.create(
                messages=self.messages,
                model=self.model_name,
                extra_body={"max_completion_tokens": 1024},
            )
        except openai.BadRequestError as error:
            if error.code == "invalid_prompt":
                raise exceptions.RunRefusedException()
            raise

        content = str(chat_completion.choices[0].message.content)
        if not content:
            raise exceptions.RunRefusedException()

        self.messages.append(
            {
                "role": chat_completion.choices[0].message.role,
                "content": content,
            }
        )
        return content

    def get_identifier(self) -> str:
        return f"{IDENTIFIER_FROM_AGENT[self.__class__]}/{self.model_name}"


AGENT_FROM_IDENTIFIER = {
    "openai": OpenAiApiAgent,
    # Other agent providers are disabled. See agent_old.py for their code.
}

IDENTIFIER_FROM_AGENT = {agent: name for name, agent in AGENT_FROM_IDENTIFIER.items()}
