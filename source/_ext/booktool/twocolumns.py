from docutils import nodes
from docutils.parsers.rst import Directive

"""
Provide 2 directive:
    bk_begin2cols
    bk_end2cols
"""

class Begin2Cols(Directive):

    def run(self):
        begin_node = nodes.raw(format='latex', text='\\begin{multicols}{2}')
        return [begin_node]

class End2Cols(Directive):

    def run(self):
        end_node = nodes.raw(format='latex', text='\\end{multicols}')
        return [end_node]

def add_preamble(app, config):
    if 'preamble' not in config.latex_elements:
        config.latex_elements['preamble'] = ""   
    config.latex_elements['preamble'] += "\\usepackage{multicol}\n"

def setup(app):
    app.add_directive("bk_begin2cols", Begin2Cols)
    app.add_directive("bk_end2cols", End2Cols)
    app.connect('config-inited', add_preamble)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

