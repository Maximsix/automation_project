from selenium.webdriver import (
    Chrome,
    Firefox,
    Edge,
    Safari,
)
from typing import TypeVar


WebDriver = TypeVar("WebDriver", Chrome, Firefox, Edge, Safari)
