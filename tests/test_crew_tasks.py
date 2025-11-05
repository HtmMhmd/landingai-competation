import pytest
from crew.tasks import execute_extract_task, execute_analyze_task, execute_report_task
from crew.crew import load_agents_config, load_tasks_config
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
async def test_load_configs():
    agents_config = load_agents_config()
    tasks_config = load_tasks_config()
    
    assert "document_extractor" in agents_config
    assert "financial_analyst" in agents_config
    assert "report_generator" in agents_config
    
    assert "extract_documents" in tasks_config
    assert "analyze_financial_data" in tasks_config
    assert "generate_report" in tasks_config

@pytest.mark.asyncio
async def test_extract_task():
    with patch('crew.agents.extract_document', new_callable=AsyncMock) as mock_extract:
        mock_extract.return_value = {"chunks": [{"text": "Sample loan data"}]}
        
        result = await execute_extract_task(["/path/to/sample.pdf"])
        
        assert len(result) == 1
        assert "chunks" in result[0]

@pytest.mark.asyncio
async def test_analyze_task():
    with patch('crew.agents.analyze_financial_data', new_callable=AsyncMock) as mock_analyze:
        mock_analyze.return_value = {
            "analysis_type": "Loan Risk Score",
            "analysis": "Low risk borrower"
        }
        
        extracted_docs = [{"chunks": [{"text": "Sample data"}]}]
        result = await execute_analyze_task(extracted_docs, "Loan Risk Score")
        
        assert result["analysis_type"] == "Loan Risk Score"
        assert "analysis" in result

@pytest.mark.asyncio
async def test_report_task():
    analysis = {
        "analysis_type": "Loan Risk Score",
        "analysis": "Low risk borrower"
    }
    result = await execute_report_task(analysis)
    
    assert "<!DOCTYPE html>" in result
    assert "Financial Analysis Report" in result
