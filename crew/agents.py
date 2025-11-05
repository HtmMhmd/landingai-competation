from typing import List, Dict, Any
from services.landing_ai import extract_document
from services.openai_llm import analyze_financial_data

class DocumentExtractorAgent:
    async def run(self, file_paths: List[str]) -> List[Dict[str, Any]]:
        extracted_docs = []
        for path in file_paths:
            raw_data = await extract_document(path)
            extracted_docs.append(raw_data)
        return extracted_docs

class FinancialAnalystAgent:
    async def run(self, extracted_docs: List[Dict[str, Any]], analysis_type: str) -> Dict[str, Any]:
        analysis = await analyze_financial_data(extracted_docs, analysis_type)
        return analysis

class ReportGeneratorAgent:
    async def run(self, analysis: Dict[str, Any]) -> str:
        summary = f"""<html><body><h1>Financial Analysis Report</h1><pre>{analysis}</pre></body></html>"""
        return summary
