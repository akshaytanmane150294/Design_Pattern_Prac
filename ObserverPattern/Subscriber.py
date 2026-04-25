from Publisher import Subject


class EmailService:
    def update(self, data):
        print(f"Email sent for: {data}")


class SMSService:
    def update(self, data):
        print(f"SMS sent for: {data}")


class AnalyticsServices:
    def update(self, data):
        print(f"Analytics Tracked: {data}")


# orderService = Subject()

# orderService.subscribe(EmailService())
# orderService.subscribe(SMSService())
# orderService.subscribe(AnalyticsServices())

# orderService.notify("Order #1234 placed")
