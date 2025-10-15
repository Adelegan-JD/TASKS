from http.server import BaseHTTPRequestHandler, HTTPServer
import json
data = [
    {'personal_info' : {
        'Name' : 'Deborah Adelegan',
        'Track': 'AI Engineer',
        'Course': 'Backend Engineering'},
    'scores' : {
        'MCQ': '95',
        'Applied Theory': '90'
    }
    }
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status = 200):
        self.send_response(status)
        self.send_header('content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_PUT(self):
        
        self.send_data(data)



def run():
    HTTPServer(('localhost', 8000), BasicAPI).serve_forever()


print('Application is running')
run()