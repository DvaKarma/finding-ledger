import unittest, ledger
class T(unittest.TestCase):
    def test_ok(self):
        f=[{"id":1,"title":"x","severity":"high","evidence":"log","status":"verified"}]
        self.assertEqual(ledger.validate(f),[]); self.assertEqual(ledger.summary(f),{"high":{"verified":1}})
    def test_sem_evidencia(self):
        f=[{"id":1,"title":"x","severity":"low","evidence":" ","status":"verified"}]
        self.assertTrue(ledger.validate(f))
    def test_severidade(self):
        self.assertTrue(ledger.validate([{"id":1,"title":"x","severity":"zzz","evidence":"e","status":"unverified"}]))
unittest.main()
