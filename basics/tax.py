"""
计算薪资个人所得额

2018-10-01日起执行税率计算：
等级    全月应纳税所得额              税率      速算扣除数
1       x < 3000                    3%          0
2       3000 <= x < 12,000          10%         210
3       12,000 <= x < 25,000        20%         1410
4       25,000 <= x < 35,000        25%         2660
5       35,000 <= x < 55,000        30%         4410
6       55,000 <= x < 80,000        35%         7160
7       80,000 <= x                 45%         15160

全月应纳税所得额 = 薪资收入 - 5000 - 个人缴纳社保公积金
个人所得税 = 全月应纳税所得额 * 税率 - 速算扣除数
个人缴纳社保公积金：养老保险 8%; 失业保险 0.5%; 住房公积金 8%; 医疗保险 2%; 大额医疗保险 5元
"""

def cal_tax(tax_base):
    if tax_base <= 0:
        rate = 0
        deduction = 0
    elif tax_base < 3000:
        rate = 0.03
        deduction = 0
    elif tax_base < 12000:
        rate = 0.1
        deduction = 210
    elif tax_base < 25000:
        rate = 0.2
        deduction = 1410
    elif tax_base < 35000:
        rate = 0.25
        deduction = 2660
    elif tax_base < 55000:
        rate = 0.3
        deduction = 4410
    elif tax_base < 80000:
        rate = 0.35
        deduction = 7160
    else:
        rate = 0.45
        deduction = 15160
    return abs(tax_base * rate - deduction)

def cal_social_fund(salary, \
    endowment_rate=0.08, \
    unemployment_rate=0.005, \
    housing_rate=0.08, \
    medical_rate=0.02, \
    others=0):
    return [salary * endowment_rate, salary * unemployment_rate, \
        salary * housing_rate, salary * medical_rate, others]

if __name__ == '__main__':
    basis = 5000
    salary = float(input('请输入薪资: '))
    # social_fund = cal_social_fund(salary, housing_rate=0.07)
    social_fund = cal_social_fund(salary, others=5)
    tax = cal_tax(salary - basis - sum(social_fund))
    remainding = salary - sum(social_fund) - tax
    print('养老保险: %.2f; 失业保险: %.2f; 住房公积金: %.2f; 医疗保险: %.2f; 大额医疗保险: %.2f;' \
        % (social_fund[0], social_fund[1], social_fund[2], social_fund[3], social_fund[4]))
    print('个人所得税: %.2f' % tax)
    print('应扣合计: %.2f; 实领合计: %.2f.' % (sum(social_fund) + tax, remainding))