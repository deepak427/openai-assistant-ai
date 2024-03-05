from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

