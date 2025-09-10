from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel
from bandit import ThompsonBandit


app = FastAPI(title="Thompson-Bandit",default_response_class=ORJSONResponse,  version="0.1.0")

# ✅ Dev CORS: allow any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # or ["http://localhost:8080"] if you want to be stricter
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,    # keep False if using "*"
)



# --- config -------------------------------------------------------------
ARM_NAMES = ["headline_A", "headline_B", "headline_C"]   # change at will
ARM_DESCRIPTIONS = {
    "headline_A": {
        "message": "Check today's <link>mortgage rates</link>",
        "url": "https://www.chase.com/personal/mortgage/mortgage-rates"
    },
    "headline_B": {
        "message": "Explore <link>refinancing options</link> for your home",
        "url": "https://www.chase.com/personal/mortgage/mortgage-refinance"
    },
    "headline_C": {
        "message": "Learn about <link>home equity</link> solutions",
        "url": "https://www.chase.com/personal/home-equity/customer-service"
    }
}
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

@app.get("/api/recommendation")
def get_recommendation(user_id: str):
    """Get a recommendation for a specific user."""
    # Here we're using the bandit to choose the recommendation
    choice = bandit.choose()
    description = ARM_DESCRIPTIONS[choice]
    
    # Get current state of the chosen arm for logging
    arm_state = bandit.state()[choice]
    print(f"\nArm Selected: {choice}")
    print(f"Current Parameters - Alpha: {arm_state['alpha']:.2f}, Beta: {arm_state['beta']:.2f}")
    if arm_state['num_pulls'] > 0:
        print(f"Average Reward: {arm_state['average_reward']:.3f} (Total Pulls: {arm_state['num_pulls']})")
    
    return {
        "user_id": user_id,
        "recommendation": choice,
        "message": description["message"],
        "url": description["url"]
    }