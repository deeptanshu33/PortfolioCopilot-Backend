from pydantic import BaseModel
from typing import List, Optional

class Metric(BaseModel):
    name: str
    value: float
    description: Optional[str]

class ReportSection(BaseModel):
    title: str
    content: str
    references: List[str]

class PortfolioReport(BaseModel):
    title: str
    ticker: str
    summary: str
    metrics: List[Metric]   
    confidence_score: float
    sections: List[ReportSection]
    recommendation: Optional[str]