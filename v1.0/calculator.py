from functions import *

# 收入数据填写

# 税前收入
income = int(input("Enter your year income without tax(yen): "))
insurance = int(input('please input your yearly insurance fee in total(yen):'))
furusato_fee = int(input('please input your ふるさと納税 in total(yen):'))
loan = int(input("please input your 住宅ローン in total(yen):"))
rise_sel = int(input('please select your 扶養控除[一般: 1/ 特定: 2/ 他: 0]:'))
if rise_sel == 1:
    rise_fee = 380000
elif rise_sel == 2:
    rise_fee = 630000
else:
    rise_fee = 0

income_with_deduction = salary_deduction(income)
income_need_tax = income_with_deduction - insurance

tax_income = income_tax(income_need_tax)
tax_resident = resident_tax(income_need_tax)
tax_total = tax_resident + tax_resident

print(f"you need to pay tax: {tax_total} yen")
print(f"you can deduct your tax to {tax_total - insurance - furusato_fee - rise_fee - loan}")
