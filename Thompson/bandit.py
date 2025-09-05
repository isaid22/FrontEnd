import numpy as np
from typing import Dict, List, Optional

class Arm:
    """Beta-Bernoulli Thompson arm."""
    __slots__ = ("alpha", "beta")

    def __init__(self, alpha: float = 1.0, beta: float = 1.0):
        self.alpha = alpha
        self.beta  = beta

    def sample(self) -> float:
        return np.random.beta(self.alpha, self.beta)

    def update(self, reward: int):
        """reward ∈ {0,1}"""
        self.alpha += reward
        self.beta  += 1 - reward


class ThompsonBandit:
    def __init__(self, arm_ids: List[str]):
        self.arms: Dict[str, Arm] = {aid: Arm() for aid in arm_ids}

    def choose(self) -> str:
        """Return arm with highest sampled probability."""
        return max(self.arms, key=lambda aid: self.arms[aid].sample())

    def reward(self, arm_id: str, reward: int):
        self.arms[arm_id].update(reward)

    def state(self) -> Dict[str, dict]:
        return {aid: {"alpha": arm.alpha, "beta": arm.beta}
                for aid, arm in self.arms.items()}