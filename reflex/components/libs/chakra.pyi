"""Stub file for chakra.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Union, overload, Optional
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class ChakraComponent(Component):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "ChakraComponent": ...  # type: ignore
