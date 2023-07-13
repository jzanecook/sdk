# generated by fastapi-codegen:
#   filename:  ../openapi.yml
#   timestamp: 2023-07-13T03:26:56+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class StateType(Enum):
    AgentStart = 'AgentStart'
    AgentStop = 'AgentStop'


class AgentState(BaseModel):
    state_type: StateType = Field(
        ..., description='Enumeration indicating what state is contained in the payload'
    )


class AgentAction(BaseModel):
    action_id: Optional[str] = Field(
        None, description='The ID of the action you want to react to (optional)'
    )
    type: Optional[str] = Field(
        None, description='Type of the action you want to create'
    )
    input: Optional[Dict[str, Any]] = Field(
        None, description='Input parameters for the action'
    )


class State(Enum):
    Pending = 'Pending'
    Running = 'Running'
    Completed = 'Completed'
    Failed = 'Failed'
    Cancelled = 'Cancelled'


class AgentActionInfo(AgentAction):
    output: Optional[Dict[str, Any]] = Field(None, description='Output of the action')
    deliverables: Optional[Dict[str, Any]] = Field(
        None, description='List of deliverables that the action has produced'
    )
    state: State = Field(..., description='The current state of the action')