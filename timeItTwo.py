import timeit

t = timeit.Timer("euclidAlgorithmTwo.getGCD(270,192)", "import euclidAlgorithmTwo")

results = t.repeat(5)

for i, item in enumerate(results):
    print(i, "\t", item)