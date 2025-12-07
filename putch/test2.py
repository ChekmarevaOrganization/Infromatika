import pytest
from purchase_anylazer import read_purchases, total_spent, spent_by_category, top_n_expensive, write_report

file = open("purchases.txt","r").read().split("\n")

def test_read_purchases():
    purchases, nopurchases = read_purchases('purchases.txt')
    assert len(purchases) == 27
    assert len(nopurchases) == 4
    assert purchases[2]['name'] == 'Apples red'
    assert purchases[5]['price'] == 4.90


def test_total_spent():
    purchases, nopurchases = read_purchases('purchases.txt')
    assert total_spent(purchases) == 153.79000000000002


def test_spent_by_category():
    purchases, nopurchases = read_purchases('purchases.txt')
    assert spent_by_category(purchases) == {
        "food": 48.39999999999999,
        "home": 19.3,
        "transport": 33.4,
        "other": 12.99,
        "health": 11.5,
        "entertainment": 28.2
    }


def test_top_n_expensive():
    purchases, nopurchases = read_purchases('purchases.txt')
    assert top_n_expensive(purchases) == [19.0, 15.4, 12.0]

def test_count_errors():
    purchases, nopurchases = read_purchases('purchases.txt')
    assert len(nopurchases) == 4


def test_write_report(tmp_path):
    purchases, errors = read_purchases('purchases.txt')
    report_file = tmp_path / "report.txt"
    write_report(purchases, errors, str(report_file))
    with open(report_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert "общая_сумма:153.79" in content
    assert f"всего_строк:{len(purchases) + len(errors)}" in content
    assert f"правильных:{len(purchases)}" in content
    assert f"ошибок:{len(errors)}" in content
    assert "food:48.40" in content
    assert "home:19.30" in content