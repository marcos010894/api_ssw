import asyncio

def run_in_loop(function, *args):
    loop = asyncio.get_event_loop()
    return loop.run_in_executor(None, function, *args)