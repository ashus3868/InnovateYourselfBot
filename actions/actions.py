# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import Restarted
from rasa_sdk.executor import CollectingDispatcher

from bot_authonticate import authenticate

data={
    "VIDEO":{
        "RASA":"https://youtube.com/playlist?list=PLtFHvora00y8NBwCMoNnPqii-y2-gyl5p",
        "PYTHON":"https://youtube.com/playlist?list=PLtFHvora00y9H1c_AYR4oindX7TOyAXPR",
        "IOT":"https://www.youtube.com/watch?v=DZHhMR3ViFg&list=PLtFHvora00y-7r-yFzWKK3CPofn-Hk_Zc"
    },
    "BLOGS":{
        "RASA":"https://innovationyourself.com/category/rasa-chatbot/",
        "PYTHON":"https://innovationyourself.com/category/python-programming/",
        "IOT":"https://innovationyourself.com/category/nodemcu-esp32/"
    }
}

class ActionShowContent(Action):

    def name(self) -> Text:
        return "action_show_content"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_check")
        content,technology=tracker.get_slot("content_type"),tracker.get_slot("technology")
        out=data[content.upper()][technology.upper()]
        dispatcher.utter_message(text="We have searched the best content as per you to start from the scratch. "
                                      "You can check the content [here]({}) and start innovating. 😍".format(out))
        dispatcher.utter_message("Is there anything else that I can hep you with?")

        return []

class ActionRestart(Action):

    def name(self) -> Text:
      return "action_restart"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

      return [Restarted()]

class ActionAuthenticate(Action):

    def name(self) -> Text:
      return "action_authenticate"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

      dispatcher.utter_message(response="utter_greet")
      # custom behavior
      # x = authenticate()
      # while True:
      #     with open("authenticate.txt") as file:
      #         if file.read() == "1":
      dispatcher.utter_message(response="utter_content")
              #     break
              # else:
              #     dispatcher.utter_message("Sorry, You are not Authorised to start the conversation.")
              #     break
      return []