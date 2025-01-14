"""Stub file for image.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Union, overload, Set, Any, Optional
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class Image(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, align: Optional[Union[Var[str], str]] = None, fallback: Optional[Component] = None, fallback_src: Optional[Union[Var[str], str]] = None, fit: Optional[Union[Var[str], str]] = None, html_height: Optional[Union[Var[str], str]] = None, html_width: Optional[Union[Var[str], str]] = None, ignore_fallback: Optional[Union[Var[bool], bool]] = None, loading: Optional[Union[Var[str], str]] = None, src: Optional[Union[Var[Any], Any]] = None, alt: Optional[Union[Var[str], str]] = None, src_set: Optional[Union[Var[str], str]] = None, **props) -> "Image": ...  # type: ignore
