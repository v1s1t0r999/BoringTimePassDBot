from discord import Intents
import os
# Constants Variables

prefix = ["-"] # multiple prefixes?? Eww
github_token = os.getenv("gtk") # How-To?: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
github_repo = os.getenv("repo")
github_email = os.getenv("ghemail")
github_username = os.getenv("ghusername")
intents = Intents.all() # Or whatever you want
token = os.getenv("dtk") # Don't as how....or gtfo
