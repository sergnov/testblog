def worker(subscribers, post):
    # print(dir(subscribers[0]))
    for us in subscribers:
        print("Send email from",us.user, "to", us.blog)