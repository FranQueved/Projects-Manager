"""Run the interactive application."""

import sys
import os

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from interactive_app import InteractiveApp

if __name__ == "__main__":
    app = InteractiveApp()
    app.run()
