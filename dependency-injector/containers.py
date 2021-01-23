"""Containers module."""
#built-in
import sys
#third party
from dependency_injector import containers, providers
#app module
sys.path.append('../')
from budget import Category

class Container(containers.DeclarativeContainer):
    # Service
    user_category=providers.Factory(Category)
    