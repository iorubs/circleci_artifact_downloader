# CircleCI Artifact Downloader  
Python script for downloading artifacts from CircleCI, manually or through RunDeck. Small Companies and individuals probably do not require a full artifact manager like Artifactory. CircleCI has the capability to hold on to it's build artifact, so if you are looking for a free artifact managing solution I suggest the use of CircleCI in addition to this downloading script.  

### Instructions:  
Currently the scripts downloads the artifacts for the most recent successful build. You can generate a new CircleCI API token, under account settings.  
The Rundeck downloader script, should be similar to the one required for other job Automation/Scheduler tools, so you may use that as a base to create your own if needed.  

#### Manual:
1 - `python manual_download.py  $ORGANIZATION  $REPO  $BRANCH  $CIRCLE_API_TOKEN $BUILD`  
2 - For the last successful build, supply 'latest' for $BUILD, other wise supply a build number.  

#### RunDeck:  
You must create the following variables before executing the job: ORGANIZATION, REPO, BRANCH and CIRCLE_API_TOKEN. Then add a new step to your execution job, select inline script and copy paste the contents of rundeck_download.py.  

### TODO list:  
1 - Change param parser for something like argparse.  
