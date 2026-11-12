import json
import unittest
from pathlib import Path


class StudyInputTests(unittest.TestCase):
    def test_domain_references_and_units(self):
        data=json.loads((Path(__file__).resolve().parents[1]/'fixtures/study-input.json').read_text())
        from forecast.batches import Batch
        Batch.parse(data['document'])
        cells=data['document']['population']
        self.assertEqual(len(cells), len({(r['year'],r['region'],r['settlement'],r['age']) for r in cells}))
        self.assertTrue(all(type(r['count']) is int and r['count']>=0 for r in cells))
