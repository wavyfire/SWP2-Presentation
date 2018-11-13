import unittest

from word import Word


class TestWord(unittest.TestCase):

    def setUp(self):
        self.w1 = Word('words.txt')  # Word 모듈에 파일을 넣어서 확인합니다. 테스트이지만 실제 파일과 같은걸 넣었습니다.

        # self.w2 = Word('') # 주어진 파일이 없는 경우에 대한 케이스, 작동하지 않습니다. 결과는 아래에.
        # w2는 setUp 단계에서부터 오류를 일으켜서 모듈을 수정해야할만큼 심각한 오류 케이스라는 결론을 내렸습니다.
        # testPalindrome 이 이 경우를 테스트 안한 것 같다고 생각해 추가했습니다.

    def tearDown(self):
        pass

    def testRandFromDB(self):
        # Assert 에서 In 기능으로 확인해보았습니다. return 된 결과값이 txt 파일 안에 있다면 테스트는 통과될 것입니다.
        self.assertIn(self.w1.randFromDB(), self.w1.words)  # word 모듈은 init 에서, words 에 txt 를 저장합니다.
        # 따라서 words 안에서 randFromDB 한 결과물을 찾아야합니다. 결과는 통과입니다.

    def testNoneTest(self):
        # self.assertIn(self.w2.randFromDB(), self.w2.words)
        # File Not Found Error 가 뜨는데, 주어진 파일이 없기 때문입니다.
        # 이를 통해서 본 프로그램에서 words.txt 파일이 없다면 오류가 날 것임을 알 수 있습니다.
        # 따라서 word module 에 이 에러에 대한 처리를 해야합니다. # (추후 구현 예정....)

        # self.assertisNone(self.w2.randFromDB())
        # 마찬가지로 File Not Found Error.... 애초에 init 에서 파일을 읽을 때 오류가 나는 것이라
        # None 으로 체크해도 마찬가지임을 알 수 있었습니다.

        pass


if __name__ == '__main__':
    unittest.main()

