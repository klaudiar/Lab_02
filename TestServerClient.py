import unittest
import rock_paper_scissors


class TestServerClient(unittest.TestCase):

    def setUp(self):
        self.rock = rock_paper_scissors

    def testyourChoice(self):
        text3, choice3 = self.rock.yourChoice(3)
        text2, choice2 = self.rock.yourChoice(2)
        text1, choice1 = self.rock.yourChoice(1)
        text9, choice9 = self.rock.yourChoice(9)
        textn, choicen = self.rock.yourChoice('n')
        assert choice1 == 1 and choice2 == 2 and choice3 == 3, "function yourChoice failed"
        assert int(choice9) == 0, "function yourChoice failed"
        assert choicen == 0, "function yourChoice failed"


    def testserverChoice(self):
        choice, text = self.rock.serverChoice()
        assert choice == 1 or choice == 2 or choice == 3, "serverChoice failed, wrong choice"
        assert (choice == 1 and text == 'Server chose 1 - rock') or \
               (choice == 2 and text == 'Server chose 2 - paper') or \
               (choice == 3 and text == 'Server chose 3 - scissors'), "serverChoice failed, wrong text"

if __name__ == "__main__":
    unittest.main()