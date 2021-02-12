import csv

class CompanyList:
    def __init__(self):
        with open('c:/Users/gdead/Desktop/SMT Project Folder/NYSE_20210125.csv') as csvfile:
            company = csv.reader(csvfile, delimiter = ',', quotechar = '|')
            print(company)
            for row in company:
                if float(row[5]) <= 50.00:
                    print(', '.join(row))

                """
                filtered = filter(lambda p: p <= 50.00 == p[5], company)
                csv.writer(open('NYSE_20210125.csv', 'w'), delimiter = ' ').writerows(filtered)
                """
"""
    def filter(self, company):
        smallShares <= 50.00
        smallCompany = [smallShares]
        for i <= smallCompany:
            if (company in smallCompany):
                print(smallCompany[i])
                return True
            else:
                return False
"""
#companies = CompanyList()
#print(companies)

List = CompanyList()

#CompanyList().filter
"""
print('$50 or less stocks are:')
for i in filtered:
    print(i)
"""