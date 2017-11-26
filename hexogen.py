
#!/usr/bin/python  
# -*- coding: utf-8 -*-


import time
import sys, getopt



def usage():
	print 'hexogen markdownfile ' + '-i' + ' filename' + ' -c' + ' category' + ' -t' +  ' 10000' ; 
	print "-i filename";
	print "-c category use str";
	print "[o]-t Stick to the top use number";
	print 'ex: hexogen -i test.md -c fengshui [-t 1000]';
	return;


def gen_time():
	return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));


def hexo_process(file_name,category_str,top_value):

	if len(file_name) <= 0:
		print 'filename is null';
		sys.exit();

	if len(category_str) <= 0:
		print 'category_str is null';
		sys.exit();

	prex_name_list = file_name.split('.');
	if len(prex_name_list) < 1:
		print 'file is error';
		sys.exit();




	_hexo_tile = '---\n';
	_hexo_tile += 'title: %s\n' %(prex_name_list[0]);
	_hexo_tile += 'author: admin\n';
	_hexo_tile += 'top: %s\n' %(top_value);
	_hexo_tile += 'data: %s\n' %(gen_time());
	_hexo_tile += 'categories: \n';
	_hexo_tile += '  - %s\n' %(category_str);
	_hexo_tile += '---\n';

	print _hexo_tile;

	with open (file_name, 'r') as original: 
		data = original.read () 
	with open (file_name, 'w') as modified: 
		modified.write ( _hexo_tile + data )


	print 'file write success!';

	return;



def do_main():


	opts,args = getopt.getopt(sys.argv[1:],'hi:c:t:')

	file_name = 'test.txt';
	top_value = 1000;


	if 0 >= len(opts):
		usage();
		sys.exit();

	top_num = 0;
	category = '';
	full_path = '';

	for op,value in opts:
		if '-h' == op:
			usage();
			sys.exit();
		elif '-c' == op:
			category = value;
		elif '-t' == op:
			top_num = value;
		elif '-i' == op:
			full_path = value;
		else:
			print '';


	hexo_process(full_path,category,top_num);

	return;


if __name__ == "__main__":
	do_main()


