import asyncio
import threading
import time


# Simulate an I/O-bound task (e.g., network request) for threading
def io_task(name, duration):
    print(f"{name} started (threading).")
    time.sleep(duration)  # Simulate I/O with time.sleep (blocking)
    result = f"{name} result"
    print(f"{name} finished (threading).")
    return result


# Wrapper function to retrieve results from threading
def threaded_io_task(name, duration, results, index):
    results[index] = io_task(name, duration)


# Asyncio version of the same I/O-bound task
async def async_io_task(name, duration):
    print(f"{name} started (asyncio).")
    await asyncio.sleep(duration)  # Simulate I/O with asyncio.sleep (non-blocking)
    result = f"{name} result"
    print(f"{name} finished (asyncio).")
    return result


# Using threading
def run_with_threading():
    print("\nRunning with threading:")
    start_time = time.time()

    # Create a list to store results
    num_tasks = 5
    results = [None] * num_tasks

    # Create and start threads, passing results list and index to each thread
    threads = [
        threading.Thread(target=threaded_io_task, args=(f"Task {i+1}", 2, results, i))
        for i in range(num_tasks)
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print(f"Threading total time: {time.time() - start_time:.2f} seconds")
    print("Threading results:", results)


# Using asyncio
async def run_with_asyncio():
    print("\nRunning with asyncio:")
    start_time = time.time()

    # Run tasks concurrently with asyncio.gather and collect results
    tasks = [async_io_task(f"Task {i+1}", 2) for i in range(5)]
    results = await asyncio.gather(*tasks)

    print(f"Asyncio total time: {time.time() - start_time:.2f} seconds")
    print("Asyncio results:", results)


def main() -> None:
    # Run threading example
    run_with_threading()

    # Run asyncio example
    asyncio.run(run_with_asyncio())


if __name__ == "__main__":
    main()
