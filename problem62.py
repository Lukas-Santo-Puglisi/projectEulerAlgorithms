def smallestCubeFivePermutations():
    root = 1
    cubes = {}
    while True:
        cube = root**3
        sortedCube = ''.join(sorted(str(cube)))
        if sortedCube in cubes:
            cubes[sortedCube].append(cube)
        else: 
            cubes[sortedCube] = [cube]
        if len(cubes[sortedCube]) == 5:
            return cubes[sortedCube][0]

        root += 1


print(smallestCubeFivePermutations())