'''
Demonstrate the use of the .enumerate() function.
'''
hawaii_islands = ["O`ahu", "Kaua`i", "Maui", "Hawai`i", "Moloka`i", "Lāna`i", "Ni`ihau", "Kaho`olawe"]

for idx, island in enumerate(hawaii_islands, start=1):
    print(f"{idx}: {island}")