import unittest
import hurricane_analyzer as analyzer


class UpdatesDamagesTest(unittest.TestCase):

    def test_should_provide_intact_damages_when_it_has_no_damages_recorded(self):
        fake_damages = ['Damages not recorded']
        self.assertEqual(analyzer.updated_damages(fake_damages), fake_damages)

    def test_should_convert_million_suffixed_damages(self):
        self.assertEqual(analyzer.updated_damages(['1M']), [1000000.0])
        self.assertEqual(analyzer.updated_damages(['10M']), [10000000.0])
        self.assertEqual(analyzer.updated_damages(['100M']), [100000000.0])
        self.assertEqual(analyzer.updated_damages(['1M', '10M']), [1000000.0, 10000000.0])

    def test_should_convert_billion_suffixed_damages(self):
        self.assertEqual(analyzer.updated_damages(['1B']), [1000000000.0])
        self.assertEqual(analyzer.updated_damages(['10B']), [10000000000.0])
        self.assertEqual(analyzer.updated_damages(['100B']), [100000000000.0])
        self.assertEqual(analyzer.updated_damages(['1B', '10B']), [1000000000.0, 10000000000.0])


if __name__ == '__main__':
    unittest.main()
