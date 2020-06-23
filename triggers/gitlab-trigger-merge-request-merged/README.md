# gitlab-trigger-merge-request-merged

This trigger fires when a PR is merged.

## Event data

| Key              | Description                                                           |
|------------------|-----------------------------------------------------------------------|
| url              | The pull request URL                                                  |
| branch           | The branch that the changes were pulled into (destination for the PR) |
| repository       | The name of the repository as username/repo-name                      |
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
- name: gitlab-merge-request-merged
  source:
    type: webhook
    image: relaysh/gitlab-trigger-merge-request-merged
  binding:
    parameters:
      repository: !Data repository 
      branch: !Data branch
```