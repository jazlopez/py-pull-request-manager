# py-pull-request-manager

Automatic Github&acute;pull request event manager.

##### 1. FEATURES

- Approve pending pull request
- Create pull request
- Comment pending pull request
- Request changes pull request


##### 2. INSTALLATION
    
> *IMPORTANT*:
> * require: python3 / pip3  
> * works: OSX / linux

Pip install packages

```bash
pip3 install -r requirements.txt
```

#####  3. USAGE

* approve pull request review

```bash
python3 main.py --login-name jaziel-lopez --review-event approve --review-comment "Approved."
```


* comment pull request review

```bash
python3 main.py --login-name jaziel-lopez --review-event comment --review-comment "I am a Pull Request Review Comment."
```

* request changes pull request review

```bash
python3 main.py --login-name jaziel-lopez --review-event request_changes --review-comment "Fix it."
```

* with cronjob (every 5 mins)

You will need the absolute path of main.py script to prevent path no found error(s).


```
echo $PWD/main.py # copy in clipboard
```

Now open your crontab amd paste the command you copied before.

```
crontab -e

*/5 * * * * python3 /full/path/to/main.py --login-name "your-login-name" --review-event approve --review-comment "Approved. Hey, I am using py-pull-request-manager by jazlopez. https://github.com/jazlopez/py-pull-request-manager"
```

Replace `/full/path/to/main.py` with the value you copied in the previous step. 

Also replace the value of `--login-name` for your username instead.

##### 4. HELP


```bash
usage: main.py [-h] --login-name LOGIN_NAME --review-event {approve,comment,request_changes} --review-comment REVIEW_COMMENT

arguments:

  -h, --help            show this help message and exit
  
  --login-name LOGIN_NAME Your github login name
  
  --review-event {approve,comment,request_changes}  Review event
  
  --review-comment REVIEW_COMMENT   Review comment
```

#### 5. LICENSE 

The Do What The Fuck You Want To Public License (WTFPL) is a free software license. There is a long ongoing battle between GPL zealots and BSD fanatics, about which license type is the most free of the two. In fact, both license types have unacceptable obnoxious clauses (such as reproducing a huge disclaimer that is written in all caps) that severely restrain our freedoms. The WTFPL can solve this problem.When analysing whether a license is free or not, you usually check that it allows free usage, modification and redistribution. Then you check that the additional restrictions do not impair fundamental freedoms. The WTFPL renders this task trivial: it allows everything and has no additional restrictions. How could life be easier? You just DO WHAT THE FUCK YOU WANT TO.

#### 6. CONTACT

Jaziel Lopez jlopez.mx
