# pyLinkwarden
A Python library and script archive for interacting with [Linkwarden](https://github.com/linkwarden/linkwarden).

Linkwarden is a self-hosted collaborative bookmark manager to collect, organize, and preserve webpages and articles.  Find out more about it on their [official website](https://linkwarden.app/) or their official [GitHub repo](https://github.com/linkwarden/linkwarden).

This repository contains a Python library that can be used to interact with Linkwarden.  It also includes useful, pre-made scripts that are ready-to-go.

# Installation
```
pip install pyLinkwarden
```

# Documentation
Full documentation can be found [here](https://tylwright.github.io/pyLinkwarden/pyLinkwarden.html).

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

# Example Usage
Please refer to the full documentation [here](https://tylwright.github.io/pyLinkwarden/pyLinkwarden.html) or see quick examples below.
## Importing the Module & Connecting to Linkwarden Instance
```
from pyLinkwarden.api import Client
c = Client(endpoint='https://linkwarden.example.com', access_token='<access token>')
```
<table>
    <thead>
        <tr>
            <th></th>
            <th>Task</th>
            <th>Code Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th rowspan='4'>Collections</th>
            <td>Return requests library response</td>
            <td><code>c.collections._get_raw()</code></td>
        </tr>
        <tr>
            <td>Return JSON</td>
            <td><code>c.collections._get()</code></td>
        </tr>
        <tr>
            <td>Return list</td>
            <td><code>c.collections.list()</code></td>
        </tr>
        <tr>
            <td>Delete</td>
            <td><code>c.collections.delete($id)</code></td>
        </tr>
        <tr>
            <th rowspan='4'>Links</th>
            <td>Return requests library response</td>
            <td><code>c.links._get_raw()</code></td>
        </tr>
        <tr>
            <td>Return JSON</td>
            <td><code>c.links._get()</code></td>
        </tr>
        <tr>
            <td>Return list</td>
            <td><code>c.links.list()</code></td>
        </tr>
        <tr>
            <td>Delete</td>
            <td><code>c.links.delete($id)</code></td>
        </tr>
        <tr>
            <th rowspan='5'>Tags</th>
            <td>Return requests library response</td>
            <td><code>c.tags._get_raw()</code></td>
        </tr>
        <tr>
            <td>Return JSON</td>
            <td><code>c.tags._get()</code></td>
        </tr>
        <tr>
            <td>Return list</td>
            <td><code>c.tags.list()</code></td>
        </tr>
        <tr>
            <td>Delete</td>
            <td><code>c.tags.delete($id)</code></td>
        </tr>
        <tr>
            <td>Rename</td>
            <td><code>c.tags.rename($id, '$new_name')</code></td>
        </tr>
    </tbody>
</table>