## Find Dead Links

This is a quick tool to find dead links in `.md` files in a github repo

It requires Python3.7

#### Usage

1. Clone
`$ git clone https://github.com/markwinter/find-dead-links.git`

2. Install the required python modules
```BASH
$ cd find-dead-links
$ pip3 install -r requirements.txt
```

3. Edit the `MD_EXTENSION` and `BASE_URL` in the script

4. Run the script with path to your git repo
```BASH
$ python3 find_dead_links.py ../path/to.repo
[*] Finding all .md pages
	[*] Found 185 pages
[*] Finding all links in pages
	[*] Found 1309 links
[*] Trying links
Page: /README.md, Link: https://github.com/kubeflow/manifests/tree/master/kfserving, Status: 404
```
