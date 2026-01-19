#!/usr/bin/env python3
import pytest
from app import app, db

# -------------------------------
# Keep your existing pytest hook
def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))

# -------------------------------
# New: create tables before tests
@pytest.fixture(autouse=True, scope="session")
def create_tables():
    """Automatically create database tables for testing."""
    with app.app_context():
        db.create_all()   # creates all tables
        yield
        db.drop_all()     # optional: clean up after tests
