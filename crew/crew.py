import os
import yaml
from typing import List, Dict, Any
from pathlib import Path
from crew.tasks import execute_extract_task, execute_analyze_task, execute_report_task

def load_agents_config() -> Dict[str, Any]:
    config_path = Path(__file__).parent / "agents.yaml"
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def load_tasks_config() -> Dict[str, Any]:
    config_path = Path(__file__).parent / "tasks.yaml"
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

async def run_crew(file_paths: List[str], analysis_type: str) -> Dict[str, Any]:
    agents_config = load_agents_config()
    tasks_config = load_tasks_config()
    
    extracted_docs = await execute_extract_task(file_paths)
    
    analysis = await execute_analyze_task(extracted_docs, analysis_type)
    
    report = await execute_report_task(analysis)
    
    return {
        "status": "completed",
        "analysis_type": analysis_type,
        "agents_used": list(agents_config.keys()),
        "tasks_executed": list(tasks_config.keys()),
        "extracted_documents": extracted_docs,
        "analysis": analysis,
        "report_html": report
    }
