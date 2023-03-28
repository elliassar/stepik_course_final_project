# stepik_course_final_project

Выполнение итого проекта по тестированию сайта

1. Проверка всех тестов, выполнить команду: "pytest -v --tb=line --language=en test_product_page.py"

2. Проверка тестов, помеченных как "need_review", выполнмить команду: "pytest -v --tb=line --language=en -m need_review test_product_page.py"

P.S.: 1. По умолчанию язык страницы английский (параметр --language можно пропустить)
	  2. Также можно выбрать браузер запуска тестов параметром --browser_name (chrome по умолчанию), например
	  
	  "pytest -v --tb=line --language=en --browser_name=firefox test_product_page.py"