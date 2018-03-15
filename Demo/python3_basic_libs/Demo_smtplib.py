import smtplib


server = smtplib.SMTP('localhost')

letter = """To: To @example.org \n\
            From: From @example.org \n\
            Attaboy!
        """

print letter
server.sendmail('From @example.org', 'To @example.org',letter )


server.quit()
