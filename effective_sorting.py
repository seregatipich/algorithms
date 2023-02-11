# 81840810

class Participant:
    def __init__(self, email, score, fine):
        self.email = email
        self.score = score
        self.fine = fine

    def __lt__(self, other):
        return (-self.score, self.fine, self.email) < (
            -other.score, other.fine, other.email)

    def __str__(self) -> str:
        return self.email


def quick_sort(array, left, right):
    if left >= right:
        return
    i = left
    j = right
    pivot = array[(i+j)//2]
    while True:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        if i > j:
            break
    quick_sort(array, left, j)
    quick_sort(array, i, right)


if __name__ == '__main__':
    num_participants = int(input())
    pull = [None] * num_participants
    for i in range(num_participants):
        email, score, fine = input().split()
        score = int(score)
        fine = int(fine)
        pull[i] = Participant(email, score, fine)
    quick_sort(pull, 0, len(pull) - 1)
    for el in pull:
        print(el)