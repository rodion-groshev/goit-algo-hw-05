import timeit
from kmp import kmp_search
from rabin_karp_search import rabin_karp_search
from boyer_moore_search import boyer_moore_search


def read_file(file_name):
    with open(file_name) as file:
        text = file.read()
        return text


if __name__ == '__main__':
    text = ["стаття 1.txt", "стаття 2.txt"]
    pattern = ["алгоритм", "неіснуючий"]
    print(f"| {'Algorithm':<30} | {'KMP':<30} | {'Boyer Moore':<30} | {'Rabin karp':<30} |")
    print(f"| {'-' * 30} | {'-' * 30} | {'-' * 30} | {'-' * 30} |")
    for name in text:
        arr = read_file(name)
        for pat in pattern:
            kmp = timeit.timeit(lambda: kmp_search(arr, pat), number=5)
            boyer_moore = timeit.timeit(lambda: boyer_moore_search(arr, pat), number=5)
            rabin_karp = timeit.timeit(lambda: rabin_karp_search(arr, pat), number=5)
            print(f"| {f'{name, pat}':<30} | {kmp:30.5f} | {boyer_moore:30.5f} | {rabin_karp:30.5f} |")
