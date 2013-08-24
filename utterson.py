import yaml
import curses
import os
import subprocess
import shutil


def window_prep(stdscr, title, options):
  """Prepare the window by clearing it and ading a border."""
  curses.noecho()
  curses.cbreak()
  curses.curs_set(0)
  stdscr.keypad(True)
  stdscr.clear()
  stdscr.border(0)
  window_header(stdscr, title)

  if (options is not None):
    window_menu(stdscr, options)

def window_header(stdscr, title):
  header =  ' ' + title + (' ' * (curses.COLS - len(title) - 1))
  stdscr.addstr(0,0,header,curses.A_STANDOUT)

def notice_header(stdscr, notice):
  stdscr.addstr(0,curses.COLS - 50, notice[:50], curses.A_STANDOUT)

def window_menu(stdscr, options):
  opstr = ''
  for key, value in options.items():
    opstr += (key + " - " + value + "   ")
    stdscr.addstr(curses.LINES - 1 , 2, opstr)

def home_screen(stdscr):
  """Runs the home screen"""

  redraw = True
  key = 0

  # Run event loop on keys.
  while (key != ord('q') and key != ord('Q')):

    if (redraw):
      # Write the main menu.
      window_prep(stdscr, "utterson", None)
      stdscr.addstr(2,5,"P - Posts")
      stdscr.addstr(3,5,"S - Setup")
      stdscr.addstr(4,5,"U - Users")
      stdscr.addstr(5,5,"C - Categories")
      stdscr.addstr(6,5,"Q - Quit")


      stdscr.addstr(2,45,"Configuration Values")
      stdscr.addstr(3,30,'   Title: ' + config["site"]["site_title"])
      stdscr.addstr(4,30,'     URL: ' + config["site"]["url"])
      stdscr.addstr(5,30,'Dep Root: ' + config["site"]["deployment_root"])
      stdscr.addstr(6,30,'Jek Root: ' + config["site"]["jekyll_root"])



      stdscr.refresh()
      redraw = False

    key = stdscr.getch()

    if (key == ord('p') or key == ord('P')):
      posts_main_screen(stdscr)

      # Prep the window.
      window_prep(stdscr, "utterson: Home", None)
      redraw = True

def published_post_screen(stdscr):

  window_prep(stdscr, "utterson:published posts", None)
  stdscr.refresh()

  posts = []
  for f in os.listdir(config['site']['jekyll_root'] + "_posts"):
    if os.path.isfile(config['site']['jekyll_root'] + "_posts/" + f):
      posts.append(f)
  posts.sort(reverse=True)
  il = ItemsListWindow(posts)
  il.set_window_size({'left_type': 'relative', 'left_value': 2,
                       'right_type': 'relative', 'right_value': 50,
                       'bottom_type': 'relative', 'bottom_value': 2,
                       'top_type' : 'relative', 'top_value': 2,
                       'height': 10,
                       'width': 15})
  il.build_item_list()
  il.refresh_window()
  

  key = 0
  while (key != ord('q')):

    key = stdscr.getch()

    if (key == curses.KEY_DOWN):
      il.select_down()
    elif (key == curses.KEY_UP):
      il.select_up()

def draft_post_screen(stdscr):

  redraw = True
  rebuild_file_list = True
  notice_txt = None
  

  key = 0
  while (key != ord('q') and key != ord('Q')):

    if (rebuild_file_list):
      posts = []
      for f in os.listdir(config['site']['jekyll_root'] + "_posts/_drafts"):
        if os.path.isfile(config['site']['jekyll_root'] + "_posts/_drafts/" + f):
          posts.append(f)
      posts.sort(reverse=True)
      il = ItemsListWindow(posts)
      il.set_window_size({'left_type': 'relative', 'left_value': 2,
                           'right_type': 'relative', 'right_value': 50,
                           'bottom_type': 'relative', 'bottom_value': 2,
                           'top_type' : 'relative', 'top_value': 2,
                           'height': 10,
                           'width': 15})
      rebuild_file_list = False

    if (redraw):
      window_prep(stdscr, "utterson:draft posts", {'Q': 'Quit', 'E': 'Edit', 'P': 'Publish'})
      if (notice_txt is not None):
        notice_header(stdscr,notice_txt)
        notice_txt = None
      stdscr.refresh()
      il.build_item_list()
      il.refresh_window()
      

      redraw = False


    key = stdscr.getch()

    if (key == curses.KEY_DOWN):
      il.select_down()
    elif (key == curses.KEY_UP):
      il.select_up()
    elif (key == ord('e') or key == ord('E')):
      selected = il.get_selected()
      subprocess.call(['vim', config['site']['jekyll_root'] + "_posts/_drafts/" + selected])
      redraw = True
    elif (key == ord('p') or key == ord('P')):
      selected = il.get_selected()
      sure = yes_no_prompt(stdscr, 'Publish?: ' + selected + ' (y/n)')
      if (sure):
        shutil.move(config['site']['jekyll_root'] + "_posts/_drafts/" + selected,
                    config['site']['jekyll_root'] + "_posts/" + selected)
        rebuild_file_list = True
        redraw = True
        notice_txt = 'Published: ' + selected
      else:
        redraw = True


