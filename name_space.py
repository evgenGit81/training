
def test_function():
    def inner_function():
        print("Я в области видимиости фукции test_function")
    inner_function()

test_function()
#inner_function() не работает - так как эта функция не видится в глобальном поле