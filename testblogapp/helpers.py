def worker(subscribers, post):
    for us in subscribers:
        print(us.username, us.email)