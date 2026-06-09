import subprocess
import sys

print("Lancement de l'application web")

backend = subprocess.Popen([sys.executable, "-m", "uvicorn", "app:app"])
frontend = subprocess.Popen([sys.executable, "-m", "streamlit", "run", "interface.py"])

backend.wait()
frontend.wait()