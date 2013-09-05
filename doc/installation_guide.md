# Installation Guide
Installation of utterson can be performed via executing setup or using pip. 
The recommended method is to use pip when available.


## Requirements
Utterson has a small list of requirements. Currently the installation will 
not automatically install them. Besides the basic python modules, requirements
 utterson obviously requires having Jekyll installed. Comments regarding the 
Jekyll installation are provided but it's up to the end user to determine 
the best method to install Jekyll.

* [Python3](http://www.python.org/)
* [pip](https://pypi.python.org/pypi/pip) - If installing via pip
* [PyYaml](http://pyyaml.org/) - Python YAML module utilized by utterson
* [Jekyll](http://jekyllrb.com/)

## Installation Methods
The following are general installation methods used for various platforms. 
Additionally a generalize overview for all platforms is provided.

### General Steps

* Install Python3
* Install Setuptools for Python3
* Install pip
* Install PyYaml via pip
* Install Utterson via pip
* Install Jekyll (One possible method)
 * Install rvm
 * Install ruby 2.0.0 (Or latest version)
 * Install Jekyll via ruby gems (make sure to use 2.0.0)

### Debian based Linux distribution installation (Debian, Ubuntu, LinuxMint)
The follow provides a step-by-step guide to install utterson on a Debian
 based Linux distribution. Depending on the distribution you may need not
 need to issue sudo on each command. Additionally the installation steps
 are not the only way to accomplish the installation.

1. __Install Python 3__

   ```
   sudo apt-get install python3
   ```
2. __Install SetupTools__

	 ```
	 sudo apt-get install python3-setuptools
	 ```
3. __Install pip__

   ```
	 sudo curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | sudo python3
   ```
4. __Install PyYaml with pip__

   ```
   sudo pip install pyyaml
   ```
5. __Install rvm___

   ```
   sudo \curl -L https://get.rvm.io | bash
   ```
6. __Install Ruby__

   ```
   sudo rvm install 2.0.0
   ```
7. __Install Jekyll__

   ```
   sudo rvm use 2.0.0
   sudo gem install jekyll
   ```

# Mac OS X 
Unfortunately I haven't had a chance to detail the Mac OS X installation 
instructions. For the most part they mirror the Debian instructions but 
for installing Python3. Below is how I _remember_ the installation going.

1. __Install Python 3__

   Python instillation is handled via python installed located 
   [here](http://www.python.org/download/)
2. __Install SetupTools__

	 ```
	 sudo wget https://bitbucket.org/pypa/setuptools/downloads/ez_setup.py -O - | python3
	 ```
3. __Install pip__

   ```
	 sudo curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | sudo python3
   ```
4. __Install PyYaml with pip__

   ```
   sudo pip install pyyaml
   ```
5. __Install rvm___

   ```
   sudo \curl -L https://get.rvm.io | bash
   ```
6. __Install Ruby__

   ```
   sudo rvm install 2.0.0
   ```
7. __Install Jekyll__

   ```
   sudo rvm use 2.0.0
   sudo gem install jekyll

### Mac OS X Configure Terminal
By default the Mac OS X Terminal application does not send a Ctrl-H when the 
delete key is pressed. The following steps will correct this.

* Open the Terminal Application
* Terminal => Preferences
* Settings => Advanced Tab
* Check the 'Delete sends Ctrl-H

