"""Stub file for video.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Union, overload, Optional
from reflex.components.libs.react_player import ReactPlayerComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class Video(ReactPlayerComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "Video": ...  # type: ignore
