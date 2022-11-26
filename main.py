from prettytable import PrettyTable
import math
def convertToBinary(num, length):
    bits = [0] * length
    if num == 0:
        return bits
    i = length - 1
    while num != 0:
        bits[i] = (num % 2)
        i -= 1
        num = num // 2
    return bits

def getAllBinary(n):
    binary_nos = []
    for i in range(pow(2, n)):
        bits = convertToBinary(i, n)
        binary_nos.append(bits)
    return binary_nos

def calculate_entropy(arr):
    answer = 0
    for num in arr:
        answer += -(num*math.log2(num))
    return answer

def entropy_of_a_Markov_Source():
    probabilities = {0: {0: 0.9, 1: 0.1}, 1: {0: 0.4, 1: 0.6}}
    total_probability = []
    alpha = float(input("Enter alpha: "))
    beta = float(input("Enter beta: "))
    N = int(input("Enter the number of bit: "))
    binary_arr = getAllBinary(N)
    table = PrettyTable()
    table.field_names = ['n_symbol', 'symbol probability distribution']
    for arr in binary_arr:
        start_from_one = alpha
        start_from_zero = beta
        start_from_one *= probabilities[1][arr[0]]
        start_from_zero *= probabilities[0][arr[0]]
        previous = arr[0]
        for num in arr[1:]:
            start_from_one *= probabilities[previous][num]
            start_from_zero *= probabilities[previous][num]
            previous = num
        answer = start_from_one+start_from_zero
        total_probability.append(answer)
        table.add_row([''.join(map(str, arr)), answer])
    entropy_of_a_message = calculate_entropy(total_probability)
    print(table)
    print("the Entropy of a message = ", str(entropy_of_a_message), "bits/message")
    print(str(N), "-th order entropy of S =", str(entropy_of_a_message/N), "bits/symbol")

if __name__ == "__main__":
    entropy_of_a_Markov_Source()
