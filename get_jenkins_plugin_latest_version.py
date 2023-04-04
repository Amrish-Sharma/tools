import requests

def get_plugin_latest_version(plugin_name):
    url = f'https://updates.jenkins.io/current/update-center.actual.json?plugin={plugin_name}'
    response = requests.get(url)
    response.raise_for_status()  # raise an exception if the request fails
    data = response.json()
    if plugin_name in data.get('plugins', {}):
        return data['plugins'][plugin_name]['version']
    return None

# Example input of list of plugins in each new line
plugin_list = """
job-dsl
extensible-choice-parameter
anything-goes-formatter
role-strategy
rebuild
envinject
snakeyaml-api
pipeline-utility-steps
validating-string-parameter
uno-choice
ansicolor
authorize-project
bootstrap4-api
branch-api
build-timeout
credentials
credentials-binding
durable-task
structs
echarts-api
email-ext
cloudbees-folder
font-awesome-api
git-client
git
git-server
github-api
github
jackson2-api
jjwt-api
ace-editor
handlebars
jquery-detached
workflow-api
workflow-step-api
momentjs
jquery
matrix-project
jquery3-api
jsch
junit
list-git-branches-parameter
antisamy-markup-formatter
apache-httpcomponents-client-4-api
lockable-resources
okhttp-api
permissive-script-security
script-security
workflow-aggregator
workflow-basic-steps
pipeline-build-step
pipeline-model-definition
pipeline-model-extensions
pipeline-github-lib
workflow-cps
pipeline-input-step
workflow-job
pipeline-milestone-step
pipeline-model-api
workflow-multibranch
workflow-durable-task-step
pipeline-rest-api
workflow-scm-step
workflow-cps-global-lib
pipeline-stage-step
pipeline-stage-tags-metadata
pipeline-stage-view
workflow-support
plain-credentials
plugin-util-api
popper-api
pipeline-graph-analysis
resource-disposer
saml
resource-disposer
ssh-slaves
ssh-credentials
timestamper
token-macro
ws-cleanup
"""

plugins = plugin_list.strip().split('\n')

for plugin in plugins:
    latest_version = get_plugin_latest_version(plugin)
    if latest_version:
        print(f'{plugin}=={latest_version}')
    else:
        print(f'Unable to fetch the latest version of {plugin}')
