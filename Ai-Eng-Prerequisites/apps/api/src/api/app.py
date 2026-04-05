from fastapi import FastAPI, Request
from pydantic import BaseModel

from openai import OpenAI
from groq import Groq
from google import genai

from api.core.config import config

import logging