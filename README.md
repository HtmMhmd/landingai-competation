# FinDoc Insight

Intelligent agentic application for financial document analysis using LandingAI's Agentic Document Extraction (ADE) and OpenAI LLM.

## Overview

FinDoc Insight is designed for financial analysts and loan officers to extract, analyze, and understand complex financial documents such as loan applications and SEC filings. It uses CrewAI to orchestrate document extraction, analysis, and report generation.

## Architecture

```
User -> FastAPI Backend -> CrewAI Orchestrator
       ↳ LandingAI ADE (document extraction)
       ↳ OpenAI LLM (reasoning / analysis)
```

## Technology Stack

- Backend: FastAPI, Pydantic
- Orchestration: CrewAI
- Document Extraction: LandingAI ADE Python SDK
- LLM Analysis: OpenAI API (gpt-4o-mini)
- Deployment: Docker, Docker Compose
- CI/CD: GitHub Codespaces ready

## Project Structure

```
.
├── app/
│   └── main.py              # FastAPI application
├── crew/
│   ├── agents.py            # CrewAI agents
│   ├── tasks.py             # CrewAI tasks
│   └── crew.py              # Crew orchestration
├── services/
│   ├── landing_ai.py        # LandingAI ADE wrapper
│   └── openai_llm.py        # OpenAI LLM wrapper
├── tests/
│   ├── test_crew_tasks.py   # Unit tests
│   └── sample_docs/         # Sample financial PDFs
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Setup

### Prerequisites

- Docker and Docker Compose installed
- OpenAI API key
- LandingAI API key

### Environment Variables

Copy `.env.example` to `.env` and add your keys:

```bash
cp .env.example .env
```

Edit `.env`:

```
OPENAI_API_KEY=your_openai_api_key_here
LANDINGAI_API_KEY=your_landingai_api_key_here
LANDINGAI_ENDPOINT=production
```

### Running with Docker

```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`

### Running Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Usage

### Health Check

```bash
curl http://localhost:8000/health
```

### Analyze Documents

```bash
curl -X POST http://localhost:8000/analyze \
  -F "files=@loan_application.pdf" \
  -F "analysis_type=Loan Risk Score"
```

Analysis types:
- `Loan Risk Score`
- `Covenant Extraction`
- `SEC Filing Summary`

## Testing

Run tests:

```bash
pytest tests/test_crew_tasks.py
```

Download sample financial documents from `tests/sample_docs/README.md` for testing.

## GitHub Codespaces

This project is configured for GitHub Codespaces. Simply:

1. Open the repository in GitHub
2. Click "Code" → "Codespaces" → "Create codespace"
3. Wait for the environment to build
4. Set your environment variables
5. Run `docker-compose up`

## Development

The project uses async/await throughout for optimal performance. Key components:

- **LandingAI ADE**: Extracts structured data from PDFs
- **OpenAI LLM**: Analyzes extracted data with financial expertise
- **CrewAI**: Orchestrates the workflow between agents

## License

MIT
