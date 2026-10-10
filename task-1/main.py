from datetime import datetime

def get_days():
    user_input = input("Please enter the data in YYYY/mm/dd format: ")

    try:
        user_date = datetime.strptime(user_input, "%Y/%m/%d").date()

    except ValueError:

        print("Invalid date entered. Please try again using YYYY/mm/dd format.")
        return

    current_date = datetime.today().date()
    delta_days = user_date - current_date
    target_date = datetime.strftime(user_date, "%Y/%B/%d")

    if delta_days.days > 0:

        print(f"You have {delta_days.days} days left before {target_date}.")

    elif delta_days.days < 0:

        print(f"You have {delta_days.days} days passed since {target_date}.")

    else:

        user_date = user_date.replace(year=user_date.year + 1)
        delta_days = user_date - current_date
        print(f"You have {delta_days.days} days left before {target_date}.")

if __name__ == '__main__':
    get_days()
