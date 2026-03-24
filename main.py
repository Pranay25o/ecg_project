from fastapi import FastAPI, WebSocket
import asyncio
import random

app = FastAPI()

@app.websocket("/ws/ecg")
async def ecg_stream(websocket: WebSocket):
    await websocket.accept()

    while True:
        # Generate 8 channel ECG-like values
        values = [str(random.uniform(-1000, 1000)) for _ in range(8)]

        # Convert to CSV format
        data = ",".join(values)

        await websocket.send_text(data)
        await asyncio.sleep(0.02)