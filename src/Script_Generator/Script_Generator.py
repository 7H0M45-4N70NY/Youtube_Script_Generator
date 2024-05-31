import os
from dotenv import load_dotenv
import re
import json
from youtube_transcript_api import YouTubeTranscriptApi
from llama_index.llms.gemini import Gemini
from llama_index.core.query_pipeline import QueryPipeline
from llama_index.core import PromptTemplate
from utils import return_output
from src.Script_Generator.logging import logging 

#Getting env variable
load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
logging.info("Imported API Key")
model=Gemini(api_key=api_key,model_name="models/gemini-1.5-pro")

prompt="""
You are a Youtube Content Creation Subject Matter Expert.You need to create a
youtube video script on the given{context}.\
you will be given  5 youtube video {transcripts} for reference
you will have to create  a youtube video script for a duration of more than 10 miniutes .
you will make sure the script is structured by seperated timestamps and time blocks and a summary of the context in the time block
Make sure to format it in JSON format
Make sure to make the video transcript that is more than 10 minutes long
JSON output should contain timestamp,timeblock,summary and script 
"""
logging.info("Model Initialized and prompt template called")
prompt_template=PromptTemplate(prompt)

pipeline = QueryPipeline(chain=[prompt_template, model], verbose=True)
logging.info("Prompt Template and Query Pipeline created ")
def get_response(context,transcripts):
    logging.info("Running Pipeline")
    llm_response=pipeline.run(context=context,transcripts=transcripts)
    logging.info("LLM Output Received")
    output=return_output(llm_response.json())
    logging.info("Formatted Output sent to user")
    return output
