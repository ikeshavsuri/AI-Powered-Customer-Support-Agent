import json
from typing import Dict,Any
# import your functions from notebook or copy code here
# assume agent_handle_message(user_message) returns dict with 'final_reply' and 'trace'

def handle_message(user_message: str) -> Dict[str,Any]:
    # call your agent controller
    out = agent_handle_message(user_message)   # from your code
    return {"reply": out["final_reply"], "trace": out["trace"]}
