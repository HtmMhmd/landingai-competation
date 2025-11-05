import os
from pathlib import Path
from landingai_ade import AsyncLandingAIADE
from typing import Dict, Any

API_KEY = os.getenv("LANDINGAI_API_KEY")
ENVIRONMENT = os.getenv("LANDINGAI_ENDPOINT", "production")

async def extract_document(file_path: str) -> Dict[str, Any]:
    async with AsyncLandingAIADE(apikey=API_KEY, environment=ENVIRONMENT) as client:
        try:
            response = await client.parse(
                document=Path(file_path),
                model="dpt-2-latest",
            )
            return response.model_dump()
        except Exception as e:
            raise RuntimeError(f"Error calling LandingAI ADE API: {e}") from e
