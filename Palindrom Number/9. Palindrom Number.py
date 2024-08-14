class Solutions:

    # Approach 1: Convert to string and compare

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x = str(x)

        return x

    # Approach 2: half and half then chop off and compare

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False

    #     div = 1
    #     while x > 10 * div:
    #         div *= 10

    #     while x:
    #         right = x % 10
    #         left = x // div

    #         if left != right:
    #             return False

    #         # chop off the left and right digit

    #         x = (x % div) // 10
    #         div = div // 100
    #     return True
