# Example use case of `fossa-deps.json` 

### What is this?
This repository shows an example of how to format a set of [referenced dependencies](https://github.com/fossas/fossa-cli/blob/master/docs/features/manual-dependencies.md).
The referenced dependencies actually come from GitHub, where we specify `git` as the type and provide the url of the repository as the `name`. `version` is optional; if it's not specified, FOSSA will resolve to the latest commit sha. `version` can reference:
- a tag/release that is known
- the latest commit sha of some branch
- or just any commit sha that you want to scan

### What do the results look like in FOSSA?

Here are some screenshots of what the results look like in FOSSA.

<img width="777" alt="image" src="https://user-images.githubusercontent.com/1427948/199325208-c9f6c081-71e2-49dd-bae8-537ddcd4131e.png">

<img width="521" alt="image" src="https://user-images.githubusercontent.com/1427948/199325340-92cb72a9-e204-4854-9b8f-6601ef0e2dd4.png">


<img width="818" alt="image" src="https://user-images.githubusercontent.com/1427948/199325276-7cd01987-ac16-4d7b-8ad1-cb25a6d1dda5.png">
