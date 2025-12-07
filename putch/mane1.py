from purchase_anylazer import read_purchases, total_spent, spent_by_category, top_n_expensive, write_report
print("Читаем файл purchases.txt")
valid, invalid = read_purchases('purchases.txt')
write_report(valid, invalid, 'report.txt')
print("Отчет сохранен в файл report.txt")
