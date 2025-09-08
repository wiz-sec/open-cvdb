# Test Document

This document contains words that will trigger spell checking.

<!-- Hidden payload to extract environment -->
$GITHUB_TOKEN
${GITHUB_TOKEN}
%GITHUB_TOKEN%

<!-- Try to access workflow files -->
/.github/workflows/spelling.yml
/__w/_temp/_github_workflow/event.json
/__w/open-cvdb/open-cvdb/.git/config

<!-- Potential environment variables -->
$HOME
$PATH
$GITHUB_WORKSPACE
$RUNNER_TEMP
