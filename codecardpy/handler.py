import json

def handle(req):
    data = {'template': 'template4', 'title': 'Prasenjit Sarkar', 'subtitle': 'Cloud Native Evangelist', 'bodytext': 'Ask me anything on Cloud Native Application World! I run blog.kube-mesh.io', 'icon': 'microservices', 'backgroundColor': 'white'}
    return json.dumps(data)
