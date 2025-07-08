from google.genai import Client
from google.genai.client import AsyncClient
from google.genai import types
import os

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

    async def summarize_text(self,text: str,summary_type: str):

        system_prompt = self._get_system_prompt(type = summary_type)
        try:
            summary = await self.aio.models.generate_content(model="gemini-2.5-flash",
                                     contents = text,
                                     config= types.GenerateContentConfig(
                                        system_instruction = system_prompt
                                     )
                                     )
            return summary.text
        except Exception as  e:
            return e


    async def summarize_document(self, file ,summary_type: str):

            prompt = self._get_system_prompt(type=summary_type)

            try:
                self.files.upload(file=file)
            except Exception as e:
                return f'failed to upload of file.ERROR {e}'

            try:
                summary = await self.aio.models.generate_content(model="gemini-2.5-flash",
                                             content=[file,prompt])
                return summary.text
            except Exception as e:
                return e

