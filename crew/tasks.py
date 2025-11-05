from typing import List, Dict, Any
from crew.agents import DocumentExtractorAgent, FinancialAnalystAgent, ReportGeneratorAgent

class ExtractTask:
    async def run(self, file_paths: List[str]) -> List[Dict[str, Any]]:
        extractor = DocumentExtractorAgent()
        return await extractor.run(file_paths)

class AnalyzeTask:
    async def run(self, extracted_docs: List[Dict[str, Any]], analysis_type: str) -> Dict[str, Any]:
        analyst = FinancialAnalystAgent()
        return await analyst.run(extracted_docs, analysis_type)

class ReportTask:
    async def run(self, analysis: Dict[str, Any]) -> str:
        reporter = ReportGeneratorAgent()
        return await reporter.run(analysis)
