#!/usr/bin/python
import sys
import commands
import ast

def usage_message():
    print '[USAGE]       python script.py $ORGANIZATION  $REPO  $BRANCH  $CIRCLE_API_TOKEN $BUILD'
    print '[USAGE]       $BUILD   =  latest or build number'
    print '[USAGE]       -h, --help for usage message.'
    sys.exit(2)

def dowloading_message(art_name, count, total):
    print '[DOWNLOADING]   -   ' + str(count) + '\\' \
          + str(total) +  '   -   ' + art_name

def list_build_artifacts(organization, repo, branch, api_token, build):
    list_url = '"https://circleci.com/api/v1/project/' + organization + '/' \
             + repo + '/' + build + '/artifacts?circle-token=' + api_token \
             + '&branch=' + branch + '&filter=successful"'
    req = commands.getstatusoutput('curl -s ' + list_url)

    print 'curl -s ' + list_url

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
        dowloading_message(art_name, count, len(artifacts))
        commands.getstatusoutput('curl ' + art_url + ' > ' + art_name)
        count += 1
    print '[DONE]'

def main(argv):
    if len(argv) == 0 or len(argv) < 5 or '-h' in argv or '--help' in argv:
        usage_message()

    artifacts = list_build_artifacts(argv[0], argv[1], argv[2], argv[3], argv[4])

    if len(artifacts) == 0:
        print '[WARNING]   -   Build without artifacts.'
    else:
        dowload_artifacts(artifacts, argv[3])

main(sys.argv[1:])
