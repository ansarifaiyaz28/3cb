import multiprocessing
import time

# A simple function that takes time
def square_number(x):
    print(f"Processing {x}")
    time.sleep(1)  # pretend this is a slow task
    return x * x


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parallel_runs = len(numbers)

    print("Running WITHOUT multiprocessing...")
    start = time.time()

    results = []
    for n in numbers:
        results.append(square_number(n))

    print("Results:", results)
    print("Time taken:", time.time() - start)

    print("\nRunning WITH multiprocessing...")
    start = time.time()

    # Create a pool of "$number" worker processes
    with multiprocessing.Pool(processes=parallel_runs) as pool:
        results = pool.map(square_number, numbers)

    print("Results:", results)
    print("Time taken:", time.time() - start)


# This is REQUIRED for multiprocessing to work properly
if __name__ == "__main__":
    main()
