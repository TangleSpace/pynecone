"""Stub file for stepper.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Tuple, Union, overload, List, Optional
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class Stepper(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, items: Optional[List[Tuple]] = None, colorScheme: Optional[Union[Var[str], str]] = None, index: Optional[Union[Var[int], int]] = None, size: Optional[Union[Var[str], str]] = None, **props) -> "Stepper": ...  # type: ignore

class Step(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "Step": ...  # type: ignore

class StepDescription(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "StepDescription": ...  # type: ignore

class StepIcon(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "StepIcon": ...  # type: ignore

class StepIndicator(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "StepIndicator": ...  # type: ignore

class StepNumber(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "StepNumber": ...  # type: ignore

class StepSeparator(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "StepSeparator": ...  # type: ignore

class StepStatus(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, active: Optional[Union[Var[str], str]] = None, complete: Optional[Union[Var[str], str]] = None, incomplete: Optional[Union[Var[str], str]] = None, **props) -> "StepStatus": ...  # type: ignore

class StepTitle(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "StepTitle": ...  # type: ignore
