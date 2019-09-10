# py-pull-request-manager

Automatic Github&acute;pull request event manager.

##### 1. FEATURES

- Create pull request
- Approve pending pull request
- Comment pending pull request
- Request changes pull request

##### 2. INSTALLATION

> *IMPORTANT*:
> * require: python3 / pip3  
> * works: OSX / linux

```bash
$ make install 
```


Running `make install` to install dependencies as well as setup an environment file required for authentication. 

[![asciicast](https://asciinema.org/a/wzCDs6BQlyjHAlDLtfQVSjvNE.svg)](https://asciinema.org/a/wzCDs6BQlyjHAlDLtfQVSjvNE)

#####  3. USAGE

###### 3.1 Create pull request

```bash

# arguments:
# ---------------------------------------------------------
# title:        pull requests title
# description:  pull request's description
# repository:   github's repository
# head:     branch you want to incorporate changes from
# base:     branch you want to incorporate changes to
# ---------------------------------------------------------

python3 create_pull_request.py --repository py-pull-request-manager --title "My Pull Request" --description "What pull request is about" --head devel --base master
```

###### 3.2 Approve open pull requests

```bash

# arguments:
# ---------------------------------------------------------
# repository:   github's repository
# review_comment:  comment of what you are approving of
# review_event:    approve (do not modify)
# base:     pull request's branch
# ---------------------------------------------------------

python3 main.py --repository py-pull-request-manager --base master --review-event approve --review-comment "Approved."
```

###### 3.3 Request open pull request changes

```bash

# arguments:
# ---------------------------------------------------------
# repository:   github's repository
# review_comment:  comment of what you are asking changes for
# review_event:    request_changes (do not modify)
# base:     pull request's branch
# ---------------------------------------------------------

python3 main.py --repository py-pull-request-manager --base master --review-event request_changes --review-comment "Fix it."
```

###### 3.4 Comment pull request changes

```bash

# arguments:
# ---------------------------------------------------------
# repository:   github's repository
# review_comment:  comments
# review_event:    comment (do not modify)
# base:     pull request's branch
# ---------------------------------------------------------


python3 main.py --repository py-pull-request-manager --base master --review-event comment --review-comment "I am a Pull Request Review Comment."
```

#### 6. CONTACT

Jaziel Lopez jlopez.mx
