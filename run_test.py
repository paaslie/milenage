from datetime import datetime

from milenage1 import Milenage, compute_opc
from test207 import TEST_VECTORS


def hx(s):
    return bytes.fromhex(s)


def verify(name, actual, expected):

    if actual.hex().lower() == expected.lower():
        print(f"   {name:<6} PASS")
        return True

    print(f"   {name:<6} FAIL")
    print(f"      expected {expected}")
    print(f"      actual   {actual.hex()}")

    return False


def write_log(message):

    with open("milenage_test_log.txt", "a",
              encoding="utf-8") as f:

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        f.write(f"[{timestamp}] {message}\n")


total = 0
passed = 0

for test in TEST_VECTORS:

    print()
    print("=" * 60)
    print(f"TEST SET {test['id']}")
    print("=" * 60)

    k = hx(test["K"])
    rand = hx(test["RAND"])
    sqn = hx(test["SQN"])
    amf = hx(test["AMF"])
    op = hx(test["OP"])

    opc = compute_opc(k, op)

    m = Milenage(k, opc)

    ok = True

    ok &= verify(
        "f1",
        m.f1(rand, sqn, amf),
        test["MAC_A"]
    )

    ok &= verify(
        "f2",
        m.f2(rand),
        test["RES"]
    )

    ok &= verify(
        "f3",
        m.f3(rand),
        test["CK"]
    )

    ok &= verify(
        "f4",
        m.f4(rand),
        test["IK"]
    )

    ok &= verify(
        "f5",
        m.f5(rand),
        test["AK"]
    )

    total += 1

    if ok:
        passed += 1
        write_log(f"Dataset {test['id']} PASS")
    else:
        write_log(f"Dataset {test['id']} FAIL")

print()
print("=" * 60)
print(f"RESULTAT: {passed}/{total} PASS")
print("=" * 60)

write_log(f"SUMMARY {passed}/{total} PASS")