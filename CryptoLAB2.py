#PBOX Exercise

class PBox:
    def __init__(self, key):
        self.key = key

    def permute(self, sequence):
        result = [''] * len(self.key)
        for index, element in enumerate(sequence):
            result[self.key[index]-1] = element
        return ''.join(result)

def main():
    # Example key for PBox
    key = [5, 4, 78, 45, 20, 34, 61, 10, 16, 28, 3, 49, 50, 7, 33, 18,
           27, 38, 2, 53, 60, 56, 15, 1, 64, 62, 12, 25, 48, 44, 30, 21,
           59, 6, 51, 47, 42, 63, 46, 31, 35, 54, 57, 11, 14, 26, 22, 19,
           8, 43, 32, 13, 55, 23, 39, 37, 9, 24, 36, 52, 58, 40, 29, 41]

    pbox = PBox(key)

    sequence = "0123456789ABCDEF"
    print("Original Sequence:", sequence)
    permuted_sequence = pbox.permute(sequence)
    print("Permuted Sequence:", permuted_sequence)

if __name__ == "__main__":
    main()
