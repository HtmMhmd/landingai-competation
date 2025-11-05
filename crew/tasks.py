from typing import List, Dict, Any
from crew.agents import extract_documents_tool, analyze_financial_data_tool, generate_report_tool

async def execute_extract_task(file_paths: List[str]) -> List[Dict[str, Any]]:
    return await extract_documents_tool(file_paths)

async def execute_analyze_task(extracted_docs: List[Dict[str, Any]], analysis_type: str) -> Dict[str, Any]:
    return await analyze_financial_data_tool(extracted_docs, analysis_type)

async def execute_report_task(analysis: Dict[str, Any]) -> str:
    return await generate_report_tool(analysis)
