"""
Python model bank_balance.py
Translated using PySD version 0.7.10
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.functions import cache
from pysd import functions

_subscript_dict = {}

_namespace = {
    'INITIAL TIME': 'initial_time',
    'Interest Rate': 'interest_rate',
    'TIME STEP': 'time_step',
    'Time': 'time',
    'Deposits': 'deposits',
    'TIME': 'time',
    'FINAL TIME': 'final_time',
    'SAVEPER': 'saveper',
    'Interest': 'interest',
    'Income': 'income',
    'Balance': 'balance'
}


@cache('run')
def final_time():
    """
    FINAL TIME

    Day

    The final time for the simulation.
    """
    return 100


integ_balance = functions.Integ(lambda: income(), lambda: 100)


@cache('run')
def interest_rate():
    """
    Interest Rate

    Dollars/Dollar/Day


    """
    return 0.001


@cache('run')
def deposits():
    """
    Deposits

    Dollars/Day


    """
    return 5


@cache('step')
def saveper():
    """
    SAVEPER

    Day [0,?]

    The frequency with which output is stored.
    """
    return time_step()


@cache('run')
def initial_time():
    """
    INITIAL TIME

    Day

    The initial time for the simulation.
    """
    return 0


@cache('step')
def interest():
    """
    Interest

    Dollars/Day


    """
    return balance() * interest_rate()


@cache('step')
def income():
    """
    Income

    Dollars/Day


    """
    return deposits() + interest()


@cache('run')
def time_step():
    """
    TIME STEP

    Day [0,?]

    The time step for the simulation.
    """
    return 1


@cache('step')
def balance():
    """
    Balance

    Dollars


    """
    return integ_balance()
