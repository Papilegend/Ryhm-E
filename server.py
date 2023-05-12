import asyncio
import websockets

connected = set()

async def handle_client(websocket):
    # registreerib kliendi
    connected.add(websocket)
    # sõnum konsooli
    print(f'Client {websocket.remote_address} connected.')
    try:
        async for message in websocket:
            # saabunud sõnum konsooli
            print(f'Received message from {websocket.remote_address}: {message}')
            # broadcastib saabunud sõnumi kõikidele klientidele
            await asyncio.wait([client.send(message) for client in connected])
    finally:
        # unregistreerib kliendi
        connected.remove(websocket)
        # sõnum konsooli
        print(f'Client {websocket.remote_address} disconnected.')


async def main():
    async with websockets.serve(handle_client, '192.168.212.194', 12345):
        # sõnum konsooli
        print("Server started...")
        await asyncio.Future()  # hoiab serveri kogu aeg töös

if __name__ == "__main__":
    asyncio.run(main())
