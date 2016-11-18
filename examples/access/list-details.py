import datetime
from mbed_cloud_sdk.access.accounts import AccountsAPI

def main():
    api = AccountsAPI()

    header = "All registered users in Organisation"
    print "%s\n%s" % (header, len(header) * "-")
    users = api.list_users()
    for u in users:
        print "\t- %s (%s - %s)" % (u.full_name, u.email, u.username)

    header = "\nAll registered groups in Organisation"
    print "%s\n%s" % (header, len(header) * "-")
    groups = api.list_groups()
    for g in groups:
        print "\t- %s" % (g.name)

    header = "\nAll registered API keys in Organisation"
    print "%s\n%s" % (header, len(header) * "-")
    keys = api.list_api_keys()
    for k in keys:
        last_used = datetime.datetime.fromtimestamp(k.last_login_time / 1000).strftime('%c') if k.last_login_time > 0 else "Never"
        print "\t- %s (Last used: %s)" % (k.name, last_used)

if __name__ == "__main__":
    main()
