## Find Dead Links

This is a quick tool to find dead links in `.md` files in a git repo

It requires Python3.7

#### Usage

1. Clone this repo

```BASH
$ git clone https://github.com/markwinter/find-dead-links.git`
$ cd find-dead-links
```

2. Install the required python modules
```BASH
$ pip3 install -r requirements.txt
```

3. Edit the `MD_EXTENSION` if necessary (Default: `.md`)

4. Run the script with path to your git repo
```BASH
$ python3 find_dead_links.py ../path/to/repo
[*] Finding all .md pages
	[*] Found 185 pages
[*] Finding all links in pages
	[*] Found 1309 links
[*] Trying links
Page: /README.md, Link: https://github.com/kubeflow/manifests/tree/master/kfserving, Status: 404
```


#### Notes

1. HTTP links are requested with python requests

2. Other links are checked by trying to find the file locally

3. `HTTP 459` This error is Github rate limiting
