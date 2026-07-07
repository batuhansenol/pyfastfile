def print_test_result(function_name: str, description: str, success: bool = True) -> None:
    color = "\033[92m" if success else "\033[91m"
    reset = "\033[0m"
    print(f"\n{color}{function_name}: {description}{reset}")
