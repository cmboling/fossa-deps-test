# Example use case of `fossa-deps.json` 

### What is this?
This repository shows an example of how to format a set of [referenced dependencies](https://github.com/fossas/fossa-cli/blob/master/docs/features/manual-dependencies.md).
The referenced dependencies actually come from GitHub, where we specify `git` as the type and provide the url of the repository as the `name`. `version` is optional; if it's not specified, FOSSA will resolve to the latest commit sha. `version` can reference:
- a tag/release that is known
- the latest commit sha of some branch
- or just any commit sha that you want to scan

### What do the results look like in FOSSA (as of 11/1/2022)?

Here are some screenshots of what the results look like in FOSSA.

<img width="777" alt="image" src="https://user-images.githubusercontent.com/1427948/199325208-c9f6c081-71e2-49dd-bae8-537ddcd4131e.png">

Notice that FOSSA pulls in the [latest commit sha](https://github.com/google/benchmark/commit/398a8ac2e8e0b852fa1568dc1c8ebdfc743a380a) if no `version` is specified for this particular referenced dependency.

<img width="521" alt="image" src="https://user-images.githubusercontent.com/1427948/199325340-92cb72a9-e204-4854-9b8f-6601ef0e2dd4.png">

Similarly, when we do specify a version as an actual version/tag or even a commit sha, FOSSA will resolve to it and will provide the commit sha when you hover over the dependency.

<img width="643" alt="image" src="https://user-images.githubusercontent.com/1427948/199326506-29893661-f71f-4842-8de5-3739cac370cf.png">


<img width="818" alt="image" src="https://user-images.githubusercontent.com/1427948/199325276-7cd01987-ac16-4d7b-8ad1-cb25a6d1dda5.png">

### Project attribution report

<img width="1535" alt="image" src="https://user-images.githubusercontent.com/1427948/205160995-206df5ee-9acc-4932-a1ae-de49e02c6d2b.png">

Click [here](https://app.fossa.com/attribution/e3f1a598-a28d-417d-bc41-2a240d075c7c) to download this example public report.
