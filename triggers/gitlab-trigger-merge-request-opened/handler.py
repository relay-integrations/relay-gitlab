from nebula_sdk import Interface, WebhookServer, Dynamic as D
from quart import Quart, request, jsonify, make_response

import logging

relay = Interface()
app = Quart('merge-request-merged')

logging.getLogger().setLevel(logging.INFO)


@app.route('/', methods=['POST'])
async def handler():
    gitlab_event = request.headers.get('X-Gitlab-Event')

    if gitlab_event is None:
        return {'message': 'not a valid GitLab event'}, 400, {}
    if gitlab_event == 'ping':
        return {'message': 'success'}, 200, {}
    if gitlab_event != 'Merge Request Hook':
        return {'message': 'only merge request events are supported'}, 400, {}

    logging.info("Received event from GitLab: {}".format(gitlab_event))

    event_payload = await request.get_json()
    logging.info("Received the following webhook payload: \n%s", json.dumps(event_payload, indent=4))
    
    if event_payload is None:
        return {'message': 'not a valid GitLab event'}, 400, {}

    mergerequest = event_payload

    if mergerequest['object_attributes']['action'] == 'open' and mergerequest['object_attributes']['state'] == 'opened':
        relay.events.emit({
            'url': mergerequest['object_attributes']['url'],
            'repository': mergerequest['repository']['name'],
            'repositoryURL': mergerequest['repository']['homepage'],
            'repositoryGitURL': mergerequest['repository']['url'],
            'repositorySSHURL': mergerequest['object_attributes']['source']['git_ssh_url'],
            'branch': mergerequest['object_attributes']['target_branch']
        })

    return {'message': 'success'}, 200, {}


if __name__ == '__main__':
    WebhookServer(app).serve_forever()
