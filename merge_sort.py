def merge_sort(a):
    if len(a) > 1:
        m = len(a) // 2
        l1 = a[:m]
        l2 = a[m:]

        merge_sort(l1)
        merge_sort(l2)

        i = j = k = 0

        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                a[k] = l1[i]
                i += 1
            else:
                a[k] = l2[j]
                j += 1
            k += 1

        while i < len(l1):
            a[k] = l1[i]
            i += 1
            k += 1

        while j < len(l2):
            a[k] = l2[j]
            j += 1
            k += 1

def main():
    a = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44, 0]
    print("Array before Sorting:")
    print(a)
    merge_sort(a)
    print("Array after Sorting:")
    print(a)
if __name__ == "__main__":

    import time
    start = time.time()
    main()
    end = time.time()
    runtime = end - start
    print(f"Runtime of the program is {runtime:.4} seconds")
    