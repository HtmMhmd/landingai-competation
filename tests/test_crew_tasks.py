import pytest
from crew.tasks import ExtractTask, AnalyzeTask, ReportTask
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
async def test_extract_task():
    with patch('crew.agents.extract_document', new_callable=AsyncMock) as mock_extract:
        mock_extract.return_value = {"chunks": [{"text": "Sample loan data"}]}
        
        task = ExtractTask()
        result = await task.run(["/path/to/sample.pdf"])
        
        assert len(result) == 1
        assert "chunks" in result[0]

@pytest.mark.asyncio
async def test_analyze_task():
    with patch('crew.agents.analyze_financial_data', new_callable=AsyncMock) as mock_analyze:
        mock_analyze.return_value = {
            "analysis_type": "Loan Risk Score",
            "analysis": "Low risk borrower"
        }
        
        task = AnalyzeTask()
        extracted_docs = [{"chunks": [{"text": "Sample data"}]}]
        result = await task.run(extracted_docs, "Loan Risk Score")
        
        assert result["analysis_type"] == "Loan Risk Score"
        assert "analysis" in result

@pytest.mark.asyncio
async def test_report_task():
    task = ReportTask()
    analysis = {
        "analysis_type": "Loan Risk Score",
        "analysis": "Low risk borrower"
    }
    result = await task.run(analysis)
    
    assert "<html>" in result
    assert "Financial Analysis Report" in result
