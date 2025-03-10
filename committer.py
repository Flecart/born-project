import os
from datetime import datetime
from datetime import timedelta

data = [
    "2002-01-06",
    "2002-01-07",
    "2002-01-08",
    "2002-01-09",
    "2002-01-10",
    "2002-01-11",
    "2002-01-12",
    "2002-01-13",
    "2002-01-16",
    "2002-01-19",
    "2002-01-20",
    "2002-01-23",
    "2002-01-26",
    "2002-01-28",
    "2002-01-29",
    "2002-01-31",
    "2002-02-01",  # finish B
    "2002-02-11",
    "2002-02-12",
    "2002-02-13",
    "2002-02-14",
    "2002-02-15",
    "2002-02-17",
    "2002-02-23",
    "2002-02-24",
    "2002-03-02",
    "2002-03-03",
    "2002-03-09",
    "2002-03-11",
    "2002-03-12",
    "2002-03-13",
    "2002-03-14",
    "2002-03-15", # finish O
    "2002-03-24",
    "2002-03-25",
    "2002-03-26",
    "2002-03-27",
    "2002-03-28",
    "2002-03-29",
    "2002-03-30",
    "2002-03-31",
    "2002-04-03",
    "2002-04-07",
    "2002-04-10",
    "2002-04-15",
    "2002-04-16",
    "2002-04-18",
    "2002-04-19",
    "2002-04-20", # finish R
    "2002-04-28",
    "2002-04-29",
    "2002-04-30",
    "2002-05-01",
    "2002-05-02",
    "2002-05-03",
    "2002-05-04",
    "2002-05-06",
    "2002-05-14",
    "2002-05-15",
    "2002-05-16",
    "2002-05-24",
    "2002-05-26",
    "2002-05-27",
    "2002-05-28",
    "2002-05-29",
    "2002-05-30",
    "2002-05-31",
    "2002-06-01", # finish N

    "2002-06-16",
    "2002-06-23",
    "2002-06-30",
    "2002-07-01",
    "2002-07-02",
    "2002-07-03",
    "2002-07-04",
    "2002-07-05",
    "2002-07-06",
    "2002-07-07",
    "2002-07-14", # FINISH T
    "2002-07-28",
    "2002-07-29",
    "2002-07-30",
    "2002-07-31",
    "2002-08-01",
    "2002-08-02",
    "2002-08-03",
    "2002-08-07",
    "2002-08-14",
    "2002-08-21",
    "2002-08-28",
    "2002-09-01",
    "2002-09-02",
    "2002-09-03",
    "2002-09-04",
    "2002-09-05",
    "2002-09-06",
    "2002-09-07", # Finish H

    "2002-09-15",
    "2002-09-16",
    "2002-09-17",
    "2002-09-18",
    "2002-09-19",
    "2002-09-20",
    "2002-09-21", # FInish I

    "2002-09-30",
    "2002-10-01",
    "2002-10-04",
    "2002-10-06",
    "2002-10-09",
    "2002-10-12",
    "2002-10-13",
    "2002-10-16",
    "2002-10-19",
    "2002-10-21",
    "2002-10-24",
    "2002-10-25", # Finish S

    "2002-11-10",
    "2002-11-18",
    "2002-11-19",
    "2002-11-26",
    "2002-11-27",
    "2002-11-28",
    "2002-11-29",
    "2002-11-30",
    "2002-12-02",
    "2002-12-03",
    "2002-12-08", # Finish Y
]

def transform_dates(data: list[str]) -> list[datetime]:
    result = []
    for date in data:
        string_format = datetime.strptime(date, "%Y-%m-%d") + timedelta(hours=12)
        
        result.append(string_format)

    return result

data_sorted = sorted(transform_dates(data))


def get_commit_dates(date: datetime):
    os.makedirs("data", exist_ok=True)

    datestring = date.strftime("%Y-%m-%d")
    if os.path.exists(f"data/{datestring}"):
        return
    with open(f"data/{datestring}", "w") as f:
        f.write(datestring + "\n")

    # git commit -m "Add commit date"

    os.system("git add .")
    os.system(f"GIT_COMMITTER_DATE={date.isoformat()} git commit -m 'Add commit date {datestring}' --date={date.isoformat()}")

# Just a funny project to print a text in the github contributor view.
if __name__ == "__main__":
    for date in data_sorted:
        get_commit_dates(date)