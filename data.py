# -*- coding: utf8 -*-
from threading import Thread
from datetime import datetime

def table_head_builder(table_head_line):
    head_top = '''
    <thead>
<tr>
    '''

    head_bottom = '''
    </tr>
</thead> 
    '''

    head_content = '''
    <th style="cursor: pointer;" _sorttype="us">%s<img src="http://tablefilter.free.fr/TableFilter/TF_Themes/blank.png" class="sort-arrow"></th>
    <th style="cursor: pointer;" _sorttype="us">%s<img src="http://tablefilter.free.fr/TableFilter/TF_Themes/blank.png" class="sort-arrow"></th>
    <th style="cursor: pointer;" _sorttype="us">%s<img src="http://tablefilter.free.fr/TableFilter/TF_Themes/blank.png" class="sort-arrow"></th>
    <th style="cursor: pointer;" _sorttype="us">%s<img src="http://tablefilter.free.fr/TableFilter/TF_Themes/blank.png" class="sort-arrow"></th>
    ''' % (table_head_line.split(',')[0], table_head_line.split(',')[1], table_head_line.split(',')[2],
           table_head_line.split(',')[3])
    head_source = head_top + head_content + head_bottom
    return head_source


def table_tr_builder(table_tr):
    table_tr_string = '''
    <tr>
      <td align="middle">%s</td>
      <td align="middle">%s</td>
      <td align="middle">%s</td>
      <td align="middle">%s</td>
    </tr>
    ''' % (table_tr.split(',')[0], table_tr.split(',')[1], table_tr.split(',')[2], table_tr.split(',')[3])
    return table_tr_string


def html_generator():
    html_top = '''<!doctype html>
<html>
<head>
<title></title>
<style type="text/css" media="screen">
	body{ 
		margin:15px; padding:15px; border:1px solid #666;
		font-family:Arial, Helvetica, sans-serif; font-size:88%; 
	}
	h2{ margin-top: 50px; }
	pre{ margin:5px; padding:5px; background-color:#f4f4f4; border:1px solid #ccc; }
	/* for elements added by sortable.js in th tags*/
	th img{ border:0; } 
	th a{ color:#fff; font-size:13px; text-transform: uppercase; text-decoration:none; }
	.helpCont{
	display:none;
	}	
</style>
<link rel="stylesheet" type="text/css" href="http://tablefilter.free.fr/includes/SyntaxHighlighter/Styles/SyntaxHighlighter.css">
<link id="demo_style" type="text/css" rel="stylesheet" href="http://tablefilter.free.fr/TableFilter/filtergrid.css">
<script src="http://tablefilter.free.fr/TableFilter/tablefilter_min.js" language="javascript" type="text/javascript"></script>
<script language="javascript" type="text/javascript"> 
//<![CDATA[
	tf_AddEvent(window,'load',initHighlighter);
	function initHighlighter()
	{
		dp.SyntaxHighlighter.ClipboardSwf = "includes/SyntaxHighlighter/Scripts/clipboard.swf";  
		dp.SyntaxHighlighter.HighlightAll("code"); 
	}
	
	/*** IE only: show/hide selects during filtering operations ***/
	function hideIESelects()
	{
		if(tf_isIE)
		{
			var slc = tf.tbl.getElementsByTagName('select');
			for(var i=0; i<slc.length; i++)
				slc[i].style.visibility = 'hidden';
		}
	}
	
	function showIESelects()
	{
		if(tf_isIE)
		{
			var slc = tf.tbl.getElementsByTagName('select');
			for(var i=0; i<slc.length; i++)
				slc[i].style.visibility = 'visible';
		}
	}
//]]>
</script>
<script id="populateSelect" type="text/javascript" src="http://tablefilter.free.fr/TableFilter/TF_Modules/tf_populateSelect.js"></script>
<script id="loader" type="text/javascript" src="http://tablefilter.free.fr/TableFilter/TF_Modules/tf_loader.js"></script>
<script id="sort" type="text/javascript" src="http://tablefilter.free.fr/TableFilter/TF_Modules/tf_sort.js"></script>
<script id="rowsCounter" type="text/javascript" src="http://tablefilter.free.fr/TableFilter/TF_Modules/tf_rowsCounter.js"></script>
<script id="cookies" type="text/javascript" src="http://tablefilter.free.fr/TableFilter/TF_Modules/tf_cookies.js"></script>
<script id="statusBar" type="text/javascript" src="http://tablefilter.free.fr/TableFilter/TF_Modules/tf_statusBar.js"></script>
<script id="resetBtn" type="text/javascript" src="http://tablefilter.free.fr/TableFilter/TF_Modules/tf_resetBtn.js"></script>
<script id="alternateRows" type="text/javascript" src="http://tablefilter.free.fr/TableFilter/TF_Modules/tf_alternateRows.js"></script>
<script id="sortabletable" type="text/javascript" src="http://tablefilter.free.fr/TableFilter/sortabletable.js"></script>
<script id="sortabletable_adapter" type="text/javascript" src="http://tablefilter.free.fr/TableFilter/tfAdapter.sortabletable.js"></script>
</head>
<body>
<table id="demo" cellpadding="0" cellspacing="0" width="100%" class=" TF">
    '''

    html_bottom = '''</table>
<script language="javascript" type="text/javascript">
//<![CDATA[	
	var props = {
		filters_row_index: 1,
		sort: true,
		sort_config: {
			sort_types:['String','String','US','US','US','US','US','US','US']
		},
		remember_grid_values: true,
		alternate_rows: true,
		rows_counter: true,
		rows_counter_text: "Displayed rows: ",
		btn_reset: true,
		btn_reset_text: "Clear",
		btn_text: " > ",
		loader: true,
		loader_text: "Filtering data...",
		loader_html: '<img src="loader.gif" alt="" ' +
				'style="vertical-align:middle;" /> Loading...',
		on_show_loader: hideIESelects, //IE only: selects are hidden when loader visible
		on_hide_loader: showIESelects, //IE only: selects are displayed when loader closed
		col_0: "select",
		col_1: "select",
		col_2: "select",
		col_9: "none",
		display_all_text: "< Show all >",
		col_width: ["15%","10%","10%","10%","13%","10%","12%","10%","10%"]
	}
	var tf = setFilterGrid("demo",props);
//]]>
</script>
</body>
</html>'''

    html_table_source = ''''''
    with open('stdout_csv ' + datetime.now().strftime("%m-%d-%Y") + ".csv", 'r') as data_file:
        n = 1
        for line in data_file:
            line = line.replace('\n', '')
            if n == 1:
                html_table_source = html_table_source + table_head_builder(line)
            if n != 1:
                html_table_source = html_table_source + table_tr_builder(line)
            n += 1

    html_source = html_top + html_table_source + html_bottom
    with open('data.html', 'w') as html_file:
        html_file.write(html_source)
        html_file.close()


Thread(target=html_generator()).start()
