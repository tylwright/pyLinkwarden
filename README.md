# pyLinkwarden
A Python library and script archive for interacting with [Linkwarden](https://github.com/linkwarden/linkwarden).

Linkwarden is a self-hosted collaborative bookmark manager to collect, organize, and preserve webpages and articles.  Find out more about it on our [official website](https://linkwarden.app/) or our official [GitHub repo](https://github.com/linkwarden/linkwarden).

This repository contains a Python library that can be used to interact with Linkwarden.  It also includes useful, pre-made scripts that are ready-to-go.

# Installation
```
pip install pyLinkwarden
```

# Documentation
Full documentation can be found [here](/build/index.html).

## Example Usage
```
from pyLinkwarden.api import Client
c = Client(endpoint='https://linkwarden.example.com', access_token='<access token>')

c.collections.list()
c.links.list()
c.tags.list()

c.tags.rename(<tag_id>, 'New Name')
```

# Capabilities
This library is a work in progress and will continue to gain new functionality.  Here is what you can expect from the current release:
<table style='text-align: center;'>
    <thead>
        <tr>
            <th rowspan='2'></th>
            <th style='text-align: center;' colspan='5'>Ability</th>
        </tr>
        <tr>
            <th>Get</th>
            <th>List</th>
            <th>Create</th>
            <th>Rename</th>
            <th>Delete</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th style='text-align: right;'>Collections</th>
            <td>✅</td>
            <td>✅</td>
            <td></td>
            <td></td>
            <td>✅</td>
        </tr>
        <tr>
            <th style='text-align: right;'>Links</th>
            <td>✅</td>
            <td>✅</td>
            <td></td>
            <td></td>
            <td>✅</td>
        </tr>
        <tr>
            <th style='text-align: right;'>Tags</th>
            <td>✅</td>
            <td>✅</td>
            <td></td>
            <td>✅</td>
            <td>✅</td>
        </tr>
    </tbody>
</table>
