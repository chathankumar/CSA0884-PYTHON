def main():
    n = 100
    nth = 4
    factors = sorted(i for i in range(1, n + 1) if n % i == 0)
    print(f"Number of factors = {len(factors)}")
    print(f"{nth}th factor of {n} = {factors[nth - 1] if nth <= len(factors) else 'N/A'}")
if __name__ == "__main__":
    main()
