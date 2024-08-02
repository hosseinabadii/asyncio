import asyncio
import random
import time
from typing import AsyncIterable

from utils.req_http import http_get

# The highest Pokemon id
MAX_POKEMON = 898


async def get_random_pokemon_name() -> str:
    pokemon_id = random.randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])


async def next_pokemon(total: int) -> AsyncIterable[str]:
    for _ in range(total):
        name = await get_random_pokemon_name()
        yield name


async def main():
    # retrieve the next 5 pokemon names
    time_before = time.perf_counter()
    async for name in next_pokemon(5):
        print(f"- {name}")
    print(f"Total time: {time.perf_counter() - time_before}")

    time_before = time.perf_counter()
    # asynchronous list comprehensions
    names = [name async for name in next_pokemon(5)]
    print("\n- ".join(names))
    print(f"Total time: {time.perf_counter() - time_before}")


if __name__ == "__main__":
    asyncio.run(main())
