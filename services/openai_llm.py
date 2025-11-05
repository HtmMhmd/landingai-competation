import os
from openai import AsyncOpenAI
from typing import List, Dict, Any

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are a senior financial analyst. Given the structured financial data extracted from documents, generate a detailed analysis focusing on the requested analysis type. Provide clear, concise insights and highlight key financial metrics."""

async def analyze_financial_data(extracted_docs: List[Dict[str, Any]], analysis_type: str) -> Dict[str, Any]:
    content = f"Analysis Type: {analysis_type}\nData: {extracted_docs}"
    
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": content}
        ]
    )
    
    return {
        "analysis_type": analysis_type,
        "analysis": response.choices[0].message.content,
        "extracted_docs": extracted_docs
    }
