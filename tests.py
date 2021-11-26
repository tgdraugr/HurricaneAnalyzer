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

    def test_should_aggregate_single_record_by_names(self):
        expected = {
            "A": {
                "Name": "A",
                "Month": "A",
                "Year": 1,
                "Max Sustained Wind": 1,
                "Areas Affected": ["area"],
                "Damage": "Damages not recorded",
                "Deaths": 1
            }
        }
        actual = analyzer.aggregated_hurricane_records_by_name(names=["A"], months=["A"], years=[1],
                                                               max_sustained_winds=[1], areas_affected=[["area"]],
                                                               damages=["Damages not recorded"], deaths=[1])
        self.assertEqual(actual, expected)

    def test_should_aggregate_many_records_by_names(self):
        expected = {
            "A": {
                "Name": "A",
                "Month": "A",
                "Year": 1,
                "Max Sustained Wind": 1,
                "Areas Affected": ["area"],
                "Damage": "Damages not recorded",
                "Deaths": 1
            },
            "B": {
                "Name": "B",
                "Month": "B",
                "Year": 2,
                "Max Sustained Wind": 2,
                "Areas Affected": ["A", "B"],
                "Damage": 500000,
                "Deaths": 2
            }
        }
        actual = analyzer.aggregated_hurricane_records_by_name(names=["A", "B"], months=["A", "B"], years=[1, 2],
                                                               max_sustained_winds=[1, 2],
                                                               areas_affected=[["area"], ["A", "B"]],
                                                               damages=["Damages not recorded", "0.5M"], deaths=[1, 2])
        self.assertEqual(actual, expected)

    def test_should_aggregate_single_record_by_year(self):
        hurricanes_by_name = {
            "A": {
                "Name": "A",
                "Month": "A",
                "Year": 1,
                "Max Sustained Wind": 1,
                "Areas Affected": ["area"],
                "Damage": "Damages not recorded",
                "Deaths": 1
            }
        }
        expected = {
            1: [
                {
                    "Name": "A",
                    "Month": "A",
                    "Year": 1,
                    "Max Sustained Wind": 1,
                    "Areas Affected": ["area"],
                    "Damage": "Damages not recorded",
                    "Deaths": 1
                }
            ]
        }
        self.assertEqual(analyzer.aggregated_hurricane_records_by_year(hurricanes_by_name), expected)

    def test_should_aggregate_many_records_by_year_on_single_year(self):
        hurricanes_by_name = {
            "A": {
                "Name": "A",
                "Month": "A",
                "Year": 1,
                "Max Sustained Wind": 1,
                "Areas Affected": ["area"],
                "Damage": "Damages not recorded",
                "Deaths": 1
            },
            "B": {
                "Name": "B",
                "Month": "B",
                "Year": 1,
                "Max Sustained Wind": 2,
                "Areas Affected": ["A", "B"],
                "Damage": 500000,
                "Deaths": 2
            }
        }
        expected = {
            1: [
                {
                    "Name": "A",
                    "Month": "A",
                    "Year": 1,
                    "Max Sustained Wind": 1,
                    "Areas Affected": ["area"],
                    "Damage": "Damages not recorded",
                    "Deaths": 1
                },
                {
                    "Name": "B",
                    "Month": "B",
                    "Year": 1,
                    "Max Sustained Wind": 2,
                    "Areas Affected": ["A", "B"],
                    "Damage": 500000,
                    "Deaths": 2
                }
            ]
        }
        self.assertEqual(analyzer.aggregated_hurricane_records_by_year(hurricanes_by_name), expected)

    def test_should_aggregate_many_records_by_year_on_multiple_years(self):
        hurricanes_by_name = {
            "A": {
                "Name": "A",
                "Month": "A",
                "Year": 1,
                "Max Sustained Wind": 1,
                "Areas Affected": ["area"],
                "Damage": "Damages not recorded",
                "Deaths": 1
            },
            "B": {
                "Name": "B",
                "Month": "B",
                "Year": 1,
                "Max Sustained Wind": 2,
                "Areas Affected": ["A", "B"],
                "Damage": 500000,
                "Deaths": 2
            },
            "C": {
                "Name": "C",
                "Month": "C",
                "Year": 2,
                "Max Sustained Wind": 2,
                "Areas Affected": ["C"],
                "Damage": 500000,
                "Deaths": 2
            },
        }
        expected = {
            1: [
                {
                    "Name": "A",
                    "Month": "A",
                    "Year": 1,
                    "Max Sustained Wind": 1,
                    "Areas Affected": ["area"],
                    "Damage": "Damages not recorded",
                    "Deaths": 1
                },
                {
                    "Name": "B",
                    "Month": "B",
                    "Year": 1,
                    "Max Sustained Wind": 2,
                    "Areas Affected": ["A", "B"],
                    "Damage": 500000,
                    "Deaths": 2
                }
            ],
            2: [
                {
                    "Name": "C",
                    "Month": "C",
                    "Year": 2,
                    "Max Sustained Wind": 2,
                    "Areas Affected": ["C"],
                    "Damage": 500000,
                    "Deaths": 2
                }
            ]
        }
        self.assertEqual(analyzer.aggregated_hurricane_records_by_year(hurricanes_by_name), expected)


if __name__ == '__main__':
    unittest.main()
