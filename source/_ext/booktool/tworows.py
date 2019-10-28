from docutils import nodes
from docutils.parsers.rst import Directive

"""
Provide 2 directive:
    bk_begin2rows
    bk_end2rows
"""

class Begin2Rows(Directive):

    has_content = True

    def run(self):
        begin_node = nodes.raw(format='latex', text='\n\\begin{tabular}{cc} \\multirow{2}{*}')
        offs = self.content_offset
        #inside_node = nodes.raw(format='latex', text='NIA')
        self.content_offset = self.state.nested_parse(self.content, offs, begin_node)
        begin_node.insert(1, nodes.raw(format='latex', text='\n&\n'))
        begin_node.insert(3, nodes.raw(format='latex', text='\n&\n'))
        print("NODE: %s" % begin_node[0])
        print("NODE: %s" % begin_node[1])
        print("NODE: %s" % begin_node[2])
        print("NODE: %s" % begin_node[3])
        print("NODE: %s" % begin_node[4])
        begin_node += nodes.raw(format='latex', text='\n\\end{tabular}\n')
        return [begin_node]

def add_preamble(app, config):
    if 'preamble' not in config.latex_elements:
        config.latex_elements['preamble'] = ""   
    config.latex_elements['preamble'] += "\\usepackage{multirow}\n"

def setup(app):
    app.add_directive("bk_2rows", Begin2Rows)
    app.connect('config-inited', add_preamble)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

