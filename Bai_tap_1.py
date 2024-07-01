import math
import random


def check_classification_f1score(tp, fp, fn):
    if not (isinstance(tp, int) and isinstance(fp, int) and isinstance(fn, int)):
        raise TypeError("tp, fp, và fn phải là một số nguyên")
    if tp <= 0 or fp <= 0 or fn <= 0:
        raise ValueError("tp, fp, và fn phải lớn hơn 0")
    try:
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1_score = 2 * precision * recall / (precision + recall)
    except ZeroDivisionError:
        raise ZeroDivisionError(
            "Không thể tính F1-score khi precision hoặc recall bằng 0")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-score: {f1_score:.2f}")


def check_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def check_function(y):
    try:
        if y in ["e", "s", "r"]:
            return True
    except ValueError:
        return False


def sigmoid(x):
    return 1 / (1 + math.e ** (-float(x)))


def relu(x):
    if float(x) <= 0:
        return 0
    else:
        return float(x)


def elu(x):
    while True:
        try:
            alpha = float(input("Nhập alpha: "))
            break
        except ValueError:
            print("Alpha phải ở dạng số. Vui lòng nhập lại.")
    try:
        x = float(x)
    except ValueError:
        print("Giá trị x phải ở dạng số.")
        return False
    if x <= 0:
        return alpha * (math.exp(x) - 1)
    else:
        return x


def main_activation_function():
    while True:
        x = input("Nhập giá trị x: ")
        if check_number(x):
            break
        else:
            print("Giá trị nhập phải là số. Vui lòng nhập lại")
    while True:
        y = input("Nhập tên thuật toán: ")
        if check_function(y):
            if y == "s":
                print("Kết quả sigmoid:", sigmoid(x))
                break
            elif y == "e":
                print("Kết quả eLU:", elu(x))
                break
            else:
                print("Kết quả ReLU:", relu(x))
                break
        else:
            print("Chỉ được nhập các ký tự (s, r, e). Vui lòng nhập lại")


def mae(n):
    try:
        n = int(n)
        if n <= 0:
            raise ValueError()
    except ValueError:
        print("Giá trị phải là số nguyên dương")
        return None
    y = []
    y_pred = []
    MAE_result = 0
    for i in range(n):
        y.append(random.randint(0, 10))
        y_pred.append(random.randint(0, 10))
        MAE_result += abs(y[i] - y_pred[i])
    MAE_result /= n
    return MAE_result


def main_mae():
    n = input("Nhập số lượng phần tử n: ")
    result = mae(n)
    if result is not None:
        print("Mean Absolute Error (MAE):", result)


def mae_loss(y, y_pred):
    return y - y_pred


def mse_loss(y, y_pred):
    return (y - y_pred) ** 2


def main_loss_function():
    while True:
        n = input("Nhập số lượng sample: ")
        if n.isnumeric():
            loss = input("Nhập Hàm cần tính loss: ")
            result = 0
            for i in range(int(n)):
                y = random.randint(0, 10)
                y_pred = random.randint(0, 10)
                if loss == "MAE":
                    x = mae_loss(y, y_pred)
                    result += x
                    print(
                        f'loss name: {loss}, sample: {i}, pred: {y_pred}, target: {y}, loss: {x}')
                elif loss == "MSE":
                    x = mse_loss(y, y_pred)
                    result += x
                    print(
                        f'loss name: {loss}, sample: {i}, pred: {y_pred}, target: {y}, loss: {x}')
                elif loss == "RMSE":
                    x = math.sqrt(mse_loss(y, y_pred))
                    result += x
                    print(
                        f'loss name: {loss}, sample: {i}, pred: {y_pred}, target: {y}, loss: {x}')
            result /= int(n)
            print(f"Loss: {result}")
            break
        else:
            print("Số lượng Sample phải là số nguyên dương")


def sin(x, n):
    sinx = 0
    for i in range(n):
        sinx += (-1) ** i * x ** (2 * i + 1) / math.factorial(2 * i + 1)
    return sinx


def cos(x, n):
    cosx = 0
    for i in range(n):
        cosx += (-1) ** i * x ** (2 * i) / math.factorial(2 * i)
    return cosx


def sinh(x, n):
    sinhx = 0
    for i in range(n):
        sinhx += x ** (2 * i + 1) / math.factorial(2 * i + 1)
    return sinhx


def cosh(x, n):
    coshx = 0
    for i in range(n):
        coshx += x ** (2 * i) / math.factorial(2 * i)
    return coshx


def main_trigonometric_functions():
    x = float(input("Nhập giá trị x: "))
    n = int(input("Nhập giá trị sample: "))
    if n <= 0:
        print("Giá trị n phải là số nguyên dương")
    else:
        print(f"sin({x}) = {sin(x, n)}")
        print(f"cos({x}) = {cos(x, n)}")
        print(f"sinh({x}) = {sinh(x, n)}")
        print(f"cosh({x}) = {cosh(x, n)}")


def md_nre(n, y, y_pred, p):
    md_nre_single_sample = (y ** (1 / n) - y_pred ** (1 / n)) ** p
    return md_nre_single_sample


def main_md_nre():
    while True:
        try:
            y = float(input("Giá trị của y: "))
            y_pred = float(input("Giá trị của y_pred: "))
            n = int(input("Giá trị của n: "))
            p = int(input("Giá trị của p: "))
            result = md_nre(n, y, y_pred, p)
            print(f"md_nre_single_sample: {result}")
            escape = input("Bạn có muốn tiếp tục không? (y/n): ")
            if escape == "y":
                continue
            else:
                break
        except ValueError:
            print("Vui lòng nhập lại các giá trị hợp lệ.")


if __name__ == "__main__":
    # Call the desired function here
    # Example: main_activation_function()
    # Uncomment the function you want to test
    # main_activation_function()
    # main_mae()
    # main_loss_function()
    # main_trigonometric_functions()
    main_md_nre()
