import unittest

from guess import Guess


class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')  # 맞추어갈 단어의 상태를 확인하는 Case
        self.g2 = Guess('FFFFFFF')  # 없는값을 계속 입력 받았을 때의 대한 Case <- 결과적으로 의미없음 + 대문자 넣어도 작동하는가(의미없음)
        self.g3 = Guess('teammate')  # 입력받는 값이 NULL ('Enter'만 입력)일 경우에 대한 Case

        self.c1 = Guess('selfish')  # 올바른 값이 리턴되고 있는가? def Finished 관련.

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        # 부분적으로 맞추어진 단어의 상태가 올바른가?
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')

        self.g2.guess('l')
        self.assertEqual(self.g2.displayCurrent(), '_ _ _ _ _ _ _ ')  # 하나도 없는데 없는값을 리턴받았을때
        self.g2.guess('r')
        self.assertEqual(self.g2.displayCurrent(), '_ _ _ _ _ _ _ ')  # 한 번 더
        self.g2.guess('F')
        self.assertEqual(self.g2.displayCurrent(), 'F F F F F F F ')  # 'FFFFFFF'

        self.g3.guess('')  # 'Enter'를 입력받았을 때
        self.assertEqual(self.g3.displayCurrent(), '_ e _ _ _ _ _ e ')  # teammate

    def testDisplayGuessed(self):
        # 이용된 글자들의 집합을 나타내는 데이터들은 올바르게 유지되는가?
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' a d e n t u ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f n t u ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f l n t u ')

        self.g2.guess('l')
        self.assertEqual(self.g2.displayGuessed(), ' e l n ')
        self.g2.guess('F')
        self.assertEqual(self.g2.displayGuessed(), ' F e l n ')

        self.assertEqual(self.g3.displayGuessed(), ' e n ')
        self.g3.guess('')  # 'Enter'만 쳤을때, 변화가 없는게 맞는가?
        self.assertEqual(self.g3.displayGuessed(), ' e n ')

    def testFinished(self):
        # 단어의 전체를 다 맞춘 경우에 대한 처리가 올바른가?
        self.c1.guess('s')
        self.c1.guess('l')
        self.c1.guess('f')
        self.c1.guess('i')
        self.c1.guess('s')
        self.c1.guess('h')
        self.assertEqual(self.c1.finished(), True)  # selfish, 모듈에서 return True. // 테스트시 True = True 이어야 합니다.
        # 이는 assertTrue 로 판단하면 더 간편한 코드 한 줄이 될 수 있습니다만 기능상 같습니다.


if __name__ == '__main__':
    unittest.main()