def template_post_screen(stdscr):

  window_prep(stdscr, "utterson:templates", None)
  stdscr.refresh()

  posts = []
  for f in os.listdir(config['site']['jekyll_root'] + "_posts/_templates"):
    if os.path.isfile(config['site']['jekyll_root'] + "_posts/_templates/" + f):
      posts.append(f)
  posts.sort(reverse=True)
  il = ItemsListWindow(posts)
  il.set_window_size({'left_type': 'relative', 'left_value': 2,
                       'right_type': 'relative', 'right_value': 50,
                       'bottom_type': 'relative', 'bottom_value': 2,
                       'top_type' : 'relative', 'top_value': 2,
                       'height': 10,
                       'width': 15})
  il.build_item_list()
  il.refresh_window()
  

  key = 0
  while (key != ord('q')):

    key = stdscr.getch()

    if (key == curses.KEY_DOWN):
      il.select_down()
    elif (key == curses.KEY_UP):
      il.select_up()

def posts_main_screen(stdscr):
  """Displays and manages the posts main screen."""

  redraw = True
  key = 0

  # Run event loop on keys
  while key != ord('q'):

    if (redraw):
      # Write the left menu.
      window_prep(stdscr, "utterson: Posts", {'Q': 'Quit'})
      stdscr.addstr(2,2,'D - Drafts')
      stdscr.addstr(3,2,'P - Published Posts')
      stdscr.addstr(4,2,'T - Templates')  

    key = stdscr.getch()

    if (key == ord('d') or key == ord('D')):
      draft_post_screen(stdscr)
      redraw = True

      # Obtain all the posts and display.
        

    if (key == ord('p') or key == ord('P')):
      published_post_screen(stdscr)
      redraw = True

    if (key == ord('t') or key == ord('T')):
      template_post_screen(stdscr)
      redraw = True


def load_configuration(config_file_dir):
  stream = open(config_file_dir, 'r')
  global config
  config = yaml.load(stream)
  stream.close()

def yes_no_prompt(stdscr, question):
  lines_offset = (curses.LINES - 3) // 2
  cols_offset = (curses.COLS - len(question) - 2) // 2
  window = curses.newwin(3,len(question) + 2, lines_offset, cols_offset)
  window.border(0)
  window.addstr(1,1,question)
  window.refresh()

  while (True):
    key = stdscr.getch()

    if (key == ord('y') or key == ord('Y')):
      return True
    elif (key == ord('n') or key == ord('N')):
      return False

def main():
	
  # Load configuration file and globals.
  load_configuration('config.yml')

  # Build Main Window
  stdscr = curses.initscr()
  curses.noecho()
  curses.cbreak()
  curses.curs_set(0)
  stdscr.keypad(True)

  # Starte home screen.
  home_screen(stdscr)
  

  # Exit
  curses.endwin()	
















