def main() -> int:
    lines = None
    with open("in", "r") as f:
        lines = f.readlines()
    
    for line in lines:
        q = line.split()
        print(q)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
