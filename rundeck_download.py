#!/usr/bin/python
import sys
import commands
import ast

def list_build_artifacts(organization, repo, branch, api_token, build):
    list_url = '"https://circleci.com/api/v1/project/' + organization + '/' \
             + repo + '/' + build + '/artifacts?circle-token=' + api_token \
             + '&branch=' + branch + '&filter=successful"'
    req = commands.getstatusoutput('curl -s ' + list_url)

    if 'not found' in req[1] or 'Not Found' in req[1]:
        print '[ERROR]   -   Invalid parameters.'
        sys.exit(1)

    return ast.literal_eval(req[1])

def dowload_artifacts(artifacts, api_token):
    print '[START]'
    count = 1
    for art in artifacts:
        art_name = art['pretty_path'].split('$CIRCLE_ARTIFACTS/')[1]
        art_url = art['url'] + '?circle-token=' + api_token
        print '[DOWNLOADING]   -   ' + str(count) + '\\' \
              + str(len(artifacts)) +  '   -   ' + art_name
        commands.getstatusoutput('curl ' + art_url + ' > ' + art_name)
        count += 1
    print '[DONE]'

def main():
    artifacts = list_build_artifacts(@option.ORGANIZATION@, @option.REPO@, @option.BRANCH@, @option.CIRCLE_API_TOKEN@, @option.BUILD@)

    if len(artifacts) == 0:
        print '[WARNING]   -   Build without artifacts.'
    else:
        dowload_artifacts(artifacts, @option.CIRCLE_API_TOKEN@)

main()
