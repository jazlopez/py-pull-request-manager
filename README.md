# py-pull-request-manager

Automatic Github&acute;pull request event manager.

##### FEATURES

- Approve pending pull request
- Comment pending pull request
- Request changes pull request

##### INSTALLATION
    
> *IMPORTANT*:
> * require: python3 / pip3  
> * works: OSX / linux

Pip install packages

```bash
pip3 install -r requirements.txt
```

#####  USAGE

```bash
usage: main.py [-h] --login-name LOGIN_NAME --review-event {approve,comment,request_changes} --review-comment REVIEW_COMMENT

arguments:

  -h, --help            show this help message and exit
  
  --login-name LOGIN_NAME Your github login name
  
  --review-event {approve,comment,request_changes}  Review event
  
  --review-comment REVIEW_COMMENT   Review comment
```

##### SCHEDULED SERVICE


#### COVERAGE

#### Coverage report 98%

* #### client.py
  * 14 statements
  * 0 missing
  * 0 excluded
  
* #### tests/client.py
  * 33 statements
  * 1 missing
  * 0 excluded

#### LICENSE 

The Do What The Fuck You Want To Public License (WTFPL) is a free software license. There is a long ongoing battle between GPL zealots and BSD fanatics, about which license type is the most free of the two. In fact, both license types have unacceptable obnoxious clauses (such as reproducing a huge disclaimer that is written in all caps) that severely restrain our freedoms. The WTFPL can solve this problem.When analysing whether a license is free or not, you usually check that it allows free usage, modification and redistribution. Then you check that the additional restrictions do not impair fundamental freedoms. The WTFPL renders this task trivial: it allows everything and has no additional restrictions. How could life be easier? You just DO WHAT THE FUCK YOU WANT TO.
