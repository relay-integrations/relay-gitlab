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