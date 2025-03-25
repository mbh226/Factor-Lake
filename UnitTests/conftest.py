import sys
import os

#adding the project root directory to sys.path so python can find PriceApp and JSON_Validation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))