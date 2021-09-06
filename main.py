import matplotlib.pyplot as plt
import math
import random

approximations_odd_fractions = []
approximations_square_fractions = []
approximations_newton = []
approximations_viete = []
approximations_dartboard = []
approximations_sphereboard = []


def average_elements(results):
    answer = []
    for x in range(len(results[0])):
        curr_sum = 0.0
        for y in results:
            curr_sum += y[x]
        answer.append(curr_sum / len(results))
    return answer


def run_odd_fractions(n):  # (Leibniz)
    denominator = 1.0
    answer = 0.0
    add = True
    for x in range(n + 1):
        answer += 1.0 / denominator if add else -1.0 / denominator
        denominator += 2.0
        add = not add
        approximations_odd_fractions.append(4 * answer)
    print(approximations_odd_fractions[n])


def run_square_fractions(n):  # (Basel)
    answer = 0.0
    for x in range(n + 1):
        answer += 1.0 / ((x + 1) ** 2.0)
        approximations_square_fractions.append(math.sqrt(6.0 * answer))
    print(approximations_square_fractions[n])


def run_newton(n):  # (Newton)
    answer = 0.0
    for x in range(n + 1):
        answer += (2 ** x) * (math.factorial(x) ** 2) / math.factorial((2.0 * x) + 1)
        approximations_newton.append(2.0 * answer)
    print(approximations_newton[n])


def run_viete(n):  # (Viete)
    answer = math.sqrt(2.0) / 2.0
    numerator = math.sqrt(2.0)
    for x in range(n + 1):
        approximations_viete.append(2 / answer)

        answer *= math.sqrt(2.0 + numerator) / 2.0
        numerator = math.sqrt(2.0 + numerator)
    print(approximations_viete[n])


def run_dartboard(n, repeats):  # (dartboard)
    results = []

    for i in range(repeats):
        curr_results = []
        points = []
        for x in range(n + 1):
            x_coord = random.uniform(-1.0, 1.0)
            y_coord = random.uniform(-1.0, 1.0)
            points.append([x_coord, y_coord])

            inside_circle = 0
            for point in points:
                if math.sqrt(point[0] ** 2 + point[1] ** 2) < 1:
                    inside_circle += 1
            curr_results.append(4 * (inside_circle / len(points)))
        results.append(curr_results)

    for e in average_elements(results):
        approximations_dartboard.append(e)
    print(approximations_dartboard[n])


def run_sphereboard(n, repeats):  # (Spherical dartboard)
    results = []

    for i in range(repeats):
        curr_results = []
        points = []
        for x in range(n + 1):
            x_coord = random.uniform(-1.0, 1.0)
            y_coord = random.uniform(-1.0, 1.0)
            z_coord = random.uniform(-1.0, 1.0)
            points.append([x_coord, y_coord, z_coord])

            inside_sphere = 0
            for point in points:
                if math.sqrt(point[0] ** 2 + point[1] ** 2 + point[2] ** 2) < 1:
                    inside_sphere += 1
            curr_results.append(6 * (inside_sphere / len(points)))
        results.append(curr_results)

    for e in average_elements(results):
        approximations_sphereboard.append(e)
    print(approximations_sphereboard[n])


def run_plot(n):
    plt.ylabel("Difference/Error")
    plt.xlabel("Precision (n)")
    plt.xticks(range(0, n + 1, int(n / 10)))
    plt.xlim([0, n])
    plt.ylim([0, 0.4])

    plt.plot([abs(x - math.pi) for x in approximations_odd_fractions], color='b', label="Leibniz")
    plt.plot([abs(x - math.pi) for x in approximations_square_fractions], color='r', label="Basel")
    plt.plot([abs(x - math.pi) for x in approximations_newton], color='y', label="Newton")
    plt.plot([abs(x - math.pi) for x in approximations_viete], color='g', label="Viete")
    plt.title("Convergence of Different Series")

    # plt.plot([abs(x - math.pi) for x in approximations_dartboard], color='r', label="Dartboard")
    # plt.plot([abs(x - math.pi) for x in approximations_sphereboard], color='b', label="Sphereboard")
    # plt.title("Convergence of Monte Carlo Simulations")

    plt.legend(loc="upper right")
    plt.show()


# n_to_use = 100000
n_to_use = 30

# n_to_use = 500
# repeats_to_use = 100

run_odd_fractions(n_to_use)
run_square_fractions(n_to_use)
run_newton(n_to_use)
run_viete(n_to_use)

# run_dartboard(n_to_use, repeats_to_use)
# run_sphereboard(n_to_use, repeats_to_use)

run_plot(n_to_use)

# print([abs(x - math.pi) for x in approximations_odd_fractions])
