from typing import List, Any, Optional, Callable
from pydantic import BaseModel
from ..labeling.assignment import majority_vote, all_labeled_spans

class LabelStrategy(BaseModel):
    """Label strategy for the dataset."""
    is_offensive: Optional[Callable[[List[Any]], Any]] = majority_vote
    is_targeted: Optional[Callable[[List[Any]], Any]] = majority_vote
    targeted_type: Optional[Callable[[List[Any]], Any]] = majority_vote
    toxic_spans: Optional[Callable[[List[Any]], Any]] = all_labeled_spans
    health: Optional[Callable[[List[Any]], Any]] = majority_vote
    ideology: Optional[Callable[[List[Any]], Any]] = majority_vote
    insult: Optional[Callable[[List[Any]], Any]] = majority_vote
    lgbtqphobia: Optional[Callable[[List[Any]], Any]] = majority_vote
    other_lifestyle: Optional[Callable[[List[Any]], Any]] = majority_vote
    physical_aspects: Optional[Callable[[List[Any]], Any]] = majority_vote
    profanity_obscene: Optional[Callable[[List[Any]], Any]] = majority_vote
    racism: Optional[Callable[[List[Any]], Any]] = majority_vote
    religious_intolerance: Optional[Callable[[List[Any]], Any]] = majority_vote
    sexism: Optional[Callable[[List[Any]], Any]] = majority_vote
    xenophobia: Optional[Callable[[List[Any]], Any]] = majority_vote
    