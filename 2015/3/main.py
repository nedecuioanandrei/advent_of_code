def main() -> int:
    with open("in", "r") as f:
        while True:
            line = f.readline()
            if not line:
                break

            houses = set()
            x = 0
            y = 0 
            for c in line:
                if c == '>':
                    x += 1 
                if c == '<':
                    x -= 1
                if c == '^':
                    y += 1
                if c == 'v':
                    y -= 1
                houses.add((x, y))
            print(len(houses))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
