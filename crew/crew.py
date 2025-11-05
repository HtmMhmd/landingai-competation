from typing import List, Dict, Any
from crew.tasks import ExtractTask, AnalyzeTask, ReportTask

async def run_crew(file_paths: List[str], analysis_type: str) -> Dict[str, Any]:
    extract_task = ExtractTask()
    analyze_task = AnalyzeTask()
    report_task = ReportTask()
    
    extracted_docs = await extract_task.run(file_paths)
    analysis = await analyze_task.run(extracted_docs, analysis_type)
    report = await report_task.run(analysis)
    
    return {
        "status": "completed",
        "analysis_type": analysis_type,
        "extracted_documents": extracted_docs,
        "analysis": analysis,
        "report_html": report
    }
