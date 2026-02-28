animals = ['cheetah', 'puma', 'jaguar']
speeds = ['112 km/h', '80 km/h', '80 km/h']

for animal in animals:
    print(f"\n{animal.title()}")
    for speed in speeds:
        print(f"This is the top speed: {speed}")
print("\nThese animals are all hunters at lightning fast speeds.")

# Here again - outside my knowledge. I wanted to create a loop inside the loop - which seemed logical to me at first.
# But I notice now that the subloop will continue to run all the way through every time the original loop runs.
# Which is not the point. I need the subloop to run once everytime the original loop runs, but that might create
# another problem. How will I do this? Also, how will the subloop know to always match the original loops index?        
