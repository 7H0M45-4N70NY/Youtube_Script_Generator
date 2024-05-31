import re
import json
from youtube_transcript_api import YouTubeTranscriptApi
from src.Script_Generator.logging import logging 

def extract_id(video_url):
  """Extracts the video ID from a YouTube URL.

  Args:
      video_url: The YouTube URL string.

  Returns:
      The extracted video ID or None if not found.
  """
  id = None
  try:
    id = re.search(r"(?<=v=)([^&]+)", video_url)
  except:
    pass  # Silently ignore the exception for "v=" case
  if id is None:
    try:
      id = re.search(r"(?<=be\/)([^\?]+)", video_url)
    except:
      pass  # Silently ignore the exception for "be/" case
  return id if id else None


def return_output(json_file):
  json_dict=json.loads(json_file)
  output=json_dict['message']['content']
  return output

def get_transcripts(urls):
  """
  This code takes list of urls
  outputs list of transcripts of the youtube video
  """
  video_ids=[extract_id(i)[0] for i in urls]
  youtube_transcripts=YouTubeTranscriptApi.get_transcripts(video_ids, languages=['en'])
  unprocessed_transcripts_set=[]
  for i in video_ids:
    unprocessed_transcripts_set.append(youtube_transcripts[0][i])
  processed_transcripts_set=[]
  for the_transcript in unprocessed_transcripts_set:
        processed_transcripts_set.append("".join([x['text'] for x in the_transcript]))
  return processed_transcripts_set


#

