import CSP_6_01_Library_Basics as HW
def test_process_expenses():
    assert HW.process_expenses([4,5,6,7]) == ([4.6, 5.75, 6.9, 8.05])


def test_analyze_scores():
    assert HW.analyze_scores ([100,25,50,75]) == ([62.5, 100])


def test_sanitize_usernames():
    assert HW.sanitize_usernames([["UP PER   ", "l ower  ", " s m a l l", "  TA L L"]]) == ([["up per", "l ower", "s m a l l", "ta l l"]])


def test_identify_outliers():
    assert HW.identify_outliers([4,50,110,200]) == ([[110,200]])


def test_search_and_report():
    assert HW.search_and_report(["Real", "Minds", "Eye"], "eye") == (2)
