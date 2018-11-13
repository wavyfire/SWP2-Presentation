import unittest

from hangman import Hangman


class TestHangman(unittest.TestCase):

    def setUp(self):
        self.h1 = Hangman()
        # Hangman 클래스에서, remainingLives 에 따른 올바른 Hangman 이 출력되고 있는가를 확인할 케이스.
        # remainingLives 에 따른 출력은 0~6까지밖에 없습니다. init 에서 -1을 하기 때문입니다.
        # 실제로 7을 넣어서 테스트해보면 IndexError: list index out of range 를 겪을 수 있습니다.

        self.h2 = Hangman()
        # Hangman 클래스에서, decreaseLife 를 테스트해보기 위한 케이스.
        # 간단한 기능이라 되는지만 확인해보았습니다.

    def tearDown(self):
        pass

    def testCurrentShape(self):
        # h1, 즉 remainingLives 에 따른 올바른 Hangman 이 출력되고 있는가를 확인할 케이스.
        self.h1.remainingLives = 0
        self.assertEqual(self.h1.currentShape(), '''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|\
''',)
        self.h1.remainingLives = 1
        self.assertEqual(self.h1.currentShape(), '''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   /
 _|_
|   |______
|          |
|__________|\
''',)
        self.h1.remainingLives = 2
        self.assertEqual(self.h1.currentShape(), '''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',)


        self.h1.remainingLives = 3
        self.assertEqual(self.h1.currentShape(), '''\
   ____
  |    |
  |    o
  |   /|
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',)

        self.h1.remainingLives = 4
        self.assertEqual(self.h1.currentShape(), '''\
   ____
  |    |
  |    o
  |    |
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',)

        self.h1.remainingLives = 5
        self.assertEqual(self.h1.currentShape(), '''\
   ____
  |    |
  |    o
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''',)

        self.h1.remainingLives = 6
        self.assertEqual(self.h1.currentShape(), '''\
   ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''',)
# 7이상은 list index out of range 입니다.


    def testDecreaseLife(self):
        self.h2.remainingLives = 6
        self.h2.decreaseLife() # default = 6 에서 기능이 한 번 수행되었으므로 5가 됩니다.
        self.assertEqual(5, self.h2.remainingLives) # Def decreaseLife 가 작동해 5 = 5로 같다면 통과할 것입니다.
        # NotEqual 로 체크한다면 다소 부정확해도 변화하는 것만을 캐치할 수 있을 것 같습니다.

if __name__ == '__main__':
    unittest.main()

