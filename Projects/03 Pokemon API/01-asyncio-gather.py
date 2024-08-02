import asyncio
import random
import time

from utils.req_http import http_get, http_get_sync

# The highest Pokemon id
MAX_POKEMON = 898


def get_random_pokemon_name_sync() -> str:
    pokemon_id = random.randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)
    return str(pokemon["name"])


async def get_random_pokemon_name() -> str:
    pokemon_id = random.randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])


async def main() -> None:
    # synchronous call
    time_before = time.perf_counter()
    print("Running synchronous...")
    for _ in range(5):
        pokemon_name = get_random_pokemon_name_sync()
        print(f"- {pokemon_name}")
    print(f"Total time (synchronous): {time.perf_counter() - time_before}")

    # asynchronous call
    time_before = time.perf_counter()
    print("Running asynchronous...")
    pokemon_names = await asyncio.gather(*[get_random_pokemon_name() for _ in range(5)])
    for pokemon_name in pokemon_names:
        print(f"- {pokemon_name}")
    print(f"Total time (asynchronous): {time.perf_counter() - time_before}")


if __name__ == "__main__":
    asyncio.run(main())
