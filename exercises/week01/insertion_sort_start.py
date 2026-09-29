"""
Oefening 1: Insertion Sort
===========================
Implementeer insertion sort volgens het stappenplan in opgave_week1.md.
"""
def timer_func(suppress_output=False):
    # dit geeft aan hoelang de functie die het meekrijgt heeft gerund
    def actual_decorator(func):
        def wrap_func(*args, **kwargs):
            t1 = time()
            result = func(*args, **kwargs)
            t2 = time()
            if not suppress_output:
                print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
            return result, t2-t1
        return wrap_func
    return actual_decorator

@timer_func(suppress_output=True)
def bubble_sort(sequence):
    n = len(sequence)
    for i in range(n-1):
        for j in range(n-i-1):
            if(sequence[j] > sequence[j+1]):
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j] # wisselen van plaats



def insertion_sort(sequence):
    """
    Sorteer een lijst van klein naar groot met behulp van insertion sort.

    Parameters:
        sequence (list): De lijst om te sorteren.

    Returns:
        list: De gesorteerde lijst.
    """
    # TODO: implementeer insertion sort
    for i in range(1, len(sequence)):
        key = sequence[i]
        j = i-1
        while j >= 0 and sequence[j] > key:
            sequence[j+1] = sequence[j]
            j -= 1
        sequence[j+1] = key

    return sequence


if __name__ == "__main__":
    # Test je implementatie met deze voorbeelden
    test_lijsten = [
        [],
        [42],
        [1, 2, 3, 4],
        [5, 4, 3, 2, 1],
        [3, 1, 2, 1, 3],
        [5, 2, 4, 6, 1, 3],
    ]

    for lijst in test_lijsten:
        origineel = lijst.copy()
        gesorteerd = insertion_sort(lijst)
        print(f"Origineel: {origineel} -> Gesorteerd: {gesorteerd}")

    # Stap 5 (uitbreiding): vergelijk met bubble sort en merge sort
    # Kopieer bubble_sort en merge_sort uit de cursus en test hier:
    # import random
    # import time
    # ...
    import random
    from time import time
    sequence = random.sample(range(1000), 1000)
    len(sequence)

    r = 100 #repitions
    n = 4000 #max 5000
    average_bubble = 0
    average_insert= 0
    for i in range(0, r):
        sequence = random.sample(range(n), n)
        result = insertion_sort(sequence)
        average_insert += result[1] /r
        print(i)
    print("Aveerage time to complete: " + f'{(average_insert):.4f}s')
    for i in range(0,r):
        sequence = random.sample(range(n), n)
        result = bubble_sort(sequence)
        average_bubble += result[1] / r
    print("Average time to complete: " + f'{(average_bubble):.4f}s')

    