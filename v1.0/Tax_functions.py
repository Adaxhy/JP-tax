def salary_deduction(salary):
    """
    给与所得控除+基础控除（这部分可以不交说）
    :param salary: 税前年收入
    :return: 控除后收需要交税的部分
    """
    if salary <= 1625000:
        sd = 550000
    elif 1625001 <= salary <= 1800000:
        sd = salary * 0.4 - 100000 + 480000
    elif 1800001 <= salary <= 3600000:
        sd = salary * 0.3 + 80000 + 480000
    elif 3600001 <= salary <= 6600000:
        sd = salary * 0.2 + 440000 + 480000
    elif 6600001 <= salary <= 8500000:
        sd = salary * 0.1 + 1100000 + 480000
    elif 8500001 < salary <= 24000000:
        sd = 1950000 + 480000
    elif 24000000 < salary <= 24500000:
        sd = 1950000 + 320000
    elif 24500000 < salary <= 25000000:
        sd = 1950000 + 160000
    else:
        sd = 1950000

    return salary - sd


def resident_tax(salary):
    """
    计算住民税
    :param salary: 税后收入
    :return:
    """
    income_new = salary * 0.1 + 4000
    return income_new


def income_tax(income_new):
    """
    所得税
    :return:
    """
    if 1000 <= income_new <= 1949000:
        tax = income_new * 0.05
    elif 1950000 <= income_new <= 3299000:
        tax = income_new * 0.1 - 91500
    elif 3300000 <= income_new <= 6949000:
        tax = income_new * 0.2 - 427500
    elif 6950000 <= income_new <= 8999000:
        tax = income_new * 0.23 - 636000
    elif 9000000 <= income_new <= 17999000:
        tax = income_new * 0.33 - 1536000
    elif 18000000 <= income_new <= 39999000:
        tax = income_new * 0.4 - 2796000
    else:
        tax = income_new * 0.45 - 4796000

    return tax * 1.021  # 复兴税2.1%
