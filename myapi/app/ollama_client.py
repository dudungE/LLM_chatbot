import subprocess

def call_ollama_model(model_name: str, prompt: str) -> str:
    try:
        result = subprocess.run(
            ['ollama', 'run', model_name, prompt],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"
