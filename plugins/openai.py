from errbot import BotPlugin, botcmd
import openai


class OpenAI(BotPlugin):
    """ Opsgenie management plugin """

    def get_configuration_template(self):
        return {"API_KEY": "", "MODEL": "gpt-3.5-turbo"}

    def check_configuration(self, config):
        if config is None:
            return

        if not config.get("API_KEY"):
            raise ValueError("Missing API key")

        super().check_configuration(config)

    def activate(self):
        """
        Errbot activate() function.
        """
        if not self.config:
            self.log.warn("Plugin is not configured, won't activate.")
            return

        try:
            openai.api_key = self.config.get("API_KEY")
            self.sessions = {}
            super().activate()
        except Exception as e:
            self.log.error(f"activate: unhandled exception: {e}")

    def get_session(self, user):
        if user not in self.sessions:
            # initialize with prompt
            self.sessions[user] = [
                {"role": "system", "content": "You are a helpful assistant."}
            ]
        return self.sessions[user]

    # ---------------

    @botcmd
    def ask_chatgpt(self, msg, question):
        """Ask a question to OpenAI's GPT-3."""
        if not question:
            return ":x: Please enter a question."

        session = self.get_session(msg.frm.person)
        session.append({"role": "user", "content": question})
        prompt = f"Q: {question}\nA:"

        response = openai.ChatCompletion.create(
            model=self.config.get("MODEL"),  # The name of the OpenAI chatbot model to use
            messages=session,       # The conversation history up to this point, as a list of dictionaries
            max_tokens=3800,        # The maximum number of tokens (words or subwords) in the generated response
            stop=None,              # The stopping sequence for the generated response, if any (not used here)
            temperature=0.7,        # The "creativity" of the generated response (higher temperature = more creative)
        )

        answer = None

        for choice in response.choices:
            if "text" in choice:
                answer = choice.text
                break

        if not answer:
            answer = response.choices[0].message.content
            # answer = response.choices[0].text.strip()[2:] # Remove "A:" prefix

        # keep response
        session.append({"role": "assistant", "content": answer})
        return answer

    @botcmd
    def reset_chatgpt(self, msg, args):
        """Reset your GPT-3 session."""
        user = msg.frm.person
        if user in self.sessions:
            del self.sessions[user]
        return "Your ChatGPT session has been reset."
