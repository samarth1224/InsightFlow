from google.genai import Client
from google.genai.client import AsyncClient
from google.genai import types
import os


# API_KEY = os.getenv("GEMINI_API_KEY")
# client = Client(api_key=API_KEY,http_options=types.HttpOptions(api_version='v1alpha'))
# # generate content with the tuned model
# response = client.models.generate_content(
#     model="gemini-2.5-Flash",
#     contents='tell me about sun in short',
# )





class Summarize(Client):
    SHORT_SUMMARY_SYSTEM_PROMPT = "Create a short and concise summary of the given prompt.Make sure it covers all relevant information."
    LONG_SUMMARY_SYSTEM_PROMPT = '''Create a summary of the given prompt.Make it as long as required to cover necessary information.
                                    DO NOT EXCEED THE LENGHT OF ORIGINAL PROMPT.'''
    BULLET_SUMMARY_SYSTEM_PROMPT = '''Generate a summary of the given prompt in bullet point formate. Keep it concise.'''
    def __init__(self,api_key: str):
        super().__init__(api_key=api_key)

    def _get_system_prompt(self,type: str):
        if type.lower() == 'short':
            return self.SHORT_SUMMARY_SYSTEM_PROMPT
        elif type.lower() == 'long':
            return self.LONG_SUMMARY_SYSTEM_PROMPT
        elif type.lower() == 'bullet':
            return  self.BULLET_SUMMARY_SYSTEM_PROMPT

    async def summarize_text(self,text: str,type: str):
        print('yes')
        system_prompt = self._get_system_prompt(type = type)

        try:
            summary = await self.aio.models.generate_content(model="gemini-2.5-flash",
                                     contents = text,
                                     config= types.GenerateContentConfig(
                                        system_instruction = system_prompt
                                     )
                                     )
            print(f'summary in sumamr = {summary.text}')
            return summary.text
        except Exception as  e:
            return e

# models/embedding-gecko-001
# models/gemini-1.0-pro-vision-latest
# models/gemini-pro-vision
# models/gemini-1.5-pro-latest
# models/gemini-1.5-pro-002
# models/gemini-1.5-pro
# models/gemini-1.5-flash-latest
# models/gemini-1.5-flash
# models/gemini-1.5-flash-002
# models/gemini-1.5-flash-8b
# models/gemini-1.5-flash-8b-001
# models/gemini-1.5-flash-8b-latest
# models/gemini-2.5-pro-preview-03-25
# models/gemini-2.5-flash-preview-04-17
# models/gemini-2.5-flash-preview-05-20
# models/gemini-2.5-flash
# models/gemini-2.5-flash-preview-04-17-thinking
# models/gemini-2.5-flash-lite-preview-06-17
# models/gemini-2.5-pro-preview-05-06
# models/gemini-2.5-pro-preview-06-05
# models/gemini-2.5-pro
# models/gemini-2.0-flash-exp
# models/gemini-2.0-flash
# models/gemini-2.0-flash-001
# models/gemini-2.0-flash-exp-image-generation
# models/gemini-2.0-flash-lite-001
# models/gemini-2.0-flash-lite
# models/gemini-2.0-flash-preview-image-generation
# models/gemini-2.0-flash-lite-preview-02-05
# models/gemini-2.0-flash-lite-preview
# models/gemini-2.0-pro-exp
# models/gemini-2.0-pro-exp-02-05
# models/gemini-exp-1206
# models/gemini-2.0-flash-thinking-exp-01-21
# models/gemini-2.0-flash-thinking-exp
# models/gemini-2.0-flash-thinking-exp-1219
# models/gemini-2.5-flash-preview-tts
# models/gemini-2.5-pro-preview-tts
# models/learnlm-2.0-flash-experimental
# models/gemma-3-1b-it
# models/gemma-3-4b-it
# models/gemma-3-12b-it
# models/gemma-3-27b-it
# models/gemma-3n-e4b-it
# models/gemma-3n-e2b-it
# models/embedding-001
# models/text-embedding-004
# models/gemini-embedding-exp-03-07
# models/gemini-embedding-exp
# models/aqa
# models/imagen-3.0-generate-002
# models/imagen-4.0-generate-preview-06-06
# models/imagen-4.0-ultra-generate-preview-06-06
# models/veo-2.0-generate-001
# models/gemini-2.5-flash-preview-native-audio-dialog
# models/gemini-2.5-flash-exp-native-audio-thinking-dialog
# models/gemini-2.0-flash-live-001
# models/gemini-live-2.5-flash-preview