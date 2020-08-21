# gitlab-trigger-merge-request-opened

This trigger fires when a merge request is opened.

## Event data

| Key              | Description                                                           |
|------------------|-----------------------------------------------------------------------|
| url              | The merge request URL                                                  |
| branch           | The branch that the changes were merged into (target for the merge request) |
| repository       | The name of the repository                                            |
| repositoryURL    | The URL to the repository on GitLab                                   |
| repositoryGitURL | The URL to the repository as a git:// scheme                          |
| repositorySSHURL | The SSH-style URL                                                     |

## Example Trigger Configuration

```
parameters:
  branch:
    default: master
  repository:
    default: "kenazk/testing"

triggers:
- name: gitlab-merge-request-opened
  source:
    type: webhook
    image: relaysh/gitlab-trigger-merge-request-opened
  binding:
    parameters:
      repository: !Data repository
      branch: !Data branch
```
