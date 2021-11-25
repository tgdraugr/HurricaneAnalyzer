import unittest
import hurricane_analyzer


class UpdatesDamagesTest(unittest.TestCase):

    def test_should_provide_intact_damages_when_it_has_no_damages_recorded(self):
        fake_damages = ['Damages not recorded']
        self.assertEqual(hurricane_analyzer.updated_damages(fake_damages), fake_damages)

    def test_should_convert_million_suffixed_damages(self):
        self.assertEqual(hurricane_analyzer.updated_damages(['100M']), [100000000])
        self.assertEqual(hurricane_analyzer.updated_damages(['10M']), [10000000])


if __name__ == '__main__':
    unittest.main()
