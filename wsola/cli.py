import argparse
import wsola as m


def main():
    ap = argparse.ArgumentParser(description="变速不变调")
        ap.add_argument("--speed", type=float, required=True)
        ap.add_argument("--out", required=True)
    a = ap.parse_args()
        print("TODO")


if __name__ == "__main__":
    main()
