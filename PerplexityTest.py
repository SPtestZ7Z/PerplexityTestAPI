#pip install perplexityai

#basic test of perplexity API

from dotenv import load_dotenv
import os
from perplexity import Perplexity

# Load variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("PERPLEXITY_API_KEY")

if not api_key:
    raise SystemExit("PERPLEXITY_API_KEY not set. Add it to .env or set the environment variable.")

client = Perplexity(api_key=api_key)  # pass API key explicitly

completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "List the major ways that AI developments are shaping careers in education, providing a list of trends and drivers, quantified and validated where possible from research. At the end provide a list of references in APA style."
        }
    ],
    model="sonar-pro"
)

print(completion.choices[0].message.content)