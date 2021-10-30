# LibGD website

## Flow

This is the repository for our website at https://libgd.org/.
The source is structured text under the content/ directory.

The main branch (master) is where all changes must be applied (updates, news,
announces or PRs).  This is your normal development & review cycle.

GitHub actions will automatically compile & push the output to the gh-pages
branch.  The `make github` in here is used to automate that process.  You do
not need to push to the gh-pages branch yourself.

Those pages are then hosted using [Github Pages](https://pages.github.com/).

## Tools

We use the [Pelican Static Site Generator](https://blog.getpelican.com/) project
to turn the structured text into html.

We currently pin the version of Pelican due to random breaking changes that new
versions introduce.  See the requirements.txt file for the current version.

## Release Process

When making a new GD release, make sure to update:
* content/release-$VER.rst: Announce w/snippet from GD's CHANGELOG.md.
* content/pages/documentation.rst: Link to new manual (see next).
* content/manuals/$VER/: Version specific manual (see below).

All the indexes and such will automatically update after that.

### Manual Generation

With a release tarball, run:

```sh
$ gd-$VER/docs/naturaldocs/run_docs.sh
$ cp -a gd-$VER/docs/naturaldocs/html/ content/manuals/$VER/
```
