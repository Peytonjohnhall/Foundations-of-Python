# Requirement 1)
class myMath:
    # additionResult = 0

    # Requirement 3)
    def __init__(self):
    # def __init__(self, additionResult):
        # self.__additionResult = additionResult # Requirement 3)
        self.__additionResult = 0 # Requirement 3)

    # Requirement 2)
    @staticmethod
    def AddAndPrintNumbers(*args, **kwargs):
        params_list = [*args]
        # print(params_list)
        # print(type(params_list))
        list_sum = 0
        for eachItem in params_list:
            list_sum = list_sum + eachItem # list_sum is local
        return list_sum

    # Requirement 4)
    def increment_additionResult(self, list_sum):
        self.__additionResult = self.__additionResult + list_sum

obj = myMath()
a = obj.AddAndPrintNumbers(1, 2, 3, 4, 5, 6, 7) # Requirement 2) Test 1)
obj.increment_additionResult(a)
print(a)
b = obj.AddAndPrintNumbers(5, 10, 15) # Requirement 2) Test 2)
obj.increment_additionResult(b)
print(b)