import matplotlib
import matplotlib.pyplot as plt
import math

approximations_odd_fractions = []


def run_odd_fractions(n):
    denominator = 1.0
    answer = 0.0
    add = True
    for x in range(n):
        if add:
            answer += 1.0 / denominator
            denominator += 2.0
            add = False
        else:
            answer -= 1.0 / denominator
            denominator += 2.0
            add = True
        approximations_odd_fractions.append(4 * answer)
    print(approximations_odd_fractions[n-1])
    print(math.pi)
    print(math.pi - approximations_odd_fractions[n-1])


def run_plot(n):
    plt.ylabel("Difference")
    plt.xlabel("Precision")
    plt.xticks(range(0, n + int(n / 10), int(n / 10)))
    plt.xlim([1, n])
    plt.loglog()

    plt.plot([abs(x - math.pi) for x in approximations_odd_fractions], color='b')

    plt.show()


n_to_use = 8900000
run_odd_fractions(n_to_use)
run_plot(n_to_use)
