# Getting Started with Utterson
Very little is required to start using Utterson for a simple blog. If you are familiar with Jekyll, using Utterson will be dead simple. If you are not, don't worry we will try and guide you through it.

## Assumptions
This guide assumes the users is somewhat familiar with command line shells, web servers such as [Apache](http://httpd.apache.org/) or [nginx](http://nginx.org/), as well as basic static html files. If you are not the following section will give a _very_ brief overview.

### Website basics
In their most basic form, websites are a set of files shared from a server to the user's computer. A user uses a web browser such as [Google Chrome](https://www.google.com/intl/en/chrome/browser/) or [Mozilla Firefox](http://www.mozilla.org/en-US/firefox/new/) to access those files. The web server sends the files, generally in HTML format, to the web browser. The web browser then reads the files and generates the page you see. 

Utterson manages an application named Jekyll that generates the HTML files from a set of text files. The key item to understand is that you, the user, needs to have a web server and a means to relocate the generated files to it. 

## The basics of Jekyll and Utterson
To understand how Utterson works, you should understand how Jekyll, the core software Utterson manages, operates. Jekyll is capable of reading a set of files and generating a static website. Think of having a number of text files in one folder. Each file contains a post for your blog. Jekyll reads those files and then generates the proper HTML pages a web browser expects. There are a set of conventions Jekyll expects the files to adhere to. As long as those conventions are not violated, Jekyll can generate a full set of files that may be uploaded to a web server.

Expanding past this simple example, Jekyll is capable of much more than simply converting some text files to HTML pages. Jekyll provides the capabilities to define a complex web site and generate all the expected pages. The scope of Jekyll's abilities are not appropriate for this guide but they should be mentioned as Utterson does not restrict what could be done. Utterson's goal is to provide a simple method for performing the day to day tasks of managing a Jekyll blog. The blog itself can be customized to the end users preference.

## Starting a new Utterson site.
Starting a new Utterson site is extremely simple. By default Utterson includes a default site design that the user can then customize. Additional templates will be available in the future.

To start a new site you first should determine where you want to locate your Utterson site at. Navigate to that location and then call the Utterson executable with the -new parameter and a name. And example can be seen below.

1. Navigate to the location you would like your Utterson site to live. In the case of the demo it's _/tmp/UttersonDemo_. In most cases this will likely be somewhere in the users home folder. e.g /home/username

	```
	$ cd /tmp/UttersonDemo
	```
2. Build a new site using the -new switch. You may name your site anything you want. This will only name the __folder__ your site is located in. You will change the name that is displayed on the web pages later.

  ```
	/tmp/UttersonDemo $ utterson -new my_new_site
	Creating new utterson site at: my_new_site
	```
3. Now that the new site is created we can move into it. You will want to always be located within the site folder when running Utterson. Utterson does support running from outside the folder but you must provide the path to the site. In almost every case this is more work than it's worth.

  ```
  /tmp/UttersonDemo $ cd my_new_site/
  ```
4. Let's take a look at whats inside the folder. As you can see there is a config.yml file and then a folder titled jekyll_root. The config.yml file contains parameters that are only relevant to Utterson. For the most part this only specifies the location of the jekyll_root folder as well as some parameters for publishing. By default the parameters will work out of the box for a new site. **NOTE: ** This is not a required step, it's included for illustrative purposes.

  ```
	/tmp/UttersonDemo/my_new_site $ ls
	config.yml  jekyll_root
	/tmp/UttersonDemo/my_new_site $ ^C
	/tmp/UttersonDemo/my_new_site $ cat config.yml 
	site:
	  url: 
	  deployment_root: 
	  jekyll_root: ./jekyll_root
	  update_cmd: /path/to/update/script/or/cmd

	tags:
	  - default

	categories:
	  - default

	editing_app: vim
	```
5. From here we can now start Utterson. So far we have generated an Utterson site which technically also generated a Jekyll site behind the scenes. Utterson provides a menu system allowing the management of posts and tools for publishing.

  ```
  /tmp/UttersonDemo/my_new_site $ utterson
  ```
  ![Utterson Home Screen](/docs/images/GSG_5.png "Utterson Home Screen")
  
6. First we will configure the site by pressing **S**. This will take us to the settings screen. This screen allows us to scroll up and down using the arrow keys and select a setting to edit. In this case we will scroll to the **Site Name** setting and press **E** to edit it.

7. For this example we will change the name to __Awesome Site 9000__. Once changed press <enter> to save the changes. The same procedure should be used to update the site description. These values can be used by the Utterson template to automatically generate a header for the blog/site.

8. Next we will write out first post. To do so press **Q** to quit back to the main menu. Then press **P** to move to the posts screen. From here you can create/edit/delete drafts, templates, and published posts.

9. Press the **D** key to move to the drafts screen. This screen shows all the drafts that have been created. The menu on bottom shows the various actions you can take. By default an example draft is provided.

10. We will be creating a new draft so press the **N** key. A prompt will come up asking you for a name to the post file. Enter __myfirstpost.markdown__. Jekyll supports multiple types of markup syntax. Jekyll knowns what markup language you are using by the file extension. I personally prefer textile although in this example we will use markdown which is the default for Jekyll.

11. After pressing enter the new draft will be opened in the text editor specified in the settings. Utterson defaults to vim but it can be changed to any text editor that can be called via the command line. For example when editing in a visual environment I utilize Sublime Text.

12. Now we can edit our post. If you are familiar with Jekyll you will notice this is just a standard Jekyll post with some predefined meta-data. All of the meta_data filed are required for Utterson but you are free to add more as you would like. Utterson will happily ignore anything it doesn't understand. In this example we will update the title and body of the text. You will notice that we do not manually set the date_published or date_updated. Both of those are automatically updated by Utterson as needed.

13. After saving the file in the text editor you will see that the new draft is now in the list. To publish we will scroll down to the draft using the arrow keys and then press the **P** key. This will move the draft to the publish folder and also update the publish data. **NOTE:** This does not publish the post to the live site!

14. If we navigate back out with the **Q** key and then into the published documents via the **P** key we will see our newly published document.

15. Next we have a couple options. One we would publish the document to a web server. Or we could load a local web server and take a look at it before we publish. In our case we will go ahead and start up the local web server. To do that navigate to the home menu. Then press **X** to enter the tools menu. Finally press **S** to start the server. The menu item will update and you will see a notice at the top of the window once the server has started.

16. Next we can navigate to our new site using a web browser. Enter http://localhost:4000 into the address bar and press enter. You should see something similar to below. The look and feel is all determined by the default template. The template can be modified as much as the user would like.

17. Now that the site is looking good we can finally publish to our web server. Honestly, Utterson is a bit lacking in this area at the moment. The Publish option in the tools menu will run any arbitrary command you provide in the settings. For example, I use a shell script that executes a secured [rsync](http://rsync.samba.org/) command using shared ssh keys. Eventually we would like to support several backed solutions such as [rsync](http://rsync.samba.org/), [scp](http://en.wikipedia.org/wiki/Secure_copy), [git](http://git-scm.com/), and [github](https://github.com/) pages. 

## Beyond the basics
With all of the basics out of the way you can look towards the other features. Utterson currently provides most tools needed to manage posts. Eventually it will support management of tags, categories, dedicated pages, and other advanced functionality provided by the templates.