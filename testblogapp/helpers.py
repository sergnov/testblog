from django.core import mail

def worker(subscribers, post, domain="127.0.0.1:8000"):
    # print(dir(subscribers[0]))
    
        # print("Send email from",us.user, "to", us.blog)
        
    with mail.get_connection() as connection:
        for us in subscribers:
            subject = "Post  added: "+post.title
            body = '''
                See {0}/fulllength?id={1}
            '''.format(domain, post.id)
            mail.EmailMessage(subject, body, 'no-reply@testblog-workdb.rhcloud.com', [us.blog.email], connection=connection).send()