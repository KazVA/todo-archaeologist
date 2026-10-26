def calculate_total(items):
    # TODO: Handle discounts for returning customers
    total = sum(items)
    return total


def authenticate_user(username, password):
    # FIXME: Replace this placeholder with proper authentication
    return username == "admin" and password == "password"


def export_report(data):
    # HACK: Temporary workaround until CSV export is implemented
    return str(data)


def main():
    items = [100, 200, 300]
    print("Total:", calculate_total(items))
    print("Report:", export_report(items))


if __name__ == "__main__":
    main()