class ItemsListWindow:
  """

  Creates a navigatble items list.

  The ItemsListWindow class provides a basic ncurses based items list. and a
  dedicated ncurses window is created for it. The location and size of the 
  window may be specified. The instance also provides navigation/selection. 


  """

  def __init__(self, items):
    """Initialized the default values."""
    self.items = items
    self.selected_line = -1
    self.last_top_line = 0


  def set_window_size(self, options):
    """

    Sets the size of the ncurses window that the list will utilize.

    The window size may be supplied as both absolute and relative values.
    The options paramter should be a dictionary containg the following
    items. By default the height and width are only utilized when
    an absolute type is specified.

    {'left_type': 'relative', 'left_value': 2,
     'right_type': 'relative', 'right_value': 15,
     'bottom_type': 'relative', 'bottom_value': 10,
     'top_type': 'relative', 'top_value': 10,
     'height': 10,
     'width': 10}

    """

    self.window_width = 0
    self.window_cols_offset = 0
    self.window_height = 0
    self.window_rows_offset = 0

    # Determine width
    if (options['left_type'] == 'relative'):
      if (options['right_type'] == 'relative'):
        # Double relative width. Determine largest possible width.
        self.window_width = curses.COLS - options['left_value'] - options['right_value']
        self.window_cols_offset = options['left_value']
      else:
        # The right is absolute so we need to use the width value.
        if (curses.COLS < (options['left_value'] + options['width'])):
          # The width is too large so reduce.
          self.window_width = (curses.COLS - options['left_value'])
        else:
          self.window_width = options['width']

        self.window_cols_offset = options['left_value']
    elif(options['right_type'] == 'relative'):
      # Relative right with absolute left.
      if (curses.COLS < (options['right_value'] + options['width'])):
        self.window_width = (curses.COLS - options['right_value'])
      else:
        self.window_width = options['width']

      # The right is relative so calc it based on width.
      self.window_cols_offset = curses.COLS - options['width'] - options['right_value']
    else:
      # Must be all absolute so set to zero.
      self.window_width = options['width']
      self.window_cols_offset = 0

    # Determine height
    if (options['top_type'] == 'relative'):
      if (options['bottom_type'] == 'relative'):
        # Double relative height. Determine largest possible height.
        self.window_height = curses.LINES - options['top_value'] - options['bottom_value']
        self.window_rows_offset = options['top_value']
      else:
        # The bottom is absolute so we need to use the height value.
        if (curses.LINES < (options['top_value'] + options['height'])):
          # The height is too large so reduce.
          self.window_height = (curses.LINES - options['top_value'])
        else:
          self.window_height = options['height']

        self.window_rows_offset = options['top_value']
    elif(options['bottom_type'] == 'relative'):
      # Relative bottom with absolute top.
      if (curses.LINES < (options['bottom_value'] + options['height'])):
        self.window_height = (curses.LINES - options['bottom_value'])
      else:
        self.window_height = options['height']

      # The bottom is relative so calc it based on height.
      self.window_rows_offset = curses.LINES - options['height'] - options['bottom_value']
    else:
      # Must be all absolute so set to zero.
      self.window_height = options['height']
      self.window_rows_offset = 0


    # Build the window
    self.window = curses.newwin(self.window_height,self.window_width, self.window_rows_offset, self.window_cols_offset)
        
  def select_down(self):
    """Moves the selected row up."""


    if (self.selected_line < len(self.items) - 1):
      self.selected_line += 1

      # Determin what the top line should be.
      if ((self.selected_line - self.last_top_line) >= self.get_visible_lines()):
        self.last_top_line += 1

    self.build_item_list()
    self.refresh_window()

  def select_up(self):
    """Moves the selected row down."""
    if (self.selected_line > 0):
      self.selected_line -= 1

      # If the top line is out of range move the range.
      if (self.last_top_line > self.selected_line):
        self.last_top_line = self.selected_line

    self.build_item_list()
    self.refresh_window()

  def get_selected(self):
    return self.items[self.selected_line]

  def refresh_window(self):
    """Refreshes the window"""
    self.window.refresh()

  def get_visible_lines(self):
    """Determines the actual visible lines for redrawing."""

    if (len(self.items) > self.window_height):
      visible_lines = self.window_height
    else:
      visible_lines = len(self.items)

    return visible_lines

  def build_item_list(self):
    """Rebuilds the ncurses window."""
    #Calculate the maximum number of rows possible.

    visible_lines = self.get_visible_lines()
    
    line_number = 0
    for item_number in range(self.last_top_line, self.last_top_line + self.get_visible_lines()):
      if item_number == self.selected_line:
        self.window.addstr(line_number, 0, self.items[item_number], curses.A_STANDOUT)
      else:
        self.window.addstr(line_number, 0, self.items[item_number])
      line_number += 1


































# Start utterson
main()
