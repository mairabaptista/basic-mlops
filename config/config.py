from dotenv import load_dotenv, dotenv_values
import os

config = dotenv_values('.env')
#config = load_dotenv('.env')

BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME")
BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")

