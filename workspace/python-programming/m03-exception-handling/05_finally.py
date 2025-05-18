try:
    print("DB Connection")
    print("Transaction 01")
    print(f"Transaction 02 {1/1}")
except Exception:
    print("Transaction failed")
else:
    print("All transaction successful")
finally:
    print("Closing connection")