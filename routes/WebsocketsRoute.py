from fastapi import APIRouter, WebSocket

websocketRoute = APIRouter()

@websocketRoute.websocket("/example")
async def example_socket(socket: WebSocket) -> str:
    await socket.accept()
    while True:
        data = await socket.receive_text()
        await socket.send_text(f"Message text was: {data}")