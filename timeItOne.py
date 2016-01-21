import timeit

t = timeit.Timer("euclidAlgorithmOne.getGCD(270,192)", "import euclidAlgorithmOne")

results = t.repeat(5)

for i, item in enumerate(results):
    print(i, "\t", item)

