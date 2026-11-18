#!/usr/bin/env python3
"""finding-ledger: valida e resume achados de auditoria em JSON (id, severidade, evidencia, status)."""
import json, sys, collections
SEV = ["critical", "high", "medium", "low", "info"]
REQ = {"id", "title", "severity", "evidence", "status"}
def validate(items):
    errs = []
    for i, f in enumerate(items):
        miss = REQ - set(f)
        if miss: errs.append(f"#{i}: faltam campos {sorted(miss)}")
        elif f["severity"] not in SEV: errs.append(f"#{i}: severidade invalida {f['severity']}")
        elif f["status"] == "verified" and not str(f["evidence"]).strip(): errs.append(f"#{i}: verificado sem evidencia")
    return errs
def summary(items):
    c = collections.Counter((f["severity"], f["status"]) for f in items)
    return {s: {st: c[(s, st)] for st in ("verified", "unverified") if c[(s, st)]} for s in SEV if any(k[0] == s for k in c)}
if __name__ == "__main__":
    data = json.load(open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin)
    e = validate(data)
    if e: print("\n".join(e)); sys.exit(1)
    print(json.dumps(summary(data), indent=2))
