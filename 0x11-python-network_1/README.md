<h3 align="center">ALX software engineering project on python networking using urlib library and request library </h3>
<p>The project tutorial was put together by:Guillaume, CTO at Holberton School in ALX Python
Scripting
Back-end
API  </p>

<p>The project has a weight of 1 and took place between Dec 1, 2023 6:00 AM to Dec 2, 2023 6:00 AM. And an autoreview was launched at the deadline of the project </p>
<ul>
 <p>Here are the resources for the tasks: Read or watch the following </p>
<li><a href="https://docs.python.org/3/howto/urllib2.html">HOWTO Fetch Internet Resources Using urllib Package</a></li>
<li><a href=""https://requests.readthedocs.io/en/latest/>Quickstart with Requests package</a></li>
<li><a href="https://pypi.org/project/requests/">Request package</a></li>
</ul>
<p><em><h4>Learning Objectives</h4></em></p>
<p>At the end of this project, you are expected to be able to explain to anyone, without the help of Google:</p>
<ul>
<li>How to fetch internet resources with the Python package urllib</li>
<li>How to decode urllib body response</li>
<li>How to use the Python package requests #requestsiswaysimplerthanurllib</li>
<li>How to make HTTP GET request</li>
<li>How to make HTTP POST/PUT/etc. request</li>
<li>How to fetch JSON resources</li>
<li>How to manipulate data from an external service</li>
</ul>
<p><h4><em>Copyright - Plagiarism</em></h4></p>
<ul>
<li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
<li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.</li>
<li>You are not allowed to publish any content of this project.</li>
</ul>
<strong>
<h4>- Any form of plagiarism is strictly forbidden and will result in removal from the program.</h4>
</strong>
<p>General Requirements:</p>
<ul>
<li>Allowed editors: vi, vim, emacs</li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly #!/usr/bin/python3</li>
<li>A README.md file at the root of the repo, containing a description of the repository</li>
<li>A README.md file, at the root of the folder of this project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.8.*)</li>
<li>Allowed editors: vi, vim, emacs</li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly #!/usr/bin/python3</li>
<li>A README.md file at the root of the repo, containing a description of the repository</li>
<li>A README.md file, at the root of the folder of this project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.8.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using wc</li>
<li>All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')</li>
<li>You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)</li>
<li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
<li>Your code should not be executed when imported (by using if __name__ == "__main__":)</li>
</ul>

<p>TASKS</>
<ul>
<li>0. What's my status? #0
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following example (tabulation before -)
You must use a with statement
guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 0-hbtn_status.py</li>
<li>1. Response header value #0
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

You must use the packages urllib and sys
You are not allow to import packages other than urllib and sys
The value of this variable is different for each request
You don’t need to check arguments passed to the script (number or type)
You must use a with statement
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 1-hbtn_header.py</li>
<li>2. POST an email #0
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
Please test your script in the sandbox provided, using the web server running on port 5000


Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 2-post_email.py</li>
<li>3. Error code #0
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).

You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
Please test your script in the sandbox provided, using the web server running on port 5000

File: 3-error_code.py</li>
<li>4. What's my status? #1
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following example (tabulation before -)
guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
guillaume@ubuntu:~/0x11$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 4-hbtn_status.py</li>
<li>5. Response header value #1
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header

You must use the packages requests and sys
You are not allow to import other packages than requests and sys
The value of this variable is different for each request
You don’t need to check script arguments (number and type) 
Repo:
GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 5-hbtn_header.py</li>
<li>6. POST an email #1
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

The email must be sent in the variable email
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to error check arguments passed to the script (number or type)
Please test your script in the sandbox provided, using the web server running on port 5000 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 6-post_email.py</li>
</ul>
<ul>
<li>7. Error code #1
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
Please test your script in the sandbox provided, using the web server running on port 5000 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 7-error_code.py</li>
<li>8. Search API
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
Please test your script in the sandbox provided, using the web server running on port 5000. All JSON generated by this server are random.

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 8-json_api.py</li>
<li>9. My GitHub!
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case, a personal access token as password)
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 10-my_github.py</li>
</ul>
<ul>
<p>Advanced task (not mandatory)</p>
<li>10. Time for an interview!
#advanced
Score: 0.0% (Checks completed: 0.0%)
The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:

Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
Write a Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
Only 17% of applicants for a backend position at Holberton finished this task in less than 15 minutes.
Be careful: only 60 requests by hour by IP for unauthenticated requests Rate limit

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 100-github_commits.py</li>
</ul>
