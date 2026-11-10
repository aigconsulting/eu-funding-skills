#!/usr/bin/env python3
"""Unit test aritmetici; NON test di compliance con bandi."""
import copy
import unittest

from estimate_grant import InvalidScenario, estimate


BASE = {
    "scenario": "Esempio didattico, non collegato a topic",
    "direct_eligible": {
        "personnel": "100000.00", "purchases": "30000.00",
        "subcontracting": "20000.00", "third_party_support": "0.00"
    },
    "other_eligible": "0.00",
    "indirect_rate": "0.25",
    "indirect_base_categories": ["personnel", "purchases"],
    "funding_rate": "0.70",
    "non_eligible": "10000.00",
    "grant_cap": None,
}


class TestIllustrativeCalculation(unittest.TestCase):
    def test_base_example_excludes_subcontract_from_indirect(self):
        result = estimate(BASE)
        self.assertEqual(result["direct_eligible"], "150000.00")
        self.assertEqual(result["indirect_base"], "130000.00")
        self.assertEqual(result["indirect_estimate"], "32500.00")
        self.assertEqual(result["eligible_total"], "182500.00")
        self.assertEqual(result["estimated_grant"], "127750.00")
        self.assertEqual(result["eligible_cofinancing"], "54750.00")
        self.assertEqual(result["estimated_funding_gap"], "64750.00")

    def test_cap_reduces_grant_not_budget(self):
        data = {**BASE, "grant_cap": "50000.00"}
        result = estimate(data)
        self.assertEqual(result["estimated_grant"], "50000.00")
        self.assertEqual(result["eligible_cofinancing"], "132500.00")
        self.assertEqual(result["estimated_funding_gap"], "142500.00")

    def test_no_indirect(self):
        data = {**BASE, "indirect_base_categories": [], "indirect_rate": "0"}
        self.assertEqual(estimate(data)["estimated_grant"], "105000.00")

    def test_rate_out_of_range_fails(self):
        with self.assertRaises(InvalidScenario):
            estimate({**BASE, "funding_rate": "1.20"})

    def test_unknown_indirect_category_fails(self):
        with self.assertRaises(InvalidScenario):
            estimate({**BASE, "indirect_base_categories": ["grant_bonus"]})

    def test_duplicate_indirect_category_fails(self):
        with self.assertRaises(InvalidScenario):
            estimate({**BASE, "indirect_base_categories": ["personnel", "personnel"]})

    def test_negative_or_nan_fails(self):
        for val in ("-1", "NaN", "Infinity"):
            with self.subTest(val=val), self.assertRaises(InvalidScenario):
                estimate({**BASE, "non_eligible": val})

    def test_omitted_field_fails(self):
        data = copy.deepcopy(BASE)
        del data["funding_rate"]
        with self.assertRaises(InvalidScenario):
            estimate(data)

    def test_boolean_or_float_fails(self):
        for val in (True, 0.70):
            with self.subTest(val=val), self.assertRaises(InvalidScenario):
                estimate({**BASE, "funding_rate": val})

    def test_unknown_cap_is_not_zero(self):
        self.assertIsNone(estimate(BASE)["grant_cap"])
        self.assertEqual(estimate({**BASE, "grant_cap": "0"})["estimated_grant"], "0.00")


if __name__ == "__main__":
    unittest.main()
