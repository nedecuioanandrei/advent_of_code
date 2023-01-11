def main() -> int:
    ans = 0
    with open("in2", "r") as f:
        while True:
            test_case = f.readline()
            if not test_case:
                break
            numbers = test_case.split("x")
            numbers = [int(x) for x in numbers]
            lateral_areas = []
            lateral_areas.append(numbers[0] * numbers[1])
            lateral_areas.append(numbers[1] * numbers[2])
            lateral_areas.append(numbers[2] * numbers[0])
            area = 2 * sum(lateral_areas) + min(lateral_areas)
            ans += area;
            print(area)
    print(f"ans is {ans}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
