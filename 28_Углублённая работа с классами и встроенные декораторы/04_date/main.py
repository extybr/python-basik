
class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return "День: {}\tМесяц: {}\tГод: {}".format(self.day, self.month, self.year)

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        day, month, year = map(int, date.split('-'))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        day, month, year = map(int, date.split('-'))
        data_object = cls(day, month, year)
        return data_object


date_string = Date.from_string('12-03-2022')
print(date_string)
date_valid = Date.is_date_valid('12-12-2099')
print(date_valid)
date_valid = Date.is_date_valid('32-13-2000')
print(date_valid)
