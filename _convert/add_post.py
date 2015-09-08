import argparse
import sys
import os
import shutil
import nbformat 

from nbconvert import MarkdownExporter
from nbconvert.writers import FilesWriter
from traitlets.config import Config
from datetime import date

from urllib2 import quote

__author__ = 'Jeff Fossett'

def get_arguments(): 
	"""
	Get the arguments passed in at command line
	"""

	# argument parser
	parser = argparse.ArgumentParser(description='Simple utility to add posts to my blog.')

	parser.add_argument('-t', '--type', 
							help='What type of file are you trying to add [ipynb, rmd, md, txt]?', 
							required=True, 
							type=str, 
							choices=['md', 'rmd', 'ipynb', 'txt'])

	parser.add_argument('-l', '--loc', 
							help='Absolute path to the post', 
							required=True, 
							type=str)

	parser.add_argument('-b', '--blogdir', 
							help='Path to the base directory of the blog', 
							default = '/Users/jeffreyfossett/Files/blog')

	parser.add_argument('-a', '--assetdir', 
							help='Path to where assets should be stored',
							default = '/Users/jeffreyfossett/Files/blog/_assets/')	

	# return parsed arguments
	args = parser.parse_args()
	return args.type, args.loc, args.blogdir, args.assetdir


def get_name_w_date_from_path(floc, ds=None): 
	"Get the raw post name & path including dates"

	if not ds: 
		ds = str(date.today())

	ftypes = ['.txt', '.Rmd', '.md', '.ipynb']
	name = os.path.split(floc)[1].strip(' | '.join(ftypes))

	return  '{date}-{name}'.format(date=ds, name=name)


def make_post_asset_dir(name, assetdir):
	"Makes the directory where we will put the assets if it does not exist already"

	subdir_path = os.path.join(assetdir, name)

	if not os.path.isdir(subdir_path): 
		os.mkdir(subdir_path)

	return subdir_path


def process_ipynb(floc, blogdir, assetdir, tags=None, templatedir='/Users/jeffreyfossett/Files/blog/_convert/ipython', templatename='jekyll.tpl'): 
	"""
	Process an ipython notebook file 
	"""

	# name like '2015-09-06-my_post'
	name = get_name_w_date_from_path(floc)

	# makes the directory fo rthe assets and returns the path
	asset_subdir = make_post_asset_dir(name, assetdir)

	def path2support(path):
		return os.path.join(asset_subdir, path)

	c = Config({"Exporter":{"template_path":[templatedir], 
							"template_file": templatename, 
							"filters":{'path2support': path2support}
							}
				})

	# reader and writer
	exporter = MarkdownExporter(c)
	writer = FilesWriter()

	# set output location
	build_dir = os.path.join(blogdir, '_posts/')
	writer.build_directory = build_dir

	# get tags
	tags = tags + ['python', 'notebook'] if tags else ['python', 'notebook']

	# read and write
	nb_body, nb_resources = exporter.from_filename(floc, resources={'blogdir': blogdir, 'assetdir': assetdir, 'tags': tags})
	writer.write(nb_body, nb_resources, notebook_name = name)

	for f in nb_resources['outputs']: 
		# move files to the correct location
		shutil.move(os.path.join(build_dir, f), os.path.join(asset_subdir, f))


def process_rmd():
	raise NotImplementedError('Rmd processing not implemented')


def process_md(): 
	raise NotImplementedError('Md processing not implemented')


def process_txt():
	raise NotImplementedError('Txt processing not implemented')


if __name__ == '__main__': 

	ftype, floc, blogdir, assetdir = get_arguments()

	if ftype == 'ipynb':
		process_ipynb(floc, blogdir, assetdir)
	elif ftype == 'rmd': 
		process_rmd()
	elif ftype == 'md': 
		process_md()
	elif ftyp == 'txt': 
		process_txt()
	else: 
		raise ValueError('File type {ftype} is not supported'.format(ftype=ftype))