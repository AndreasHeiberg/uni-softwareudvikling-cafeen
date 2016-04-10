class Notifications:
    
    def __init__(self, request):
        self.request = request

        if not self.request.session.get('notifications'):
            self.request.session['notifications'] = []

    def add(self, type, message):
        notifications = self.request.session['notifications']
        notifications.append({'type': type, 'message': message})
        self.request.session['notifications'] = notifications

    def all():
        return self.request.session['notifications']
