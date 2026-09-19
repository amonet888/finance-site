from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ArticleData:
    id: str
    category: str  # "Credit", "Investing", or "Savings"
    title: str
    read_time: str
    author_info: str
    intro_text: str
    mid_text: str
    closing_text: str
    head_image_label: str
    paragraph_photo_label: str
    sources: List[str]

