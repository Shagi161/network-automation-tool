import csv
from ping_check import ping
from report import save_csv_report, save_summary
from utils import now_timestamp, ensure_output_dir

def load_devices(csv_path: str = "devices.csv"):
    devices = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            devices.append({"name": row["name"].strip(), "ip": row["ip"].strip()})
    return devices

def main():
    devices = load_devices()
    results = []

    for d in devices:
        status = "UP" if ping(d["ip"]) else "DOWN"
        results.append({"name": d["name"], "ip": d["ip"], "status": status})
        print(f"{d['name']} ({d['ip']}) -> {status}")

    out_dir = ensure_output_dir()
    ts = now_timestamp()

    csv_report = out_dir / f"report_{ts}.csv"
    txt_summary = out_dir / f"summary_{ts}.txt"

    save_csv_report(csv_report, results)
    save_summary(txt_summary, results)

    print("\nReports saved:")
    print(f"- {csv_report}")
    print(f"- {txt_summary}")

if __name__ == "__main__":
    main()

