from django.core import mail

def worker(subscribers, post):
    # print(dir(subscribers[0]))
    
        # print("Send email from",us.user, "to", us.blog)
        
    with mail.get_connection() as connection:
        for us in subscribers:
            subject = "Post  added: "+post.title
            body = '''
                See http://testblog-workdb.rhcloud.com/fulllength?id={0}
            '''.format(post.id)
            mail.EmailMessage(subject, body, 'no-reply@testblog-workdb.rhcloud.com', [us.blog.email], connection=connection).send()