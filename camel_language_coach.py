from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.models.groq_model import GroqModel
from camel.types import RoleType


class CamelLanguageCoach:
    def __init__(self, language: str = "English", groq_api_key: str = ""):
        self.language = language
        self.system_prompt = (
            f"You are a friendly and patient language coach helping users learn {language}. "
            f"Correct mistakes and explain grammar and vocabulary in simple terms."
        )
        self.history = []

        # Initialize the Groq model
        self.model = GroqModel(
            model_type="meta-llama/llama-4-maverick-17b-128e-instruct",
            api_key=groq_api_key
        )

        print("Available roles in RoleType:", RoleType.__members__)


        self.chat_agent = ChatAgent(
            system_message=self.system_prompt,
            model=self.model
        )

        if 'SYSTEM' in RoleType.__members__:
            self._append_message(RoleType.SYSTEM, self.system_prompt) 
        else:
            print("SYSTEM role not found, using 'ASSISTANT' role.")
            self._append_message(RoleType.ASSISTANT, self.system_prompt) 

    def _append_message(self, role_type, content):
        if not content.strip():
            return
        self.history.append(BaseMessage(
            role_name=role_type.name,
            role_type=role_type,
            content=content,
            meta_dict={}  
        ))

    def chat(self, user_input: str) -> str:
        if not user_input.strip():
            return "Please enter something to practice."


        user_msg = BaseMessage(
            role_name=RoleType.USER.name,
            role_type=RoleType.USER,
            content=user_input,
            meta_dict={}
        )
        self.history.append(user_msg)


        assistant_response = self.chat_agent.step(user_msg)


        try:
            if hasattr(assistant_response, "msg") and hasattr(assistant_response.msg, "content"):
                return assistant_response.msg.content
            else:
                return "Sorry, I couldn't extract a valid response."
        except Exception as e:
            print("⚠️ Error extracting response:", e)
            return "Sorry, I couldn't find a valid response."
