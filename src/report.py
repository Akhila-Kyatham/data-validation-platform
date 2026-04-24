def generate_report(results):
    print("\n--- Data Validation Report ---")
    for test, result in results.items():
        status = "PASS ✅" if result else "FAIL ❌"
        print(f"{test}: {status}")