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

    def test_should_correctly_update_damage(self):
        expected = [500000, 'Damages not recorded', 500000000]
        self.assertEqual(analyzer.updated_damages(['0.5M', 'Damages not recorded', '0.5B']), expected)


class AggregateHurricaneDataTest(unittest.TestCase):

    def test_should_aggregate_single_record(self):
        expected = [{
            "Name": "A",
            "Month": "A",
            "Year": 1,
            "Max Sustained Wind": 1,
            "Areas Affected": ["area"],
            "Damage": "Damages not recorded",
            "Deaths": 1
        }]
        self.assertEqual(analyzer.aggregated_records(
            names=["A"],
            months=["A"],
            years=[1],
            max_sustained_winds=[1],
            areas_affected=[["area"]],
            damages=["Damages not recorded"],
            deaths=[1]
        ), expected)


if __name__ == '__main__':
    unittest.main()
