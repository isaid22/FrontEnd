from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bandit import ThompsonBandit

app = FastAPI(title="Thompson-Bandit", version="0.1.0")

# --- config -------------------------------------------------------------
ARM_NAMES = ["headline_A", "headline_B", "headline_C"]   # change at will
bandit = ThompsonBandit(ARM_NAMES)
# ------------------------------------------------------------------------

class ChoiceOut(BaseModel):
    arm_id: str

class RewardIn(BaseModel):
    arm_id: str
    reward: int   # 0 or 1

@app.get("/choose", response_model=ChoiceOut)
def choose():
    """Pick an arm."""
    return ChoiceOut(arm_id=bandit.choose())

@app.post("/reward")
def reward(payload: RewardIn):
    """Log a binary reward."""
    if payload.arm_id not in bandit.arms:
        raise HTTPException(status_code=404, detail="Unknown arm")
    bandit.reward(payload.arm_id, payload.reward)
    return {"status": "ok"}

@app.get("/state")
def state():
    """Debug: current posterior parameters."""
    return bandit.state()