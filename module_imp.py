import pay_module

print(pay_module.version)
pay_module.printAuthor()

pay_info = pay_module.Pay("1aAdf", 13000, "2020-10-22")
print(pay_info.get_pay_info())

print(pay_module.__name__)
