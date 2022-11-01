# Example use case of `fossa-deps.json` 

This repository shows an example of how to format a set of [referenced dependencies](https://github.com/fossas/fossa-cli/blob/master/docs/features/manual-dependencies.md).
The referenced dependencies actually come from GitHub, where we specify `git` as the type and provide the url of the repository as the `name`. `version` is optional; if it's not specified, FOSSA will resolve to the latest commit sha. `version` can reference a tag that is known; it can also be the latest commit sha of some branch.
