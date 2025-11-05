# Sample Financial Documents for Testing

## Public Financial Documents

### 1. Small Business Loan Application
- **URL**: https://www.bankcom.com.ph/wp-content/uploads/2018/03/Small-Business-Loan-Application-Form-2.pdf
- **Description**: Detailed loan application with financial statements and business information
- **Test Use**: Loan Risk Score analysis

### 2. SEC Form 10-K
- **URL**: https://www.sec.gov/files/form10-k.pdf
- **Description**: Official annual report filing template
- **Test Use**: SEC Filing Summary analysis

### 3. Personal Loan Application
- **URL**: https://www.accessbankplc.com/access/media/Media-PDF-Attachment/Personal-Loan-Application-Form.pdf
- **Description**: Personal loan application with financial details
- **Test Use**: Covenant Extraction analysis

## Testing Instructions

1. Download these PDFs to `tests/sample_docs/`
2. Run tests with: `pytest tests/test_crew_tasks.py`
3. Test the API manually by uploading these documents to `/analyze` endpoint

## Expected Outputs

Each document should return:
- Extracted structured data (tables, key-value pairs)
- Financial analysis based on analysis type
- HTML report summary
