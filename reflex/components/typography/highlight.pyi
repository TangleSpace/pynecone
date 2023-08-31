"""Stub file for highlight.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Dict, List, Optional, overload, Union
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class Highlight(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, query: Optional[Union[Var[List[str]], List[str]]] = None, styles: Optional[Union[Var[Dict], Dict]] = None, **props) -> "Highlight": ...  # type: ignore