import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

# .env file load karo
load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def generate_content(prompt: str, content_type: str = "blog", tone: str = "professional") -> str:
    """
    Generate AI content using OpenAI GPT
    """
    system_prompt = f"""You are an expert content writer. 
Generate {content_type} content in a {tone} tone.
Make it engaging, well-structured, and informative."""

    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        raise Exception(f"OpenAI API Error: {str(e)}")
    