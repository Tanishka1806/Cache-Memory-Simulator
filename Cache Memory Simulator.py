
# Mini Project: Cache Memory Simulator
# Subject: Computer Organization and Architecture

cache = []
cache_size = 3

hits = 0
misses = 0

def display_cache():
    print("Current Cache:", cache)


def main():
    global hits, misses

    print("===== CACHE MEMORY SIMULATOR =====")
    print("Cache Size:", cache_size)

    while True:
        print("\n1. Access Memory Address")
        print("2. Display Cache")
        print("3. Display Statistics")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            address = input("Enter memory address: ")

            if address in cache:
                hits += 1
                print("Cache HIT! Data found in cache.")
            else:
                misses += 1
                print("Cache MISS! Data loaded from main memory.")

                if len(cache) >= cache_size:
                    removed = cache.pop(0)
                    print("Removed from cache:", removed)

                cache.append(address)

        elif choice == '2':
            display_cache()

        elif choice == '3':
            total = hits + misses
            print("\nTotal Accesses:", total)
            print("Cache Hits:", hits)
            print("Cache Misses:", misses)

            if total > 0:
                hit_rate = (hits / total) * 100
                print("Cache Hit Rate:", round(hit_rate, 2), "%")
                print("Cache Miss Rate:",
                      round((misses / total) * 100, 2), "%")
            else:
                print("No memory accesses yet.")

        elif choice == '4':
            print("Thank you for using the simulator!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
