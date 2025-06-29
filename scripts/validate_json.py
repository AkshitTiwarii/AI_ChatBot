import json
import sys
from pathlib import Path

def validate_or_repair(filepath, default):
    """Ensure a JSON file exists and contains valid data"""
    path = Path(filepath)
    try:
        if not path.exists() or path.stat().st_size == 0:
            path.parent.mkdir(exist_ok=True)
            path.write_text(json.dumps(default))
            print(f"Initialized {filepath}")
            return False
        
        # Test if valid JSON
        json.loads(path.read_text())
        return True
    except (json.JSONDecodeError, UnicodeDecodeError):
        path.write_text(json.dumps(default))
        print(f"Repaired invalid {filepath}")
        return False

if __name__ == "__main__":
    checks = {
        "data/raw_pages.json": [],
        "data/pdf_text.json": {}
    }
    
    all_valid = True
    for filepath, default in checks.items():
        if not validate_or_repair(filepath, default):
            all_valid = False
    
    if not all_valid:
        print("⚠️ Some files needed repair", file=sys.stderr)
        sys.exit(1)
    print("✅ All JSON files valid")
