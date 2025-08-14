import runpod

def handler(job):
    # Holt den Wert "name" aus der Eingabe oder setzt "World" als Standard
    name = job["input"].get("name", "World")
    return {"message": f"Hello, {name}!"}

# Startet den Serverless-Handler auf RunPod
runpod.serverless.start({"handler": handler})√
