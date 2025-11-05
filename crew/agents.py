from typing import List, Dict, Any
from services.landing_ai import extract_document
from services.openai_llm import analyze_financial_data
import json

async def extract_documents_tool(file_paths: List[str]) -> List[Dict[str, Any]]:
    extracted_docs = []
    for path in file_paths:
        raw_data = await extract_document(path)
        extracted_docs.append(raw_data)
    return extracted_docs

async def analyze_financial_data_tool(extracted_docs: List[Dict[str, Any]], analysis_type: str) -> Dict[str, Any]:
    analysis = await analyze_financial_data(extracted_docs, analysis_type)
    return analysis

async def generate_report_tool(analysis: Dict[str, Any]) -> str:
    analysis_str = json.dumps(analysis, indent=2) if isinstance(analysis, dict) else str(analysis)
    summary = f"""<!DOCTYPE html>
<html>
<head>
    <title>Financial Analysis Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1 {{ color: #2c3e50; }}
        .section {{ margin: 20px 0; padding: 15px; background: #f8f9fa; border-radius: 5px; }}
        pre {{ white-space: pre-wrap; word-wrap: break-word; }}
    </style>
</head>
<body>
    <h1>Financial Analysis Report</h1>
    <div class="section">
        <h2>Analysis Results</h2>
        <pre>{analysis_str}</pre>
    </div>
</body>
</html>"""
    return summary
